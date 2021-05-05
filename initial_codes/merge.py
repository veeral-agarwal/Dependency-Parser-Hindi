import os
import sys
import re

data = '../Data/'
dev = data + 'Development/'
test = data + 'Testing/'
train = data + 'Training/'


def merge_files(path, outpath):
    files = os.listdir(path)
    sentences = []
    i = 1
    for file in files:
        f = open(path + file).read()
        reg = re.compile(r"<Sentence id='.*?'>.*?<\/Sentence>", re.S)
        data = reg.findall(f)
        for sentence in data:
            sentence = "<Sentence id='"+ str(i) + "'>" + sentence[sentence.find('\n'):]
            i += 1
            sentences.append(sentence)

    for sentence in sentences:
        print(sentence)

    return i

if len(sys.argv) > 2:
    merge_files(argv[1], argv[2])
else:
     merge_files(dev, 'out.txt')