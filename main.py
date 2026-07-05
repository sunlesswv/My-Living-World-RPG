from utils import strings as st
from game import combat as cb
from game import entities as en
from game import menu as mn
from game import save as sv
from database import skills as s
from database import players as p
from database import monstros as m
from database import items as i
from database import weapons as w
from random import randint
from time import sleep
from copy import deepcopy

def load_player(player):
    return en.create_entity(player, 1)

def init_game(jogador):
    #print(jogador)
    enemy = en.create_entity(m.monstros_database, randint(1, 2))
    danoj = en.refresh_entity(jogador, True)
    danom = en.refresh_entity(enemy, True)
    #st.linc(danoj, 50)
    #st.linc(danom, 50)
    mn.perfil(jogador, True)
    sleep(2)
    print(f'Seu inimigo é um {enemy['nome']}!!')
    return enemy

def batalha(entity, enemy):
    while True:
        mn.perfil(entity, False)
        mn.perfil(enemy, False)

        mn.mostrar_ataques(entity)
        escolha = mn.escolha_ataques(entity)

        combate = cb.atacar(entity, escolha, enemy)
        cb.relatorio(combate)
        en.refresh_entity(entity)
        st.lin(50)

        if cb.verif_morte(enemy):
            return 'win'
        print('Esperando o ataque do monstro.',end='', flush=True)
        st.pontos()
        print()
        escolha_monstro = randint(1, len(enemy['ataques']))
        combate = cb.atacar(enemy, escolha_monstro, entity)
        cb.relatorio(combate)
        st.lin(50)
        if cb.verif_morte(entity):
            return 'lose'
        sleep(3)

def check_resultado(jogador, enemy, resultado):
    print(st.colors(f'a vida do {enemy['nome']} é: {enemy['status']['hp']:.0f}', 3))
    print(st.colors(f'sua vida é: {jogador['status']['hp']:.0f}', 6))

    if resultado == 'lose':
        print(st.colors('VC MORREU', 1)) 
        if st.validfim():
            print('encerrando o jogo.',end='')
            st.pontos()
            return 'end'
        else:
            print('Recomeçando.',end='')
            st.pontos()
            print()
            return 'restart'
        
    elif resultado == 'win':
        print(st.colors(f'Vc derrotou um {enemy['nome']}!!'))
        cb.regain_hp(jogador, enemy)
        mn.perfil(jogador)
        if st.validfim():
            print('encerrando o jogo.',end='')
            st.pontos()
            return 'end'
        
def game(database):
    fim = ''      
    while True:
        jogador = load_player(database)
        while True:
            monstro = init_game(jogador)

            resultado = batalha(jogador, monstro)

            fim = check_resultado(jogador, monstro, resultado)

            if fim in ('end', 'restart'):
                break
        if fim == 'end':
            break


jogador = p.jogadores_database
game(jogador)