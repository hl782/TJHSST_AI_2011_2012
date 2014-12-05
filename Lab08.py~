#Lab08 - GHOST
from random import *
from math import *
from sys import *

class Node:
        def __init__(self, val):
                self.val = val
                self.children = []

def display (t, k):
        print '\t'*k, t.val
        for p in t.children:
                display(p, k+1)

def main():
        wlist = open('dictionary.txt', 'r').read().split()
        root = Node('*')
        for words in wlist:
                point = root
                size = 0
                for child in words:
                        size = size+1
                        x = 0
                        for nodes in point.children:
                                if nodes.val == child:
                                        x = 1
                                        point = nodes
                        if x == 0:
                                newNode = Node(child)
                                point.children.append(newNode)
                                point = newNode
                        if size == len(words):
                                newNode = Node('*')
                                point.children.append(newNode)
                                point = newNode
        point = root
        players = []
        n = input('# Of Players?')
        x = 1
        ghost = ['g','h','o','s','t']
        while (len(players)<n):
                temp = []
                temp1 = 0
                temp.append(x)
                temp.append(temp1)
                players.append(temp)
                x = x+1
                
        current = 0
        string = ''
        isWord = 0
        while(len(players)>1):
                print 'Current Word:' + string
                char = ''
                while len(char) != 1:
                        char = raw_input('What letter player ' + str((current + 1)) + '?')
                        if len(char) == 1:
                                string = string + char
                                if isWord == 0:
                                        isWord = 1
                                        for nodes in point.children:
                                                if nodes.val == char:
                                                        point = nodes
                                                        isWord = 0
                                print isWord

                        elif char == 'challenge':
                                correct = 0
                                if(isWord == 1):
                                        correct = 1
                                        if current > 0:
                                                players[current-1][1] = players[current-1][1]+1
                                                print ghost[players[current-1][1]-1]
                                        else:
                                                players[len(players)-1][1] = players[len(players)-1][1]+1
                                                print ghost[players[len(players)-1][1]-1]
                                elif(len(string)>3):
                                        for nodes in point.children:
                                                if nodes.val == '*':
                                                        correct = 1
                                                        if current >0:
                                                                players[current-1][1] = players[current-1][1]+1
                                                                print ghost[players[current-1][1]-1]
                                                        else:
                                                                players[len(players)-1][1] = players[len(players)-1][1]+1
                                                                print ghost[players[len(players)-1][1]-1]
                                if (correct == 0):
                                        print 'Your challenge is incorrect. You get a letter.'
                                        players[current][1] = players[current][1]+1
                                        print ghost[players[current][1]-1]
                                index = 0
                                remover = 0
                                for player in players:
                                        if player[1] >= 6:
                                                print 'Player ' + str(player[0]) + ' you lose. You are removed from the game.'
                                                remover = index
                                        index = index+1
                                if (remover >= 0):
                                        players.pop(remover)
                                isWord = 0
                                string = ''
                                point = root
                        elif char == 'hint':
                                temp = []
                                for nodes in point.children:
                                        temp.append(nodes.val)
                                print temp
                        elif char == 'exit':
                                print 'Good Bye'
                                sys.exit(0)
        
                current = current + 1
                if current >= len(players):
                        current = 0

main()
