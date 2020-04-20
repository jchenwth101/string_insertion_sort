#author: Joel Chenoweth
#Date 03-19-20
#Description:  A string sort insertion that lists a set of strings instead of numbers

def string_sort(a_list):
    """Sorts a string sort alphabetically using insertion sort
    without considering capital case parameter"""
    for index in range(1, len(a_list)):
      #  a_list.append(a_list[index].lower())
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos].lower() > value.lower():
            a_list[pos + 1] = a_list[pos].lower()
            pos -= 1
        a_list[pos + 1] = value

#a_list = ["Zebra", "apple", "marKer", "marble"]
#string_sort(a_list)
#print(a_list)










   # indexing_length = range(1, len(a_list))
    #f#or i in indexing_length:
       # value_to_sort =  a_list[i]
        #while a_list[i-1] > value_to_sort and i > 0:
           # a_list[i], a_list[i-1] = a_list[i-1], a_list[i]
            #i = i - 1
        #return a_list





    # lower case
   # for index in range(len(a_list)):
        #a_list.append(a_list[index].lower())
    #insertion sort
    #for i in a_list:
     #   pos = a_list.index(i)
      #  while pos > 0:
       #     if a_list[pos - 1] > a_list[pos]:
                #a_list[pos - 1], \
        #        a_list[pos] = a_list[pos - 1]
         #   else:
          #      break
           # pos = pos-1
       # print(a_list)




    #for index in range(1, len(a_list)):
       # a_list.append(a_list[index].lower())
        #value = a_list[index]
        #pos = index - 1
        #while pos >= 0 and a_list[pos].lower() > value.lower():
         #  a_list[pos + 1] = a_list[pos].lower()
          # pos -= 1
        #a_list[pos + 1] = value


        #for index in range(len(a_list)):
            #a_list.append(a_list[index].lower())
           #return a_list

#print("apple" < "zebra")

#a_list = ["Zebra", "apple", "marKer", "marble"]
#string_sort(a_list)
#print(a_list)









#after insertion sort sorted list
#for i in range(len(l2)):
 #   value = l2[i]
  #  for pos in range(len(l1)):
   #     if l1[pos].lower() == value.lower():
    #        print(l1[pos])






















#a_list = ["aardvark", "Baboon", "Zebra", "maRker", "marble", "Woodpecker"]
