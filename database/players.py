from database import weapons as w


jogadores_database = { 
1: {
    'nome': 'jogador', 'classe': 'player', 'level': 1, 'xp': 0, 
    'status': {
        'hp': 100, 'mana': 100},
    'status_base': {
        'hp': 90, 'mana': 97, 'dano': 4
    },
    'status_max': {
        'hp': 100, 'mana': 100, 'dano': 22.5
    },
    'arma': {'classe': 'espadas', 'id': 1},
    'critic_chance': 5, 'critic_x': 1.5,
    'modifiers': {
    'level': {
        'hp': 10, 'mana': 10, 'dano': 5.5
    },
    'debuffs': {

    },
    'buffs': {

    },
    },
    'ataques': {
    1: {'id': 1}, 2: {'id': 2}, 3: {'id': 3}}
    }
}

