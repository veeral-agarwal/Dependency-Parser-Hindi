from sys import argv
import re
import json

tags,chunk_tags,root,words = [],[],[],[]

li = 0
f = open(argv[1], "r")
for line in f:
    li += 1
    print(li)
    if(line.rstrip()):
        line = re.sub("\s+"," ",line)
        line1 = line.split(";")

        a1 = line1[0].split(" ")
        a2 = line1[1].split(" ")

        if(a1[0] == "H"):
            if a1[1] not in words:
                indx = len(words)
                words.insert(indx , a1[1])
            if a1[2] not in root:
                indx = len(root)
                root.insert(indx , a1[2])
            if a1[3] not in chunk_tags:
                indx = len(indx,chunk_tags)
                chunk_tags.insert(a1[3])
            if a1[4] not in tags:
                indx = len(tags)
                tags.insert(indx,a1[4])

        
        if a2[2] not in words:
            indx = len(words)
            words.insert(indx , a2[2])
        if a2[3] not in root:
            indx = len(root)
            root.insert(indx,a2[3])
        if a2[4] not in chunk_tags:
            indx = len(chunk_tags)
            chunk_tags.insert(indx,a2[4])
        if a2[5] not in tags:
            indx = len(tags)
            tags.insert(indx,a2[5])	


print(len(words))					
print(len(root))					
print(len(tags))					
print(len(chunk_tags))

words.append("ROOT")
root.append("ROOT")
tags.append("ROOT")
chunk_tags.append("ROOT")

data = {}
data["words"] = words
data["root"] = root
data["tags"] = tags
data["chunk_tags"] = chunk_tags

with open("data_lists.json","w") as f:
	json.dump(data,f)