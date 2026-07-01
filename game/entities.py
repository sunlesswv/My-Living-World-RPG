from copy import deepcopy
from utils import strings as st

def create_entity(banco, id = 1):
    return deepcopy(banco[id])


def level_up(entity, requerimento = 100):
    niveis = 0
    while True:
        req_xp = entity['level'] * requerimento
        if entity['xp'] >= req_xp:
            entity['xp'] -= req_xp
            entity['level'] += 1
            print(st.colors(f'{entity['nome']} subiu de nivel', 2))
            niveis += 1
        else:
            if entity['classe'] == 'player' and niveis > 0:
                print(st.colors(f'{entity['nome']} subiu {niveis}', 2))
                print(f'nivel de {entity['nome']}: {entity['level']}')
            break


def level_up_forced(entity, level = 1):
    entity['level'] += level

def max_life(entity):
    jogador = deepcopy(entity)
    jogador['status']['hp'] = jogador['status_base']['hp'] + (jogador['level'] * jogador['multiplicators']['hp'])
    return jogador['status']['hp']

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