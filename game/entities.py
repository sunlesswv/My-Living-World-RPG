from copy import deepcopy
from utils import strings as st
from game import combat as cb
from game import effects as ef
from database import weapons as w
from database import skills as s

def create_entity(banco, id = 1):
    entity = deepcopy(banco[id])
    entity['arma'] = deepcopy(w.weapons_database
    [entity['arma']['classe']]
    [entity['arma']['id']]
    )
    load_skills(entity)
    refresh_entity(entity)
    entity['status']['hp'] = entity['status_max']['hp']
    entity['status']['mana'] = entity['status_max']['mana']
    return entity

def level_up(entity, requerimento = 100):
    niveis = 0
    while True:
        reqxp = req_xp(entity, requerimento)
        if entity['xp'] >= reqxp:
            entity['xp'] -= reqxp
            entity['level'] += 1
            niveis += 1
            cb.regain_hp(entity)
        else:
            if entity['classe'] == 'player' and niveis > 0:
                if niveis == 1:
                    nivel_escrito = 'nivel'
                else:
                    nivel_escrito = 'niveis'

                print(st.colors(f'{entity['nome']} subiu {niveis} {nivel_escrito}', 2))
                print(f'nivel de {entity['nome']}: {entity['level']}')
                print(f'xp de {entity['nome']}: {entity['xp']}')
            break

def req_xp(entity, requerimento = 100):
    return entity['level'] * requerimento

def level_up_forced(entity, level = 1):
    entity['level'] += level

def load_weapon(entity, dano=False):
    arma = deepcopy(w.weapons_database
    [entity['arma']['classe']]
    [entity['arma']['id']]
    )
    if dano:
        return arma['dano']
    else:
        entity['arma'] = arma


def unload_weapon(entity):
    entity['arma'] = {'classe': entity['arma']['classe'], 
    'id': entity['arma']['id']}


def load_skills(entity):
    for key, skill in entity['ataques'].items():
        entity['ataques'][key] = deepcopy(s.skills_database
        [skill['id']])


def unload_skills(entity):
    for k, skill in entity['ataques'].items():
        entity['ataques'][k] = {
            'id': skill['id']}


def cooldown_decrease(entity, ataque = 'sem_ataque'):
    skills = entity['ataques']
    if ataque != 'sem_ataque':
        skills[ataque]['cooldown'] = skills[ataque]['cooldown_base'] 

    for k in skills.keys():
        if skills[k]['cooldown'] > 0 and k != ataque:
            skills[k]['cooldown'] -= 1


def refresh_entity(entity, relatorio = False):
    level_up(entity)
    for k in entity['status_max']:
        entity['status_max'][k] = entity['status_base'][k] + (entity['level'] * entity['modifiers']['level'][k])
    if entity['modifiers']['debuffs']:
        for name, debuff in entity['modifiers']['debuffs'].items():
            if debuff['classe'] == 'status':
                ef.aplicar_modificadores(entity, 'debuffs', name)

    entity['status']['hp'] = min(entity['status']['hp'], entity['status_max']['hp'])
    weapon_damage = load_weapon(entity, True)
    entity['status_max']['dano'] += weapon_damage

    if relatorio:
        show_damage(entity)

        
def show_damage(entity):
    name = entity['nome']
    total =  entity['status_max']['dano']
    base = entity['status_base']['dano']
    espada = load_weapon(entity, True)
    bonus_nivel = entity['modifiers']['level']['dano']
    bonus_nivel_total = entity['level'] * entity['modifiers']['level']['dano']
    return f'''Nome da entidade: {name}
Dano total: {total}
Dano da espada: {espada}
Dano base: {base}
Dano ganho por nivel: {bonus_nivel}
Dano ganho por estar nivel {entity['level']}: {bonus_nivel_total:.1f}'''
