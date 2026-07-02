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


jogador = en.create_entity(p.jogadores_database, 1)
while True:

    #print(jogador)
    monstro = en.create_entity(m.monstros_database, randint(1, len(m.monstros_database)))
    statusj = en.refresh_entity(jogador, jogador['status']['hp'], True)
    statusm = en.refresh_entity(monstro, None, True)
    #st.linc(statusj, 50)
    #st.linc(statusm, 50)
    print(f'Seu inimigo é um {monstro['nome']}!!')

    while True:

        print(st.colors(f'sua vida é: {jogador['status']['hp']:.0f}', 6))
        print(st.colors(f'a vida do {monstro['nome']} é: {monstro['status']['hp']:.0f}', 3))
        escolha_monstro = randint(1,2)
        st.linc('MENU DE ATAQUES', 50)

        while True:

            escolha = st.validnum('[1] para corte\n[2] para empurrão\n[3] para chute\n')
            st.lin(50)
            if escolha not in (1,2,3):
                print('erro, digite apenas 1,2 ou 3')
            else:
                break

        combate = cb.atacar(jogador, escolha, monstro)
        cb.relatorio(combate)
        en.level_up(jogador)
        en.refresh_entity(jogador, jogador['status']['hp'])
        st.lin(50)
        fim = mn.fimdojogo(jogador['status']['hp'], monstro['status']['hp'])

        if fim in ('win', 'loose'):
            break

        print('Esperando o ataque do monstro.',end='', flush=True)
        st.pontos()
        print()
        combate = cb.atacar(monstro, escolha_monstro, jogador)
        cb.relatorio(combate)
        en.level_up(jogador)
        en.refresh_entity(jogador, jogador['status']['hp'])
        st.lin(50)
        sleep(3)
        fim = mn.fimdojogo(jogador['status']['hp'], monstro['status']['hp'])

        if fim in ('win', 'loose'):
            break

    if fim == 'loose':
        print(st.colors(f'sua vida é: {jogador['status']['hp']:.0f}', 6))
        print(st.colors(f'a vida do {monstro['nome']} é: {monstro['status']['hp']:.0f}', 3))
        print(st.colors('VC MORREU', 1))
        break

    elif fim == 'win':
        print(st.colors(f'sua vida é: {jogador['status']['hp']:.0f}', 6))
        print(st.colors(f'Vc derrotou um {monstro['nome']}!!'))
        cb.regain_hp(jogador, monstro)

        if st.validfim():
            print('encerrando o jogo.')
            st.pontos()
            break