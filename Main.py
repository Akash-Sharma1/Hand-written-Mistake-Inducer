import random
import opwords

def make_mistake(word):
    word = word.upper()
    code = opwords.getsound(word)
    opwords.init(word,code)
    
    word = opwords.removepunct(word)
    word=opwords.changedigits(word)
    
    rand = random.randrange(1,5,1)
    ans = []
    if rand  ==  1 and len(word)<=6 and opwords.alldigits(word)==False:
        ans = opwords.generate("",0)
        if len(ans) > 0:
            index = random.randrange(max(len(ans)-5,0),len(ans),1)
            ans.sort()
            ans = ans[index][1]
    if rand  ==  2 or ans  ==  []:
        ans = opwords.make2cons1(word)
    if rand  ==  3 or ans  ==  []:
        ans = opwords.jumblewords(word)
    if rand  ==  4 or ans  ==  []:
        ans = opwords.repeatletter(word)
    return ans


def main():
    opwords.loadwords("sorted_words.txt")
    print("Enter Sentence")
    text = list(map(str,input().split()))
    if(len(text)==0):
        return
    final = ""
    mod = 0
    if(len(text)==1):
        mod = 1
    else:
        mod=random.randrange(2,len(text)+1,1)
    index = 0
    lastchar = ''
    for word in text:
        index += 1
        if index%mod  ==  0:
            word = make_mistake(word).lower()
            if lastchar  ==  '.' or index  ==  1:
                tmp = ''
                if(len(word)>1):
                    tmp = word[1:len(word)]
                word  =  word[0].capitalize()+tmp
            final +=  word
        else:
            final +=  word
        if len(word)>0:
            lastchar = word[len(word)-1]
        final +=  ' '
    print(final)

if __name__  ==   "__main__":
  main()