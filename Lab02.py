#Ed Lee 09-08-11 Lab 02
#Find a ladder of each word
from string import lowercase
from sys import exit
import random
wlist = open('words.txt', 'r').read().split()
ustr = 'acorns'
current = 'acorns'
mylist = []
neighborlist = []
mylist.append(ustr)
def getNeighbors(word1):
        list1=[]
        for word in wlist:
                count = 0
                for x in range(6):
                        if word1[x] == word[x]:
                                count = count+1
                        if count == 5:
                                list1.append(word)
        if word1 in list1:
                list1.remove(word1)
        return list1
        
def isIn(word, list1):
        for x in range(0, len(list1)):
                if word == list1[x]:
                        return True
        return False
  
def difference(one, two):
        count = 0
        for x in range(6):
                if one[x] != two[x]:
                        count = count+1
        return count

print getNeighbors('acorns')
while difference(ustr, current) != 6:
        neighborlist = getNeighbors(current)
        temp = neighborlist[random.randint(0, len(neighborlist)-1)]
        while len(neighborlist) != 0:
                if temp not in mylist:
                        mylist.append(temp)
                        current = mylist[-1]
                        break
                else: #in my list
                        neighborlist.remove(temp)
                        if len(neighborlist) == 0:
                                print 'Dead End'
                                exit(0)
                temp = neighborlist[random.randint(0, len(neighborlist)-1)]
      
print mylist
  
  
