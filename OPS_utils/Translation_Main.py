from Translation_Index import Translation_Index
import shutil

# origin_path = r'\\brnpim7pro01\folders\ImportArchive\Translations\TPlus'
origin_path = 'C:/E-Commerce/Test1'

# dest_path = '\\brnpim7pro01\folders\inbox\hotfolder'
dest_path = 'C:/E-Commerce/Test2'

# directory and name of index
index_directory = "indexdir"
index_name = "trans_index"



# put in a while loop for the brand numbers here

brands = {'1': 'Jack and Jones', '2': 'Mamalicious/Minimize', '3': 'Name It', '4': 'Object', '5': 'Only (1)', '6': 'Only (2)',
          '7': 'Pieces', '8': 'Selected', '9': 'Vila', '10': 'Vero Moda/Noisy May', '11': 'J Lindeberg', '12': 'Junarose',
          '16': 'YAS', '18': 'Only & Sons', '19': 'ADPT', '20': 'Produkt'}

index = Translation_Index(origin_path, index_directory, index_name)

# while True:
#     brand_number = input("Please enter the brand number (for a list of brands and their numbers, press 'B') or 'Q' or 'q' to quit: ")
#
#     if brand_number == "B":
#         print(brands)
#     if brand_number == "q" or brand_number == "Q":
#         raise SystemExit
#     if brand_number in brands:
#         break

while True:

    prompt = "Please enter the EDI Style Number or 'Q' or 'q' to quit: "
    try:
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
            shutil.copy2(file, dest_path)