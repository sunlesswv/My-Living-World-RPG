from database import weapons as w


monstros_database = { 
1: {
    'nome': 'lobo', 'classe': 'monstro', 'level': 1, 'xp': 0, 
    'status': {
        'hp': 100, 'mana': 0, 'dano': 18}, 
    'status_base': {
        'hp': 97.5, 'mana': 0, 'dano': 5},
    'critic_chance': 6, 'critic_x': 1.50,
    'arma': {'classe': 'corporal', 'id': 1},
    'multiplicators': {
        'hp': 2.5, 'mana': 0, 'dano': 4
    }, 
    'ataques': { 
    1: {'nome': 'mordida', 'dano': 20}, 2: {'nome': 'arranhão', 'dano': 8}
    }},

2: {
    'nome': 'goblin', 'classe': 'monstro', 'level': 1, 'xp': 0,
    'status': {
        'hp': 125, 'mana': 0, 'dano': 33},
    'status_base': {
        'hp': 122, 'mana': 0, 'dano': 3},
    'arma': {'classe': 'espadas', 'id': 2}, 
    'multiplicators': {
        'hp': 3, 'mana': 0, 'dano': 3},
    'critic_chance': 5, 'critic_x': 1.30,
    'ataques': { 
    1: {
        'nome': 'corte', 'dano': 20
    },
    2: {
        'nome': 'chute', 'dano': 12
    },
    3: {'nome': 'empurrão', 'dano': 7
    }}},

 3: {
    'nome': 'orc', 'classe': 'monstro', 'level': 1, 'xp': 0,
    'status': {
        'hp': 150, 'mana': 0, 'dano': 33},
    'status_base': {
        'hp': 147, 'mana': 0, 'dano': 8},
    'arma': {'classe': 'cutelos', 'id': 1}, 
    'multiplicators': {
        'hp': 3.5, 'mana': 0, 'dano': 3.5},
    'critic_chance': 5, 'critic_x': 1.40,
    'ataques': { 
    1: {
        'nome': 'corte', 'dano': 20
    },
    2: {
        'nome': 'chute', 'dano': 12
    },
    3: {'nome': 'rugido de orc', 'dano': 16
    }}}} 
