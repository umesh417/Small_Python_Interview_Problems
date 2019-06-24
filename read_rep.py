import re

word = raw_input("Enter the word ")
with open('fani.txt') as f:
    text = f.read()
#    print(type(read_data))
#    read_data.split()
#    find = "\\b" + word + "\\b"
#    result = re.findall(find, text)
    result = re.findall('\\b'+word+"\\b", text, flags=re.IGNORECASE)
    if len(result)>0:
        print(len(result))
    else:
        print("Not there..")
