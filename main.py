import os
import api

choosen = api.getData()   # palavra escolhida
stay='s'    # permanecer no programa
gibbet=[]   # forca
attempt = 0 # tentativas
hangman = [
    ['  ',' ',''],
    [' ',' ',' '],
    ['  ',' ',''],
    [' ',' ',' '],
] # enforcado

# Coloca um "-" para c/ caractere
for term in choosen:
    gibbet.append('-')

# ----------------------------------
# Função que reseta o programa para uma nova partida
def reset():
    global data
    global choosen
    global gibbet
    global attempt
    global hangman
    choosen = api.getData()   # palavra escolhida
    gibbet=[]   # forca
    attempt = 0 # tentativas
    hangman = [
        ['  ',' ',''],
        [' ',' ',' '],
        ['  ',' ',''],
        [' ',' ',' '],
    ] # enforcado
    # Coloca um "-" para c/ caractere
    for term in choosen:
        gibbet.append('-')

# ----------------------------------
# Cria a forca e os dashs
def screen():
    global hangman
    # Limpa a tela se for no Win
    os.system('cls') or None
    print(' ________\n'+
         '|        |\n'+
         '|        '+hangman[0][1]+'\n'+
         '|       '+hangman[1][0]+hangman[1][1]+hangman[1][2]+'\n'
         '|        '+hangman[2][1]+'\n'+
         '|       '+hangman[3][0]+' '+hangman[3][2]+'\n'+
         '|'
    )
    # Como a Forca(gibbet) é uma lista para exibir é meio "méh", então ela é atribuida a uma var 
    #   e removido os caracteres indesejados e caso esteja se perguntando.. "Sim, é uma gambiarra!"
    dashs=str(gibbet)
    dashs = dashs.replace('[','')
    dashs = dashs.replace(']','')
    dashs = dashs.replace('\'','')
    dashs = dashs.replace(',','')
    print('\\'+dashs)
    
# Loop responsável por toda a execução do programa
while stay=='s' or stay=='S':
    # Se não tiver nenhum '-' quer dizer que a palavra está completa
    if '-' not in gibbet:
        print("\nSalvou o Jequetibas, boa!\n")
        stay=input('Deseja jogar novamente?[s/n]: ')
        reset()
    elif attempt==7:
        print("\nPalavra:"+str(choosen)+"\n\nNãããooo Jequetibas!\nCaixão Lacrado!\n")
        stay=input('Deseja jogar novamente?[s/n]: ')
        reset()
    else:
        # se faltar algum caractere ele monta a tela e solicita a letra
        screen()
        word=input('Digite uma letra:')
        
        # se a letra não se encontrar na palavra escolhida ele registra a tentativa e 
        #   adiciona uma parte do Jequitibas
        if word not in choosen:
            attempt=attempt+1
            if(attempt==1):
                hangman[0][1]='O'
            elif(attempt==2):
                hangman[1][0]='/'
            elif(attempt==3):
                hangman[1][1]='|'
            elif(attempt==4):
                hangman[1][2]='\\'
            elif(attempt==5):
                hangman[2][1]='|'
            elif(attempt==6):
                hangman[3][0]='/'
            elif(attempt==7):
                hangman[3][2]='\\'
        else:
            i=0 # para calcular a posição
            for term in choosen:
                # se algum termo for igual a letra digitada pelo usuário, ele altera o "dash" para a letra
                if term==word:
                    gibbet[i] = term
                i=i+1
            i=0