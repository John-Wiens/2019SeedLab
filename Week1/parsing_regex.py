import re

text = str(raw_input("Please Enter Some Text:\n"))
contains = re.search("abcd",text)
if contains is not None:
    print("Found the String abcd!")

else:
    print("String abcd is not present.")

