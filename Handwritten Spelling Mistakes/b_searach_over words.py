global lines

def infile(word):
    global lines    
    l=0
    r=370103-1
    while(l<=r):
        mid=int((l+r)/2)
        print(lines[mid])
        if lines[mid].strip()==word:
            return True
        elif lines[mid]<word:
            l=mid+1
        else:
            r=mid-1
    return False
def main():
    print("enter n: ")
    n=int(input())
    fo = open("sorted_words.txt", "r")
    global lines
    lines = fo.readlines()
    while(n>0):
        n=n-1
        print("Enter The Word to be Searched: ")
        word = input()
        print(infile(word))
    

if __name__== "__main__":
  main()