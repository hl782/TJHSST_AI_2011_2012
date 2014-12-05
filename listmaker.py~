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

wlist = open('words.txt', 'r').read().split()
fout = open('nbrs.txt', 'w')
nbrlist = []
for word in wlist:
  fout.write(word + '\n')
  nbrlist = getNeighbors(word)
  for word1 in nbrlist:
    fout.write(word1 + ' ')
  fout.write('\n')
fout.close()
    