from random import randint
from game import combat as cb
from copy import deepcopy
from game import entities as en
from utils import strings as st


def aplicar_sangramento(skill, entity):
    entity['modifiers']['debuffs']['sangramento'] = deepcopy(skill['efeitos']['sangramento'])
    aplicar_msg(entity, 'sangramento')

def processar_sangramento(entity):
    sangramento = entity['modifiers']['debuffs']['sangramento']
    dano = entity['status_max']['hp'] * (sangramento['dano_por_rodada'] /100)
    entity['status']['hp'] -= dano
    print(st.colors(f"{entity['nome']} sob efeito de sangramento, -{dano:.1f} de vida"))
    verif_duração(entity, 'sangramento')
    
def aplicar_atordoamento(skill, entity):
    entity['modifiers']['debuffs']['atordoamento'] = deepcopy(skill['efeitos']['atordoamento'])
    aplicar_msg(entity, 'atordoamento')

def processar_atordoamento(entity):
    print(f"{entity['nome']} sob efeito de atordoamento, ATAQUES INDISPONIVEIS")
    verif_duração(entity, 'atordoamento')

def aplicar_fraqueza(skill, entity):
    entity['modifiers']['debuffs']['fraqueza'] = deepcopy(skill['efeitos']['fraqueza'])
    aplicar_msg(entity, 'fraqueza')

def processar_fraqueza(entity):
    fraqueza = entity['modifiers']['debuffs']['fraqueza']
    print(f"{entity['nome']} sob efeito de fraqueza, vida e dano reduzidos em 10%")
    if not fraqueza['modificadores']: 
        fraqueza['modificadores'] = {
            'dano': entity['status_max']['dano'] * fraqueza['status_reduzido'],
            'hp': entity['status_max']['hp'] * fraqueza['status_reduzido']}
        aplicar_modificadores(entity, 'fraqueza')
    verif_duração(entity, 'fraqueza')    


aplicar_debuff = {
    'sangramento': aplicar_sangramento,
    'atordoamento': aplicar_atordoamento,
    'fraqueza': aplicar_fraqueza
}
processar_debuff = {
    'sangramento': processar_sangramento,
    'atordoamento': processar_atordoamento,
    'fraqueza': processar_fraqueza
}

def aplicar_debuffs(skill, entity):
    efeitos = []
    for name, effect in skill['efeitos'].items():
        if randint(1, 100) <= effect['chance']:
            efeitos.append(name)
            if name in aplicar_debuff:
                aplicar_debuff[name](skill, entity)
    
    return','.join(efeitos)

def processar_debuffs(entity):
    for debuff in list(entity['modifiers']['debuffs']):
        if debuff in processar_debuff:
            processar_debuff[debuff](entity)

#def aplicar_buffs(skill, entity):
#def processar_buffs(entity):

def aplicar_msg(entity, debuff):
    print(f"foi aplicado {debuff}, duração: {entity['modifiers']['debuffs'][debuff]['duração']}")

def verif_duração(entity, debuff):
    effect =  entity['modifiers']['debuffs'][debuff]
    
    effect['duração'] -= 1

    if effect['duração'] > 0:
        print(f"{effect['duração']} rounds restantes de duração")
        return True
    else:
        print(f"{debuff} terminou.")
        del entity['modifiers']['debuffs'][debuff]
        en.refresh_entity(entity)
        return False

def aplicar_modificadores(entity, category, effect):
    for name, modifier in entity['modifiers'][category][effect]['modificadores'].items():
        if category == 'debuffs':
            entity['status_max'][name] -= modifier
        elif category == 'buffs':
            entity['status_max'][name] += modifier

        
