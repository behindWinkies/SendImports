from Translation_Index import Translation_Index
import shutil
import sys

origin_path = r'\\brnpim7pro01\folders\ImportArchive\Translations\TPlus'
# for testing # origin_path = 'C:/E-Commerce/Test1'

dest_path = r'\\brnpim7pro01\folders\inbox\hotfolder'
# for testing # dest_path = 'C:/E-Commerce/Test2'

# directory and name of index
index_directory = "indexdir"
index_name = "trans_index"

index = Translation_Index(origin_path, index_directory, index_name)

while True:

    prompt = "Please enter the EDI Style Number or 'Q' or 'q' to quit: "
    try:
        print(prompt)
        EDISN = input(prompt)
    except ValueError:
        print(prompt)
        continue

    if not (EDISN.isnumeric() or EDISN == "Q" or EDISN == 'q'):
        print(prompt)
    elif EDISN == "q" or EDISN == "Q":
        raise SystemExit
    else:
        EDISN = int(EDISN)
        result_list = index.get_most_recent(EDISN)
        if not result_list:
            print("No translations found in the past year for this EDI Style Number.")
        for file in result_list:
            for i in range(50):
                try:
                    shutil.copy2(file, dest_path)
                except FileNotFoundError:
                    continue
                else:
                    break
