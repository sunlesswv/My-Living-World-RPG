skills_database = { 
1: {
    'nome': 'corte', 'id': 1, 'tipo': 'arma', 'dano': 20, 'mana': 0, 'cooldown': 0,'cooldown_base': 2, 
    'efeitos': {
        'sangramento': {'tipo': 'debuff', 'classe': 'continuo', 'chance': 100, 'dano_por_rodada': 2, 'duração': 2, 'modificadores': {}}
    }
},

2: {
    'nome': 'chute', 'id': 2, 'tipo': 'corporal', 'dano': 12, 'mana': 0, 'cooldown': 0, 'cooldown_base': 1, 
    'efeitos': {
        'atordoamento': { 'tipo': 'debuff', 'classe': 'controle', 'chance': 100, 'duração': 2, 'modificadores': {}}
    }
},
3: {
    'nome': 'empurrão', 'id': 3, 'tipo': 'corporal', 'dano': 7, 'mana': 0, 'cooldown': 0, 'cooldown_base': 0, 
    'efeitos': {
        'atordoamento': { 'tipo': 'debuff', 'classe': 'controle', 'chance': 1, 'duração': 1, 'modificadores': {}}
    }
},
4: {
    'nome': 'mordida', 'id': 4, 'tipo': 'corporal', 'dano': 20, 'mana': 0, 'cooldown': 0, 'cooldown_base': 2, 
    'efeitos': {
        'sangramento': { 'tipo': 'debuff', 'classe': 'continuo', 'chance': 10, 'dano_por_rodada': 2, 'duração': 2,'modificadores': {}}
    }
},
5: {
    'nome': 'arranhão', 'id': 5, 'tipo': 'corporal', 'dano': 8, 'mana': 0, 'cooldown': 0, 'cooldown_base': 0, 
    'efeitos': {
        'sangramento': { 'tipo': 'debuff', 'classe': 'continuo', 'chance': 15, 'dano_por_rodada': 2, 'duração': 1, 'modificadores': {}}
    }
   
},
6: {
    'nome': 'rugido de orc', 'id': 6, 'tipo': 'corporal', 'dano': 25, 'mana': 30, 'cooldown': 0, 'cooldown_base': 6, 
    'efeitos': {
        'fraqueza': { 'tipo': 'debuff', 'classe': 'status', 'chance': 100, 'status_reduzido': 0.10, 'duração': 3, 'modificadores': {}}
}   
},
}