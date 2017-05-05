from whoosh import index
from whoosh.fields import Schema, ID, NUMERIC, KEYWORD
from whoosh.qparser import QueryParser
import os
import time
from Translation_XML import Translation_XML
from operator import itemgetter

class Translation_Index:

    # Constructor: takes folder directory, index directory and index name as inputs

    def __init__(self, directory, index_dir, index_name):
        self.directory = directory
        self.index_dir = index_dir
        self.index_name = index_name
        os.chdir(self.directory)


    # Creates an index in the given location, using the given directory as a list of files

    def create_index(self):

        schema = Schema(created_time=NUMERIC(stored=True, sortable=True),
                        file_name=ID(stored=True, sortable=True),
                        # brand_num=ID(stored=True, sortable=True),
                        edisns=KEYWORD,
                        country=ID(stored=True, sortable=True))
        if not os.path.exists(self.index_dir):
            os.mkdir(self.index_dir)

        ix = index.create_in(self.index_dir, schema, self.index_name)


    # Indexes the files in directory, with file name, modification time and EDI Style Numbers as stored fields

    def index_files(self):

        # time since the epoch minus one year (in seconds)
        max_mtime = time.time() - 31557600

        # If the index does not exist, create it
        if not index.exists_in(os.path.join(self.directory,self.index_dir), self.index_name):
            print("(Re-)Creating Index. Please wait.")
            self.create_index()

        ix = index.open_dir(self.index_dir, self.index_name)
        writer = ix.writer()
        direc = os.getcwd()

        # Walk through the directory and add files that are less than one year old
        print("Adding files to the index. Please wait.")
        for root, dirs, files in os.walk(direc):
            for name in files:

                mtime = os.path.getmtime(name)
                trans_xml = Translation_XML(name)
                edisn_list = trans_xml.edisn_list()
                # make the list into a string and encode into utf-8
                stripped_list = " ".join(str(x) for x in edisn_list)
                encoded_list = str(stripped_list).encode("utf-8").decode("utf-8")
                country = trans_xml.get_country(name)
                if mtime > max_mtime:
                    #print(name)
                    writer.add_document(created_time=mtime, file_name=name, edisns=encoded_list, country=country)

            # When done walking through files, stop
            break
        print("Index is complete.")
        writer.commit()


    # Input: EDI Style Number
    # Output: a list of lists; each internal list contains a file name, its creation time and its country code

    def get_translations(self, edisn):

        result = []
        if not index.exists_in(os.path.join(self.directory, self.index_dir), self.index_name):
            print ("No index exists in the current directory")
            return False

        # Query the EDISN keyword field in the index
        ix = index.open_dir(self.index_dir, self.index_name)
        qp = QueryParser("edisns", schema = ix.schema)
        edisn_str = str(edisn)
        q = qp.parse(edisn_str)

        # Append each resulting list to the list of results
        with ix.searcher() as searcher:
            for file in searcher.search(q):
                temp = file.values()
                result.append(temp)

        return result


    # Input: EDI Style Number
    # Output: A list of the most recent files for this EDI Style Number, one per country

    def get_most_recent (self, edisn):

        result = []

        languages = ['nl', 'fi', 'fr', 'de', 'no', 'es', 'sv', 'da', 'it']
        edisn_matrix = self.get_translations(edisn)

        # find the files from the index per language
        for lang in languages:
            temp_list = []
            for list in edisn_matrix:
                if list[0] == lang:
                    temp_list.append(list)
            # if the list for the language is not empty, append the most recently modified
            if temp_list:
                maximum = max(temp_list,key=itemgetter(1))[2]
                result.append(maximum)

        return result