from database import weapons as w


jogadores_database = { 
1: {
    'nome': 'kauã', 'classe': 'player', 'level': 1, 'xp': 0, 
    'status': {
        'hp': 100, 'mana': 100, 'dano': 25.5,},
    'status_base': {
        'hp': 90, 'mana': 97, 'dano': 4
    },
    'arma': {'classe': 'espadas', 'id': 1},
    'critic_chance': 5, 'critic_x': 1.5, 
    'multiplicators': {
        'hp': 10, 'mana': 10, 'dano': 8.5
    }, 
    'ataques': {
    1: {'nome': 'corte', 'dano': 20}, 2: {'nome': 'chute', 'dano': 12}, 3: {'nome': 'empurrão', 'dano': 7}}
    }
}

