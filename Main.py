import meta,opwords,random

def make_mistake(word):
    word = word.upper()
    code = opwords.getsound(word)
    opwords.init(word,code)

    rand = random.randrange(1,5,1)
    ans = []
    rand=3
    print(rand)
    if rand  ==  1 and len(word)<10:
        ans = opwords.generate("",0)
        index = random.randrange(max(len(ans)-5,0),len(ans),1)
        ans.sort()
        ans = ans[index][1]
    if rand  ==  2 or ans  ==  []:
        ans = opwords.jumblewords(word)
    if rand  ==  3 or ans  ==  []:
        ans = opwords.make2cons1(word)
    if rand  ==  4 or ans  ==  []:
        ans = opwords.repeatletter(word)
    return ans

def removeallpunct(word):
    final = ""
    for i in word:
        if opwords.is_punctuation(i)  ==  False:
            final+= i
    return final

def main():
    opwords.loadwords("sorted_words.txt")
    print("Enter the Document")
    text = list(map(str,input().split()))
    
    final = ""
    mod = random.randrange(1,len(text)+1,1)
    print(mod)
    index = 0
    lastchar = ''
    for word in text:
        index+= 1
        if index%mod  ==  0:
            pi = random.randrange(1,3,1)
            if pi%2  ==  0:
                word = removeallpunct(word)
            word = make_mistake(word).lower()
            print(word)
            if lastchar  ==  '.' or index  ==  1:
                tmp = ''
                if(len(word)>1):
                    tmp = word[1:len(word)]
                word  =  word[0].capitalize()+tmp
            final +=  word
        else:
            final +=  word
        lastchar = word[len(word)-1]
        final +=  ' '
 
    print(final)

if __name__  ==   "__main__":
  main()