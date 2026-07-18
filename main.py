from utils import strings as st
from game import combat as cb
from game import entities as en
from game import menu as mn
from game import save as sv
from game import effects as ef
from database import skills as s
from database import skills as s
from database import players as p
from database import monstros as m
from database import items as i
from database import weapons as w
from random import randint
from time import sleep
from copy import deepcopy
from pathlib import Path
import json


    

def init_game(jogador):
    enemy = en.create_entity(m.monstros_database, randint(1, 2))
    en.refresh_entity(jogador)
    en.refresh_entity(enemy)
    mn.perfil(jogador, True)
    sleep(2)
    print(f'Seu inimigo é um {enemy['nome']}!!')
    return enemy

def batalha(entity, enemy):
    mn.perfil(entity, True)
    while True:
        ef.processar_debuffs(entity)
        if cb.verif_morte(entity):
            return 'lose'
        mn.perfil(entity, False)
        mn.perfil(enemy, False)
                
        if cb.verif_ataque(entity):
            mn.mostrar_ataques(entity)
            escolha = mn.escolha_ataques(entity)
            en.cooldown_decrease(entity, escolha)
            combate = cb.atacar(entity, escolha, enemy)
            cb.relatorio(combate)
        else:
            en.cooldown_decrease(entity)


        en.refresh_entity(entity)
        st.lin(50)
        if cb.verif_morte(enemy):
            return 'win'
        ef.processar_debuffs(enemy)
        if cb.verif_morte(enemy):
            return 'win'
        print('Esperando o ataque do monstro.',end='', flush=True)
        st.pontos()
        print()

        cb.IA_monstro(enemy, entity) 
            
        st.lin(50)
        if cb.verif_morte(entity):
            return 'lose'
        sleep(3)

def check_resultado(jogador, enemy, resultado, nome_save):
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
        cb.regain_hp(jogador, enemy, 0.6)
        cb.regain_mana(jogador)
        sv.save(jogador, nome_save)
        mn.perfil(jogador)
        if st.validfim():
            print('encerrando o jogo.',end='')
            st.pontos()
            return 'end'
        
def game():
    fim = ''      
    while True:
        save = sv.choose_save()
        jogador = save[0]
        nome_save = save[1]
        while True:            
            monstro = init_game(jogador)

            resultado = batalha(jogador, monstro)

            fim = check_resultado(jogador, monstro, resultado, nome_save)

            if fim in ('end', 'restart'):
                break
        if fim == 'end':
            break


game()