import os
import random

words = ('abelha','lagartixa')
choosen = random.choice(words)
s=len(choosen)
stay='s'
spaces=[]
i=0
s=0
# Limpa a tela se for no Win
os.system('cls') or None

# Coloca um "-" para c/ caracter
for w in choosen:
    spaces.append('-')

while stay=='s':
    sp=str(spaces)
    sp = sp.replace('[','')
    sp = sp.replace(']','')
    sp = sp.replace('\'','')
    sp = sp.replace(',','')
    print(sp)
    word=input('Digite uma letra:')
    for l in choosen:
        if l==word:
            spaces[i] = l
        i=i+1
    i=0

    for w in spaces:
        
        if w=='-':
            s=0
            s=s+1
    

    if s==0:
        print("Parabens, voce ganhou!")
        stay=input("Deseja continuar? [s/n]")
        