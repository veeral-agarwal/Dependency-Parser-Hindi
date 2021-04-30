from sys import argv
import re
count,cnt,w = 0,0,0

head_const_tags = ""
head_tag = 0
tags = {
    "NP": [],"JJP": [],"CCP": [],"VGNF": [],"VGF": [],"BLK": [],"VGNN": [],"RBP": [],"FRAGP": [],"NEGP": []
}

f = open(argv[1], "r")

for line in f:
    if (line.rstrip()):
        line = re.sub("\s+"," ",line)
        troot = 0 
        line1 = line.split(' ')
        if (line1[0] == "<Sentence"):
            count +=1
            print("<Sentence id=" + "\'" + str(count) + "\'>")
        elif(line1[0].strip() == "</Sentence>"):
            print(line1[0].strip())    
        elif(line1[0].strip() == "))"):

            if head_const_tags not in tags[str(head_tag)]:
                indx = len(tags[str(head_tag)])
                tags[str(head_tag)].insert(indx,head_const_tags)
            troot = 0
            continue
        elif(line1[1] == "(("):
            head_const_tags = ""
            relation,relative,drel,name,head_tag = 0,0,0,0,0
            if(line1[2].split("_")[0] == "NULL"):
                head_tag = line1[2].split("_")[2]
            else:
                head_tag = line1[2]
                    
            for i in range(4,len(line1)):
                if(line1[i].split("=")[0] == "name"):
                    name = line1[i].split('=')[1].split("\'")[1]
                elif(line1[i].split("=")[0] == "drel" or line1[i].split("=")[0] == "dmrel"):
                    drel = 1
                    relation = line1[i].split("=")[1].split("\'")[1].split(":")[0]
                    relative = line1[i].split("=")[1].split("\'")[1].split(":")[1]

            print("H" + " " + head_tag + " ",end = " ")        

            if(name != 0):
                print(name + " ",end=" ")
            else:
                print("NULL ",end=" ")

            if(drel != 0):
                print(relation + " " + relative)
            else:
                print("NULL ROOT")
        else:
            troot = line1[1]
            troot_tag = line1[2]
            troot_lemma = line1[4].split("=")[1].split("\'")[1].split(",")[0]
            print("T " + troot + " " + troot_tag + " " + troot_lemma)
            head_const_tags = head_const_tags + " " + troot_tag
