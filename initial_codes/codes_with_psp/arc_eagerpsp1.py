import sys
import re
import copy
from collections import deque

sentence_id,line_number=0,0
not_parasble_sentences_ki,not_parasble_sentences,stack,dependencies,tags,line_state,buffer=[],[],[],[],[],[],[]

def check_orignal_dependencies():
	buffer_top = buffer[len(buffer) - 1]

	f=1
	stack_top = stack[len(stack) - 1]
	for i in range(len(tags)):
		if(tags[i][0] == stack_top and tags[i][1] == buffer_top):
			f=0
			return tags[i][2],tags[i][3]
	if f == 1:
		return 0,0;		


def check_left_arc():
	f=1
	stack_top = stack[len(stack) - 1]
	for i in range(len(dependencies)):
		if(dependencies[i][2] == stack_top):
			f=0
			return 0
	if f == 1:
		return 1	

def check_right_arc():
	f=1
	buffer_top = buffer[len(buffer) - 1]
	for i in range(len(dependencies)):
		if(dependencies[i][2] == buffer_top):
			f=0
			return 0
	if f == 1:
		return 1			

def check_reduce():
	f=1
    
	stack_top = stack[len(stack) - 1]

	for i in range(len(dependencies)):
		if(dependencies[i][2] == stack_top):
			f=0
			return 1
	if f==1:
		return 0


def left_arc(relation):
	indx =0 
	stack_top = stack[len(stack) - 1]
	buffer_top = buffer[len(buffer) - 1]

	temp = []
	indx = len(temp)
	temp.insert(indx,buffer_top)
	temp.insert(indx+1,relation)
	temp.insert(indx+2,stack_top)
	indx = len(dependencies)
	dependencies.insert(indx,temp)
	indx = len(stack)
	stack.pop(indx-1)

def right_arc(relation):
	indx = 0 
	stack_top = stack[len(stack) - 1]
	buffer_top = buffer[len(buffer) - 1]

	temp = []
	indx = len(temp)
	temp.insert(indx , stack_top)
	temp.insert(indx+1,relation)
	temp.insert(indx+2,buffer_top)
	indx = len(dependencies)
	dependencies.insert(indx , temp)
	indx = len(buffer)
	buffer.pop(indx-1)
	indx = len(stack)
	stack.insert(indx , buffer_top)

def reduce():

	stack.pop()

def shift():
	indx = 0
	buffer_top = buffer[len(buffer) - 1]
	indx = len(buffer)
	buffer.pop(indx-1)
	indx = len(stack)
	stack.insert(indx ,buffer_top)

def dependency_link():
	indx = 0
	buffer_top = buffer[len(buffer) - 1]
	f=1
	for i in range(len(stack)-2 , -1 , -1):
		stack_element = stack[i]
		for j in range(len(tags)):
			if(tags[j][0] == stack_element and tags[j][1] == buffer_top):
				f=0
				return 1
	if f==1:
		return 0			



def is_parsable():
	while((len(stack) != 1 or len(buffer) != 1)):

		print(stack[len(stack) - 1],end=" ")
		if(len(buffer) > 0):
			print(buffer[len(buffer) - 1])
		
		if(len(buffer) > 1):
			if(len(stack) > 0):
				orignal_dependency,relation = check_orignal_dependencies()

				if(orignal_dependency == 0):
					size = len(stack)
					if(size > 1):

						if(dependency_link() == 1):
							
							if(check_reduce() == 1):
								reduce()
								print("reduce")
							else:
								return 0	
						else:
							shift()
							print("shift")
					else:
						shift()
						print("shift")								


				elif(orignal_dependency == "L"):
					can_right_arc = check_right_arc()
					if(can_right_arc == True):
						right_arc(relation)
						print("right_arc")
					else:
						return 0

				elif(orignal_dependency == "R"):
					can_left_arc = check_left_arc()
					if(can_left_arc == True):
						left_arc(relation)
						print("left_arc")
					else:
						return 0

		elif(len(stack) > 1 and len(buffer) == 1):
			can_reduce = check_reduce()
			if(can_reduce==True):
				reduce()
				print("reduce")
			else:
				return 0

	if(stack[0] == "ROOT"  ):
		if( buffer[0] == "BLK"):
			return 1
	else:
		return 0															




f = open(sys.argv[1], "r")
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
		print(sentence_id)


	elif(pattern_head.match(line)):
		line_state = []
		indx = len(line_state)
		line1 = line.split(";")
		line_state.insert(indx,line1[0].split(' ')[5])
		line_state.insert(indx+1,line1[1].split(' ')[6])
		line_state.insert(indx+2,line1[2].split(' ')[1])
		line_state.insert(indx+3,line1[3].split(' ')[1])
		indx = len(tags)
		tags.insert(indx,line_state)

	elif(pattern_root.match(line)):
		line_state = []
		indx = len(line_state)
		line1 = line.split(";")
		line_state.insert(indx,"ROOT")
		line_state.insert(indx+1,line1[1].split(" ")[6])
		line_state.insert(indx+2,"L")
		line_state.insert(indx+3,"ROOT")
		indx = len(tags)
		tags.insert(indx,line_state)	

	elif(line_number == 8):
		buffer=[]
		line1=line.strip()
		indx = 0 
		line2 = line1.split(' ')
		for i in range(len(line2)):
			indx = len(buffer)   
			buffer.insert(indx , line2[i])
		buffer.reverse()


	elif(pattern_end.match(line)):
		initialiser='ROOT'
		indx = len(stack)
		stack.insert(indx , initialiser)


		flag = is_parsable()

		if(flag == 1):
			print("parsable")
			a = 1
		else:
			print("Not parsable")
			indx = len(not_parasble_sentences)
			not_parasble_sentences.insert(indx, sentence_id)
			count+=1


		print(dependencies)	

		flagki = 0	
		tags=[]
		stack=[]	
		buffer=[]
		dependencies=[]	

print(count)
print(not_parasble_sentences)
print(len(not_parasble_sentences))
