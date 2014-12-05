#Ed Lee, Lab 01

from string import lowercase

wlist = open('words.txt', 'r').read().split()
ustr = raw_input('Word :')
mylist = []
flag=False
k=0
while k<len(wlist):
        if wlist[k]==ustr:
                flag=True
                break
        k+=1

if flag == True:
        if len(ustr) == 6:
                for word in wlist:
                        count = 0
                        for x in range(6):
                                if ustr[x] == word[x]:
                                        count = count+1
                                if count == 5:
                                        mylist.append(word)
else:
        print 'Word entered is not 6 letters'  
  
print mylist
