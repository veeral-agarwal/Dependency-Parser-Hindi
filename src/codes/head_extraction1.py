import re
import sys
count = 0

head_list = {
    "JJP": ["JJ"],
    "JJP1": ["QF","QC","QO"],
    "VG*": ["VM"],
    "NEGP": ["NEG"],
    "RBP": ["RB"],
    "RBP1": ["NN","WQ"],
    "BLK": ["SYM"],
    "BLK1": ["UNK","RP","INJ"],
    "CCP": ["CC"],
    "CCP1": ["SYM"],
    "NP":["NN","PRP","NNP"],
    "NP1":["QC","QF","QO"],
    "NP2":["NST"],
    "NP3":["WQ"]
}

dependencies = []

head_relation,head_pos,head_name,head_relative_name,head_lemma,head_o_pos,head = "","","","","","",""
heads_o_pos,heads,sentence_pos,heads_lemma,heads_name,heads_pos,sentence_lemma,sentence = "","","","","","","",""


chunk_lemma,chunk_pos,chunk_words = [],[],[]

def find_head_jjp(head_o_pos):
    
    for i in range(len(chunk_pos)-1 , -1 , -1):
        for j in head_list['JJP']:
            if(chunk_pos[i] == j ):
                return i

    for i in range(len(chunk_pos)-1 , -1 , -1):
        for j in head_list['JJP1']:
            if(chunk_pos[i] == j):
                return i


def find_head_vg(head_o_pos):
    
    for i in range(len(chunk_pos)-1 , -1 , -1):
        for j in head_list['VG*']:
            if(chunk_pos[i] == j):
                return i

def find_head_negp(head_o_pos):

    for i in range(len(chunk_pos)-1 , -1 , -1):
        for j in head_list['NEGP']:
            if(chunk_pos[i] == j):
                return i


def find_head_rbp(head_o_pos):

    for i in range(len(chunk_pos)-1 , -1 , -1):
        for j in head_list['RBP']:
            if(chunk_pos[i] == j):
                return i    

    for i in range(len(chunk_pos)-1 , -1 , -1):
        for j in head_list['RBP1']:
            if(chunk_pos[i] == j):
                return i


def find_head_blk(head_o_pos):

    for i in range(len(chunk_pos)-1 , -1 , -1):
        for j in head_list['BLK']:
            if(chunk_pos[i] == j):
                return i

    for i in range(len(chunk_pos)-1 , -1 , -1):
        for j in head_list['BLK1']:
            if(chunk_pos[i] == j):
                return i


def find_head_ccp(head_o_pos):

    for i in range(len(chunk_pos)-1 , -1 , -1):
        for j in head_list['CCP']:
            if(chunk_pos[i] == j):
                return i

    for i in range(len(chunk_pos)-1 , -1 , -1):
        for j in head_list['CCP1']:
            if(chunk_pos[i] == j):
                return i


def find_head_np(head_o_pos):

    for i in range(len(chunk_pos)-1 , -1 , -1):
        for j in head_list['NP']:
            if(chunk_pos[i] == j):
                return i

    for i in range(len(chunk_pos)-1 , -1 , -1):
        for j in head_list['NP1']:
            if(chunk_pos[i] == j):
                return i

    for i in range(len(chunk_pos)-1 , -1 , -1):
        for j in head_list['NP2']:
            if(chunk_pos[i] == j):
                return i

    for i in range(len(chunk_pos)-1 , -1 , -1):
        for j in head_list['NP3']:
            if(chunk_pos[i] == j):
                return i


def find_head(head_o_pos):
    if(head_o_pos == "JJP"):return find_head_jjp(head_o_pos)
    if(head_o_pos == "VGF" or head_o_pos == "VGNN" or head_o_pos == "VGNF"):return find_head_vg(head_o_pos)
    if(head_o_pos == "NEGP"):return find_head_negp(head_o_pos)
    if(head_o_pos == "RBP"):return find_head_rbp(head_o_pos)
    if(head_o_pos =="BLK"):return find_head_blk(head_o_pos)
    if(head_o_pos == "CCP"):return find_head_ccp(head_o_pos)
    if(head_o_pos == "NP"):return find_head_np(head_o_pos)

f = open(sys.argv[1], 'r')
for line in f:
    # print(count)
    if (line.rstrip()):
        line = re.sub('\s+'," ",line)
        line1 = line.split(" ")

        if (line1[0] == "<Sentence"):

            count +=1
            print("<Sentence id=" + '\'' + str(count) + '\'>')

        elif(line1[0].strip() == "</Sentence>"):

            # index = find_head(head_o_pos)
            head = chunk_words[find_head(head_o_pos)]
            head_pos = chunk_pos[find_head(head_o_pos)]
            head_lemma = chunk_lemma[find_head(head_o_pos)]
            
            heads += head + " "
            heads_pos += head_pos + " "
            heads_o_pos += head_o_pos + " "
            heads_name += head_name + " "
            heads_lemma += head_lemma + " "

            indx = len(dependencies)
            fill = "H " + head + " " + head_lemma + " " +  head_o_pos + " " + head_pos + " " + head_name + " " + head_relation + " " +  head_relative_name
            dependencies.insert(indx,fill)

            print(sentence)
            print(sentence_lemma)
            print(sentence_pos)

            print(heads)
            print(heads_lemma)
            print(heads_o_pos)
            print(heads_pos)
            print(heads_name)

            for i in dependencies:
                print(i)

            chunk_words.clear()
            chunk_pos.clear()
            chunk_lemma.clear()
            heads_lemma,heads_o_pos,heads,sentence_lemma,heads_name,heads_pos,sentence_pos,sentence = '','','','','','','',''
            
            dependencies.clear()

            print(line1[0].strip())

        elif(line1[0] == 'H'):

            if(len(chunk_words)):
                # index = find_head(head_o_pos)
                head = chunk_words[find_head(head_o_pos)]
                head_pos = chunk_pos[find_head(head_o_pos)]
                head_lemma = chunk_lemma[find_head(head_o_pos)]

                heads += head + " "
                heads_pos += head_pos + " "
                heads_o_pos += head_o_pos + " "
                heads_name += head_name + " "
                heads_lemma += head_lemma + " "
                
                indx = len(dependencies)
                fill = "H " + head + " " + head_lemma + " " +  head_o_pos + " " + head_pos + " " + head_name + " " + head_relation + " " +  head_relative_name
                dependencies.insert(indx,fill)

            head_o_pos = line1[1]
            head_name = line1[2]
            head_relation = line1[3]
            head_relative_name = line1[4]

            chunk_words.clear()
            chunk_pos.clear()
            chunk_lemma.clear()

        elif(line1[0] == "T"):

            indx = len(chunk_words)
            chunk_words.insert(indx,line1[1])
            indx = len(chunk_pos)
            chunk_pos.insert(indx, line1[2])
            indx = len(chunk_lemma)
            chunk_lemma.insert(indx, line1[3])
            sentence += line1[1] + " "
            sentence_pos += line1[2] + " "
            sentence_lemma += line1[3] + " "
