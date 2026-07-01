monstros_database = { 
1: {
    'nome': 'lobo', 'classe': 'monstro', 'level': 1, 'xp': 0, 
    'status': {
        'hp': 100, 'mana': 0, 'dano': 18}, 
    'status_base': {
        'hp': 97, 'mana': 0, 'dano': 5},
    'critic_chance': 5, 'critic_x': 1.25,
    'arma': {'nome': 'garras de lobo', 'id': 1, 'classe': 'sem_classe', 'dano': 10},
    'multiplicators': {
        'hp': 3, 'mana': 0, 'dano': 3
    }, 
    'ataques': { 
    1: {'nome': 'mordida', 'dano': 30}, 2: {'nome': 'arranhão', 'dano': 13}
    }},

2: {
    'nome': 'goblin', 'classe': 'monstro', 'level': 1, 'xp': 0,
    'status': {
        'hp': 125, 'mana': 0, 'dano': 33},
    'status_base': {
        'hp': 122, 'mana': 0, 'dano': 8},
    'arma': {
        'nome': 'espada velha de goblin', 'id': 2, 'classe': 'espada', 'dano': 20}, 
    'multiplicators': {
        'hp': 3, 'mana': 0, 'dano': 5},
    'critic_chance': 5, 'critic_x': 1.50,
    'ataques': { 
    1: {
        'nome': 'corte', 'dano': 30
    },
    2: {
        'nome': 'chute', 'dano': 15
     }}}}
