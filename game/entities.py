from copy import deepcopy
from utils import strings as st
from game import combat as cb

def create_entity(banco, id = 1):
    return deepcopy(banco[id])


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
                print(st.colors(f'{entity['nome']} subiu {niveis}', 2))
                print(f'nivel de {entity['nome']}: {entity['level']}')
                print(f'xp de {entity['nome']}: {entity['xp']}')
            break

def req_xp(entity, requerimento = 100):
    return entity['level'] * requerimento

def level_up_forced(entity, level = 1):
    entity['level'] += level


def refresh_entity(entity, hp_in_game = None, relatorio = False):
    for k in entity['status']:
        entity['status'][k] = entity['status_base'][k] + (entity['level'] * entity['multiplicators'][k])
    if hp_in_game is not None:
        hp_perdido = entity['status']['hp'] - hp_in_game
        entity['status']['hp'] -= hp_perdido
    entity['status']['dano'] += entity['arma']['dano']
    name = entity['nome']
    total =  entity['status']['dano']
    espada = entity['arma']['dano']
    base = entity['status_base']['dano']
    bonus_nivel = entity['multiplicators']['dano']
    bonus_nivel_total = entity['level'] * entity['multiplicators']['dano']
    if relatorio:
        return f'''Nome da entidade: {name}
Dano total: {total}
Dano da espada: {espada}
Dano base: {base}
Dano ganho por nivel: {bonus_nivel}
Dano ganho por estar nivel {entity['level']}: {bonus_nivel_total:.1f}'''