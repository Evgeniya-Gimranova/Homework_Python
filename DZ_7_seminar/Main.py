from os.path import exists
from Creating_csv_file import creating
from Write_file import writing_scv
from Write_file import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()
