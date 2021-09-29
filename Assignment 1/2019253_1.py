''' Meetakshi Setiya, 2019253
'''

import random

map1 = {'a':'@', 'b':'ß', 'c':'<', 'd':'d', 'e':'£', 'f':'f', 'g':'[', 'h':'#', 'i':'!', 'j':'}', 'k':'<', 'l':'|', 'm':'m', 'n':'^', 'o':'ø', 'p':'P', 'q':'Q', 'r':'R', 's':'$', 't':'+', 'u':'u', 'v':'^', 'w':'W', 'x':'%', 'y':'?', 'z':'/', '1':'|', '2':'~', '3':'E', '4':'^', '5':'s', '6':'c', '7':'Z', '8':'%', '9':'N', '@':'a', '!':'i', '#':'H', '$':'S', '&':'6', '*':'+', '(':'C', ')':'>', '?':'q', '<':'{', '>':'}', '-':'T', '_':'U', '%':'P', '^':'A', '+':'X', '=':'F', '{':'[', '}':']', '|':'l', ':':'3', ';':'g','.':'o', ',':'y'}
map2 = {'a':'4', 'b':'8', 'c':'[', 'd':'D', 'e':'3', 'f':'7', 'g':'6', 'h':'#', 'i':'1', 'j':'9', 'k':'K', 'l':'l', 'm':'M', 'n':'n', 'o':'0', 'p':'p', 'q':'9', 'r':'r', 's':'2', 't':'7', 'u':'U', 'v':'v', 'w':'w', 'x':'*', 'y':'Y', 'z':'5', '1':'|', '2':'~', '3':'E', '4':'^', '5':'s', '6':'c', '7':'Z', '8':'%', '9':'N', '@':'a', '!':'i', '#':'H', '$':'S', '&':'6', '*':'+', '(':'C', ')':'>', '?':'q', '<':'{', '>':'}', '-':'T', '_':'U', '%':'P', '^':'A', '+':'X', '=':'F', '{':'[', '}':']', '|':'l', ':':'3', ';':'g','.':'o', ',':'y'}

def password(plaintext):
    ''' 
    Input: plain english text
    Substitutes random characters from the input string as per a randomly selected mapping.
    Return: a password string
    '''
    #1: map1, 2: map2, 3: toggle case, 4: keep original character
    transtext = []
    for chr in plaintext:
        rand = random.randint(1,4)
        if(chr in map1):
            if rand==1:
                transtext.append(map1[chr])
            elif rand==2:
                transtext.append(map2[chr])
            elif rand==3:
                transtext.append(chr.swapcase())
            elif rand==4:
                transtext.append(chr)
    return ''.join(str(i) for i in transtext)

def main():
    plaintext = input("Enter plain text: ")
    print(password(plaintext.lower()))

main()