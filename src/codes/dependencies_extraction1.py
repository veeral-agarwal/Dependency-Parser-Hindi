import sys
import re
count = 0

dependencies = []
new_dependencies = []

f = open(sys.argv[1], 'r')
for line in f:

    if (line.rstrip()):
        line = re.sub("\s+", " ", line)
        line1 = line.split(" ")

        if (line1[0] == "<Sentence"):

            count += 1
            print("<Sentence id=" + '\'' + str(count) + '\'>')

        elif(line1[0].strip() == "</Sentence>"):
            for t in range(0,len(dependencies)):
                temp = []
                if (dependencies[t][7] != "ROOT"):
                    for j in range(0,len(dependencies)):
                        check = dependencies[j][5]
                        if (dependencies[t][7] == check):

                            if(t < j):
                                for k in range(0,len(dependencies[t])):
                                    indx = len(temp)
                                    temp.insert(indx,dependencies[t][k])

                                temp.append(";")

                                for k in range(len(dependencies[j])):
                                    indx = len(temp)
                                    temp.insert(indx ,dependencies[j][k])

                                temp.append(";")

                                temp.append("R")

                            elif(j < t):
                                for k in range(len(dependencies[j])):
                                    indx = len(temp)
                                    temp.insert(indx ,dependencies[j][k])

                                temp.append(";")

                                for k in range(len(dependencies[t])):
                                    indx = len(temp)
                                    temp.insert(indx , dependencies[t][k])

                                temp.append(";")

                                temp.append("L")

                            temp.append(";")
                            temp.append(dependencies[t][6])

                            break

                else:
                    temp.append("ROOT")
                    temp.append(";")
                    for k in range(len(dependencies[t])):
                        temp.append(dependencies[t][k])
                    indx = len(temp)
                    temp.insert(indx,";")
                    temp.insert(indx+1,"L")
                    temp.insert(indx+2,";")
                    temp.insert(indx+3,"ROOT")

                new_dependencies.append(temp)
            for t in range(len(new_dependencies)):
                for j in new_dependencies[t]:
                    print(j + " ", end=" ")
                print()
            dependencies.clear()
            new_dependencies.clear()

            print(line1[0].strip())

        elif(line1[0] == "H"):
            indx = len(dependencies)
            dependencies.insert(indx , line1)

        else:
            print(line)