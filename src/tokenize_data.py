import sys
import re
import json

words = []
pos_tags = []
chunk_tags = []

with open(sys.argv[1], "r") as f:
    for line in f:
        if(line.rstrip()):
            line = re.sub("\s+", " ", line)
            line = line.split(";")
            chunk1 = line[0].split(" ")
            chunk2 = line[1].split(" ")

            if(chunk1[0] == "H"):
                if chunk1[1] not in words:
                    words.append(chunk1[1])
                if chunk1[3] not in chunk_tags:
                    chunk_tags.append(chunk1[3])
                if chunk1[4] not in pos_tags:
                    pos_tags.append(chunk1[4])

            if chunk2[2] not in words:
                words.append(chunk2[2])
            if chunk2[4] not in chunk_tags:
                chunk_tags.append(chunk2[4])
            if chunk2[5] not in pos_tags:
                pos_tags.append(chunk2[5])


words.append("ROOT")
pos_tags.append("ROOT")
chunk_tags.append("ROOT")

data = {}
data["words"] = words
data["tags"] = pos_tags
data["chunk_tags"] = chunk_tags

json.dump(data, open("data_tokens.json", "w"))

print("Total no. of words: " + str(len(words)))
print("Total no. of pos_tags: " + str(len(pos_tags)))
print("Total no. of chunk_tags: " + str(len(chunk_tags)))
