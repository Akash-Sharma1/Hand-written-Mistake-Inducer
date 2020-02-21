import random
import phonetics,jellyfish

def is_punctuation(letter):
    return (ord(letter) < 97 or ord(letter) >=  97+26) and ( ord(letter) < 65 or ord(letter) >= 65+26 ) and ( ord(letter) < 48 or ord(letter) >= 48+10 ) 

def isdigit(letter):
    return (ord(letter) >= 48 and ord(letter) <48+10)

def alldigits(word):
    for i in word:
        if isdigit(i)==False:
            return False
    return True 

def repeatletter(word):
    if(len(word)==0):
        return word
    count = 0
    rand = random.randrange(0,len(word),1)
    while( is_punctuation(word[rand]) == True or isdigit(word[rand]) == True ):
        rand = random.randrange(0,len(word),1)
        if count>len(word):
            return word
        count+=1
    word = word[0:rand]+word[rand]+word[rand]+word[rand+1:len(word)]
    return word

def jumblewords(word):
    if len(word)<= 2:
        return repeatletter(word)
    count = 0
    rand = random.randrange(1,len(word)-1,1)
    while( is_punctuation(word[rand]) == True or is_punctuation(word[rand+1]) == True or word[rand]==word[rand+1]):
        rand = random.randrange(0,len(word)-1,1)
        if count>len(word):
            return word
        count+=1

    word = word[0:rand]+word[rand+1]+word[rand]+word[rand+2:len(word)]
    return word

def make2cons1(word):
    final = ""
    flag = 1
    for i in range(0,len(word)):
        if flag == 1 and i+1 < len(word) and word[i] == word[i+1]:
            flag = 0
            continue
        final += word[i]
    if flag == 1:
        return jumblewords(word)
    return final

def changedigits(word):
    for i in range(len(word)):
        if (isdigit(word[i])):
            mod=random.randrange(1,len(word)+1,1)
            if (i+1)%mod == 0:
                rand=random.randrange(0,10,1)
                word=word[0:i-1]+str(rand)+word[i+1:len(word)]
                return word
    return word

def removepunct(word):
    if(len(word) == 0):
        return word
    for i in range(len(word)):
        if is_punctuation(word[i])  ==  True:
            mod=random.randrange(1,len(word)+1,1)
            if (i+1)%mod == 0:
                word=word[0:i]+word[i+1:len(word)]
                return word
    return word

global lines

def loadwords(path):
    global lines
    fo = open(path, "r")
    lines = fo.readlines()

def infile(word):
    word = word.lower()
    global lines
    l = 0
    r = 370103-1
    while(l<= r):
        mid = int((l+r)/2)
        if lines[mid].strip() == word:
            return True
        elif lines[mid]<word:
            l = mid+1
        else:
            r = mid-1
    return False

global dic
dic = {
    'A':['','E','J','Y','U','AU','O','I','OA','AW','AI','A'],
    'B':['','P','D','E','B'],
    'C':['','K','CK','Q','QUE','S','SC','SE','TC','TCH','C'],
    'D':['','B','P','ED','ET','T','D'],
    'E':['','IE','EI','I','A','EE','L','O','B','W','E'],
    'F':['','PH','B','UGH','F'],
    'G':['','HE','J','JE','GE','GH','GN','G'],
    'H':['','A','W','H'],
    'I':['','Y','E','IE','U','WI','I'],
    'J':['','GE','JE','G','J'],
    'K':['','Q','QUE','C','X','CK','K'],
    'L':['','W','E','U','LV','L'],
    'M':['','UM','AM','EM','MN','MB','M'],
    'N':['','NN','N'],
    'O':['','A','W','AU','E','OA','OW','OUGH','U','EW','OE','OW','UI','OO','O'],
    'P':['','F','B','P','PP'],
    'Q':['','K','QUE','Q'],
    'R':['','RR','RE','R'],
    'S':['','Z','X','SS','ZE','C','SC','SE','S'],
    'T':['','TE','TT','GHT','TCH','T'],
    'U':['','W','Y','I','EW','UE','O','U'],
    'V':['','WA','LV','V'],
    'W':['','H','O','OW','U','L','EU','OH','OE','W'],
    'X':['','K','C','EX','X'],
    'Y':['','I','IGH','U','AY','EWE','Y'],
    'Z':['','ZE','SE','S','X','Z']
}

global orig_word
global orig_code

def init(word,code):
    global orig_word
    global orig_code
    orig_word = word
    orig_code = code

def getsound(word):
    if word != "-1":
        return phonetics.dmetaphone(word)[0]
    else:
        return ""

def getchange(word_a,word_b):
    return jellyfish.jaro_winkler(word_a,word_b)

global ans
def generate(word , pos):
    global orig_word
    global orig_code
    global ans
    if pos == len( orig_word ):
        if len(word) == 0:
            ans = []
        x = getchange(orig_word , word)
        if orig_word !=  word and len(word) > 0 and orig_code == getsound(word):
            if x >=  .94:
                ans.append( (x,word) )
            elif x > .80 and infile(word) == True:
                ans.append((x*2,word))
        return ans

    if dic.get(orig_word[pos],'-1') == '-1':
        ans = generate(word , pos+1)
        ans = generate(word + orig_word[pos] , pos+1)
        return ans
    for i in dic[orig_word[pos]]:
        tmp = word+i
        ans = generate(tmp , pos+1)
    return ans

