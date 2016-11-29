

fp = open('corpus_step3.txt', 'r')
data = fp.readlines()
fp.close()
fp = open('formatted_corpus.txt', 'w')
for line in data :
    fp.write("<s> " + line.strip('\n') + " </s>\n")
fp.close()
