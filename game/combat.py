from random import randint
from time import sleep
from copy import deepcopy
from utils import strings as st

def calc_dano(entity, skill):
    dano = entity['status']['dano']
    dano += entity['ataques'][skill]['dano']
    if randint(1, 100) <= entity['critic_chance']:
        print(st.colors(f'ATAQUE CRITICO!! dano recebe mais {entity['critic_x']}x', 4))
        dano *= entity['critic_x']

    return dano

def atacar(atacker, escolha, enemy):
        ataque = atacker['ataques'][escolha]
        dano = calc_dano(atacker, escolha)
        enemy['status']['hp'] = max(0, enemy['status']['hp'] - dano)
        if enemy['status']['hp'] == 0:
            atacker['xp'] += enemy['level'] * 50

        return {
                'enemy': enemy['nome'],
                'atacker': atacker['nome'],
                'hp_enemy': enemy['status']['hp'],
                'dano': dano, 
                'ataque': ataque['nome']
                }

def regain_hp(max_life, entity, hp = 50):
    if entity['status']['hp'] + hp > max_life:
        entity['status']['hp'] = max_life
    else:
        entity['status']['hp'] += hp
        print(st.colors(f'{entity['nome']} recuperou {hp} de vida', 6))       

def relatorio(combate):
        print(st.colors(f'{combate['atacker']} usou {combate['ataque']}', 6))
        print(st.colors(f'Foi causado {combate['dano']:.0f} de dano ao {combate['enemy']}', 1),)
        print(st.colors(f"Vida de {combate['enemy']}: {combate['hp_enemy']:.0f}", 3))