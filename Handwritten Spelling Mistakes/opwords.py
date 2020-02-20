import random
import meta

def anyvowels(word):
    count=0
    for i in word:
        if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            count+=1
    return count
def isvowel(letter):
    return (letter=='A' or letter=='E' or letter=='I' or letter=='O' or letter=='U')

def repeatvowels(word):
    count=anyvowels(word)
    if count==0:
        return []
    variant=[]
    for i in range(len(word)):
        if ord(word[i])<65 or ord(word[i])>=97+26:
            continue
        if i+1==len(word) or word[i]!=word[i+1]:
            tmp=word[0:i]+word[i]+word[i]+word[i+1:len(word)]
            variant.append(tmp)
    return variant

def jumblewords(word):
    final=""
    variant=[]
    for i in range(len(word)):
        if ord(word[i])<65 or ord(word[i])>=97+26:
            continue
        if i+1<len(word) and (ord(word[i+1])<65 or ord(word[i+1])>=97+26):
            continue
        if i+1<len(word) and word[i]!=word[i+1]:
            tmp=word[0:i]+word[i+1]+word[i]+word[i+2:len(word)]
            variant.append(tmp)
    return variant

def make2cons1(word):
    final=""
    flag=1
    for i in range(0,len(word)-1):
        if flag==1 and word[i]==word[i+1]:
            flag=0
            continue
        final+word[i]
    return final

def import_homonyms():
    file1 = open('words_alpha.txt', 'r') 
    Lines = file1.readlines() 
    homophones=[]
    for line in Lines:
        line=line.strip()
        line=line.upper()
        homophones.append(line)
    return homophones

global root
global endvalues
def newnode():
    list=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,]
    return list

def insertin_trie(word):
    global root
    global endvalues
    pointer=0
    for i in range(len(word)):
        val=ord(word[i])-65
        if val<0 or val>=26:
            return
        if root[pointer][val]==-1:
            root.append(newnode())
            endvalues.append("-1")
            root[pointer][val]=len(root)-1
        pointer=root[pointer][val]
    endvalues[pointer]=word

def make_trie(arr):
    global root
    global endvalues
    root=[]
    endvalues=[]
    endvalues.append("-1")
    root.append(newnode())
    for data in arr:
        insertin_trie(data)
    # print(root)
    print(endvalues)

def findin_trie(word):
    global root
    global endvalues
    pointer=0
    for i in range(0,len(word)):
        if endvalues[pointer]!="-1":
            return False
        val=ord(word[i])-65
        if val<0 or val>=26:
            return False
        if root[pointer][val]==-1:
            return False
        pointer=root[pointer][val]

    if endvalues[pointer]!="-1":
        return False
    return True