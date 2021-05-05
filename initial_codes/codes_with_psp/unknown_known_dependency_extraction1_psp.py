import sys
import re

tags_pair,tags,unknown_dependencies_name,heads_name = [],[],[],[]
line_number,flag,word_data = 0,0,{}

def extract_unknown_dependencies():
	for dependency in range(len(tags)):
		if(tags[dependency][2] == "R"):
			head_index = heads_name.index(tags[dependency][1])
			dependent_index = heads_name.index(tags[dependency][0])
             
			if (head_index - dependent_index) > 3:
				cnt,pair1,pair2 = 0,[heads_name[dependent_index] , heads_name[head_index - 1]],[heads_name[dependent_index] , heads_name[dependent_index + 1]]
				if pair1 not in unknown_dependencies_name :
					if pair1 not in tags_pair:
						indx = len(unknown_dependencies_name) 
						unknown_dependencies_name.insert(indx,pair1)
						cnt += 1
				if pair2 not in unknown_dependencies_name :
					if pair2 not in tags_pair:
						unknown_dependencies_name.insert(len(unknown_dependencies_name),pair2)
						cnt += 1

				if(cnt < 2):
					for i in range(dependent_index + 2,head_index - 1,1):
						pair = [heads_name[dependent_index] , heads_name[i]]
						indx=0
						if pair not in unknown_dependencies_name and pair not in tags_pair:
							indx = len(unknown_dependencies_name)
							unknown_dependencies_name.insert(indx,pair)
							cnt += 1
						if(cnt == 2):
							break		

			elif (head_index ) > 1+dependent_index:
				pair1,indx = [heads_name[dependent_index],heads_name[dependent_index + 1]],0
				
				if pair1 not in unknown_dependencies_name and pair1 not in tags_pair:
    				

					indx = len(unknown_dependencies_name)
					unknown_dependencies_name.insert(len(unknown_dependencies_name),pair1)
				elif (head_index ) > 2+dependent_index:	
					pair,indx = [heads_name[dependent_index],heads_name[dependent_index + 2]],0
					if pair not in unknown_dependencies_name and pair not in tags_pair:
						indx= len(unknown_dependencies_name)
						unknown_dependencies_name.insert(indx,pair)

		elif(tags[dependency][2] == "L"):
			if(tags[dependency][0] != "ROOT" and tags[dependency][1] != "BLK"):
				dependent_index,head_index = heads_name.index(tags[dependency][1]),heads_name.index(tags[dependency][0])
				if (dependent_index ) > 3+head_index:
					cnt,pair2,pair1 =0,[heads_name[dependent_index - 1] , heads_name[dependent_index]] , [heads_name[head_index + 1] , heads_name[dependent_index]]
					if pair1 not in unknown_dependencies_name and pair1 not in tags_pair:
						indx = len(unknown_dependencies_name)
						unknown_dependencies_name.insert(indx,pair1)
						cnt += 1
					if pair2 not in unknown_dependencies_name and pair2 not in tags_pair:
						indx = len(unknown_dependencies_name)
						unknown_dependencies_name.insert(indx,pair2)
						cnt += 1

					if(2>cnt):
						for i in range(dependent_index - 2,head_index + 1,-1):
							pair,indx = [heads_name[i] , heads_name[dependent_index]],0
							if pair not in unknown_dependencies_name and pair not in tags_pair:
								indx = len(unknown_dependencies_name)
								unknown_dependencies_name.insert(indx ,pair)
								cnt += 1
							if(cnt == 2):
								break

				elif (head_index ) > 1+dependent_index:
					pair1,indx = [heads_name[dependent_index - 1] , heads_name[dependent_index]],0
					
					if pair1 not in unknown_dependencies_name and pair1 not in tags_pair:
						indx = len(unknown_dependencies_name)
						unknown_dependencies_name.insert(indx,pair1)
					elif (head_index ) > 2+dependent_index:
						pair,insx = [heads_name[dependent_index-2] , heads_name[dependent_index]],0
						if pair not in unknown_dependencies_name and pair not in tags_pair:
							indx = len(unknown_dependencies_name)
							unknown_dependencies_name.insert(indx,pair)

			else:
				dependent_index,cnt = heads_name.index(tags[dependency][1]),0
				for i in range(dependent_index-1 , -1 , -1):
    			
					indx,pair = 0,[heads_name[i], heads_name[dependent_index]]
					if(pair not in unknown_dependencies_name and pair not in tags_pair):
						indx = len(unknown_dependencies_name)
						unknown_dependencies_name.insert(indx,pair)
						cnt += 1
					if(cnt == 2):
						break
				cnt = 0
				for i in range(0 , dependent_index-1,1):
					pair,indx = [heads_name[i], heads_name[dependent_index]],0
					if(pair not in unknown_dependencies_name and pair not in tags_pair):
						indx = len(unknown_dependencies_name)
						unknown_dependencies_name.insert(indx,pair)
						cnt += 1
					if(cnt == 2):
						break

				if(tags[dependency][0] != "ROOT"):
					cnt,dependent_index = 0,heads_name.index(tags[dependency][1])
					for i in range(dependent_index-1 , -1 , -1):
						pair = ["ROOT",heads_name[i]]
						if(pair not in unknown_dependencies_name and pair not in tags_pair):
							indx = len(unknown_dependencies_name)
							unknown_dependencies_name.insert(indx,pair)
							cnt += 1
						if(cnt == 2):
							break
					cnt = 0
					for i in range(0 , dependent_index-1,1):
						pair = ["ROOT",heads_name[i]]
						if(pair not in unknown_dependencies_name and pair not in tags_pair):
							indx = len(unknown_dependencies_name)
							unknown_dependencies_name.insert(indx,pair)
							cnt += 1
						if(cnt == 2):
							break 

