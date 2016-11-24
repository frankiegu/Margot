import re
fp = open("sample.txt", 'r')
data = fp.read().split("\n")
form_data = [re.sub('[0-9]+\t', '', x) for x in data]
fp.close()
fp  = open("limited_corpus.txt", "w")
for x in form_data:
    fp.write("<s> " + x.lower() + " </s>\n") 
fp.close()
