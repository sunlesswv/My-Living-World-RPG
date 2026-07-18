from random import randint
from time import sleep
from copy import deepcopy
from utils import strings as st
from game import effects as ef
from random import choice
from game import entities as en


def calc_dano(entity, skill_choose):
    dano = entity['status_max']['dano']
    dano += entity['ataques'][skill_choose]['dano']
    if randint(1, 100) <= entity['critic_chance']:
        print(st.colors(f'ATAQUE CRITICO!! dano recebe mais {entity['critic_x']}x', 4))
        dano *= entity['critic_x']

    return dano

def atacar(atacker, escolha, enemy):
        ataque = atacker['ataques'][escolha]
        atacker['status']['mana'] -= ataque['mana']
        dano = calc_dano(atacker, escolha)
        efeitos = ef.aplicar_debuffs(ataque, enemy)
        enemy['status']['hp'] = max(0, enemy['status']['hp'] - dano)
        if enemy['status']['hp'] == 0:
            atacker['xp'] += enemy['level'] * 50

        return {
                'enemy': enemy['nome'],
                'atacker': atacker['nome'],
                'hp_enemy': enemy['status']['hp'],
                'dano': dano, 
                'ataque': ataque['nome'],
                'efeitos': efeitos
                }


def verif_ataque(entity):
            ataques = entity['ataques']
            for ataque in ataques.values():
                if ataque['cooldown'] == 0:
                    break
            else:        
                print('todos ataques em cooldown, passando a vez')
                return False
                
            debuffs = entity['modifiers']['debuffs']
            for debuff in debuffs.values():
                if debuff['classe'] == 'controle':
                    return False
            return True


def regain_hp(entity, target = None, heal = 0.5):
    hp_max = entity['status_max']['hp']
    if target is not None:
        hp_recover = target['status_max']['hp'] * heal
    else:
        hp_recover = hp_max * heal
    st.lin(50)
    print(st.colors(f'{entity['nome']} recuperou {hp_recover} de vida', 6))

    entity['status']['hp'] = min(entity['status']['hp'] + hp_recover, hp_max)

def verif_morte(entity):
    if entity['status']['hp'] <= 0:
         return True
    else:
         return False

def relatorio(combate):
        print(st.colors(f"{combate['atacker']} usou {combate['ataque']}", 6))
        print(st.colors(f"Foi causado {combate['dano']:.0f} de dano ao {combate['enemy']}", 1),)
        print(st.colors(f"Vida de {combate['enemy']}: {combate['hp_enemy']:.0f}", 3))

def verif_cooldown(skill):
     if skill['cooldown'] > 0:
          print(st.colors('essa skill esta em cooldown, tente outra'), 1)

def IA_monstro(enemy, entity):
            if not verif_ataque(enemy):
                return
            
            ataques_disponiveis = []    
            for key, atq in enemy['ataques'].items():
                if atq['mana'] <= enemy['status']['mana'] and atq['cooldown'] == 0:
                    ataques_disponiveis.append(key)
                    
            if ataques_disponiveis:
                escolha_monstro = choice(ataques_disponiveis)
                en.cooldown_decrease(enemy, escolha_monstro)
                combate = atacar(enemy, escolha_monstro, entity)
                relatorio(combate)
            else:
                en.cooldown_decrease(enemy, escolha_monstro)               