def print_unknown_dependencies():
	for dependency in range(len(unknown_dependencies_name)):
		print(word_data[unknown_dependencies_name[dependency][0]].strip(),end = " ",)
		print(' ; ',end = " ")
		print(word_data[unknown_dependencies_name[dependency][1]].strip(),end = " ")
		print(' ; ',end = " ")
		print('U ; ',end = " ")
		print('NULL')


f= open(sys.argv[1], "r") 
count = 0
for line in f:
    line_number += 1
    line = re.sub("\s+"," ",line)

    pattern_start=re.compile('<S+')
    pattern_end=re.compile('</S+')
    pattern_head=re.compile('H+')
    pattern_root=re.compile('ROOT+')

    if(pattern_start.match(line)):
        line_number = 0
        sentence_id = line.split("'")[1]
        

    elif(pattern_end.match(line)):
        extract_unknown_dependencies()
        print_unknown_dependencies()
        tags_pair,tags,unknown_dependencies_name,heads_name=[],[],[],[]
        word_data.clear()
        

    elif(line_number == 8):
        heads_name=[]
        line1=line.strip()
        line2 = line1.split(" ")
        for i in range(len(line2)):   
            indx = len(heads_name)
            heads_name.insert(indx,line2[i])

    elif(pattern_head.match(line)):
        print(line)
        line_state_pairs,line_state = [],[]
        
        line1 = line.split(";")
        indx = len(line_state)
        line_state.insert(indx,line1[0].split(" ")[5])
        indx=len(line_state_pairs)
        line_state_pairs.insert(indx,line1[0].split(" ")[5])
        indx = len(line_state)
        line_state.insert(indx,line1[1].split(" ")[6])
        indx = len(line_state_pairs)
        line_state_pairs.insert(indx,line1[1].split(" ")[6])
        indx = len(line_state)
        line_state.insert(indx ,line1[2].split(" ")[1])
        indx = len(tags)
        tags.insert(indx ,line_state) 
        indx = len(tags_pair)
        tags_pair.insert(indx,line_state_pairs)


        if(line_state[0] not in word_data):
            word_data[line_state[0]] = line1[0]
        if(line_state[1] not in word_data):
            word_data[line_state[1]] = line1[1]	

    elif(pattern_root.match(line)):
        print(line)
        line_state_pairs,line_state = [],[]
        line1 = line.split(";")
        indx = len(line_state)
        line_state.insert(indx,"ROOT")
        indx = len(line_state_pairs)
        line_state_pairs.insert(indx,"ROOT")
        indx = len(line_state)
        line_state.insert(indx,line1[1].split(" ")[6])
        indx = len(line_state_pairs)
        line_state_pairs.insert(indx,line1[1].split(" ")[6])
        indx = len(line_state)
        line_state.insert(indx,"L")
        indx = len(tags)
        tags.insert(indx,line_state)
        indx = len(tags_pair)
        tags_pair.insert(indx,line_state_pairs)
		
		
		
		
        if(line_state[0] not in word_data):
            word_data[line_state[0]] = line1[0]	
        if(line_state[1] not in word_data):
            word_data[line_state[1]] = line1[1]	
