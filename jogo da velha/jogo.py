from random import randint
posicoes = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
jogando = True
posicoes_ganhar = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
print('Começar jogo:')

def checar_vitorias(jogador):
    for i in posicoes_ganhar:
        pontos = 0
        for j in i:
            #print(j)
            if posicoes[j] == jogador:
                pontos+=1
            if pontos==3:
                print(f' {posicoes[0]} / {posicoes[1]} / {posicoes[2]} ')
                print(f' {posicoes[3]} / {posicoes[4]} / {posicoes[5]} ')
                print(f' {posicoes[6]} / {posicoes[7]} / {posicoes[8]} ')
                print(f'O jogador com a forma {jogador} ganhou!')
                global jogando
                jogando = False


while jogando == True:
    print(f' {posicoes[0]} / {posicoes[1]} / {posicoes[2]} ')
    print(f' {posicoes[3]} / {posicoes[4]} / {posicoes[5]} ')
    print(f' {posicoes[6]} / {posicoes[7]} / {posicoes[8]} ')
    lance_jogador = int(input('Diga a posição para colocar a peça: '))
    while posicoes[lance_jogador-1] != ' ':
        lance_jogador = int(input('Local inválido, diga outro: '))
    posicoes[lance_jogador-1] = 'X'

    checar_vitorias('X')
    if jogando == False:
        break

    lance_computador = randint(0,8)
    while posicoes[lance_computador] != ' ':
        if ' ' not in posicoes:
            print(f' {posicoes[0]} / {posicoes[1]} / {posicoes[2]} ')
            print(f' {posicoes[3]} / {posicoes[4]} / {posicoes[5]} ')
            print(f' {posicoes[6]} / {posicoes[7]} / {posicoes[8]} ')
            print('Deu velha!')
            jogando = False
            break
        lance_computador = randint(0,8)
    posicoes[lance_computador] = 'O'

    checar_vitorias('O')