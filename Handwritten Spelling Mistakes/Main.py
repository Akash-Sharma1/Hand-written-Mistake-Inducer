import meta,opwords,random

global homonyms

def getsound(word):
    if word!="-1":
        return meta.dmetaphone(word)[0]
    else:
        return ""

global dic
dic={
    'A':['','E','J','Y','H','U','W','AU','O','I','OA','AW','AI','A'],
    'B':['','P','D','E','B'],
    'C':['','X','K','CK','Q','QUE','S','SC','SE','TC','TCH','C'],
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
    'O':['','A','W','W','AU','E','OA','OW','OUGH','U','EW','OE','OW','UI','OO','O'],
    'P':['','F','B','P','PP'],
    'Q':['','K','QUE','Q'],
    'R':['','RR','RE','R'],
    'S':['','Z','X','SS','ZE','C','SC','SE','S'],
    'T':['','TE','TT','GHT','TCH','T'],
    'U':['','W','Y','I','EW','UE','O','U'],
    'V':['','WA','LV','V'],
    'W':['','R','H','O','OW','U','H','L','EU','OH','OE','W'],
    'X':['','K','C','EX','X'],
    'Y':['','I','IGH','U','AY','EWE','Y'],
    'Z':['','ZE','SE','S','X','Z']
}
global ans
global orig_word
global orig_code
ans=""

def Replace(word,pos):
    global orig_word
    global orig_code
    if pos==len(orig_word):
        global ans
        x=meta.jaro_winkler(orig_word,word,5,5)
        y=meta.jaro_winkler(orig_word,ans,5,5)
        if opwords.findin_trie(word)==True or (len(word)>0 and x>=.94 and orig_code==getsound(word) and orig_word!=word):
            print(word,meta.jaro_winkler(orig_word,word,5,5))
            if x>y:
                ans=word
            elif x==y and len(word)<len(ans):
                ans=word
            return 
        return 
    for i in dic[orig_word[pos]]:
        tmp=word+i
        a=Replace(tmp,pos+1)
    return

def make_mistake(word):
    global ans
    global orig_word
    global orig_code

    orig_word=word.upper()
    orig_code=getsound(orig_word)
    
    if meta.jaro_winkler(orig_word,ans,5,5)>=0.94:
        return ans

    Replace("",0)
    option=[ans]
    ans=[]
    ans=opwords.jumblewords(orig_word)
    for i in ans:
        option.append(i)
    option.append(opwords.make2cons1(orig_word))
    
    maxx=0
    ans=[]
    for i in option:
        xx=meta.jaro_winkler(orig_word,i,5,5)
        if i==option[0]:
            xx*=1.5
        if xx>maxx:
            ans.append((xx,i))
    ans.sort()
    #print(ans)
    rnd=random.randrange(max(0,len(ans)-2),len(ans),1)
    return ans[rnd][1]

def main():
    global homonyms
    homonyms=opwords.import_homonyms()
    opwords.make_trie(homonyms)
    
    print("Enter the Document")
    text = list(map(str,input().split()))
    if(text==["-1"]):
        while(True):
            word = input()
            word=word.upper()
            code=getsound(word)
            print(word,code)
    final=""
    for word in text:
        final+=make_mistake(word)
        final+=' '

    print(final)

if __name__== "__main__":
  main()