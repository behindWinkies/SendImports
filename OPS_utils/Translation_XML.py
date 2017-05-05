import xml.etree.ElementTree as ET

class Translation_XML:

    def __init__(self, file):
        self.file = file

    # Returns a list of all distinct EDI Style Numbers in XML file

    def edisn_list(self):

        result = []
        tree = ET.parse(self.file)
        root = tree.getroot()
        for item in root.iter('Item'):
            style = item.attrib
            style_id = int(style['style-id'])
            if style_id not in result:
                result.append(style_id)
        return result


    # Return the country code for the given file

    def get_country(self, file_name):

        start = len(file_name) - 2
        if '.xml' in file_name:
            start = len(file_name) - 6
            end = len(file_name) - 4
        else:
            start = len(file_name) - 2
            end = len(file_name)
        return file_name[start:end]