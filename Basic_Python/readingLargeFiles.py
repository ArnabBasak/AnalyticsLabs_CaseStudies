#reading the text file
file = open('textfile.txt','r')
content = file.readlines()
#counting the number of lines
print('File content :',len(content),'These many lines')
#including the negative and positive word corpus
positive = []
negative = []
neg_file = open('negative-words.txt','r')
neg_file_content = neg_file.readlines()
for neg_elements in neg_file_content:
    neg_items = neg_elements.rstrip("\n\r")
    negative.append(neg_items)
pos_file = open('positive-words.txt','r')
pos_file_content = pos_file.readlines()
for pos_elements in pos_file_content:
    pos_items = pos_elements.rstrip("\n\r")
    positive.append(pos_items)

#statistical analysis of the word characters in the file
upper = 0
lower = 0
words = 0
characters = 0
for elements in content:
    if(elements.islower()):
        lower = lower + 1
    elif(elements.isupper()):
        upper = upper + 1
    wordslist=elements.split()
    words=words+len(wordslist)
    characters += sum(len(word) for word in wordslist)
print("There are: ",words,"In the file")
print("There are:",characters,"In the file")
print("Lower case letters in the file are:",lower)
print("Upper case letters in the file are:",upper)
print("space and special characters present in the file: ",((len(content))-lower+upper))
print("percentage of lowercase letters in the file are: ",(lower/(len(content)))*100)
print("percentage of uppercase letters in the file are: ",(upper/(len(content)))*100)
print("percentage of the space and special characters present in the file:",(((len(content))-lower+upper)/(len(content)))*100)
