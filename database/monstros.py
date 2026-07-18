from database import weapons as w


monstros_database = {
1: {
    'nome': 'lobo', 'classe': 'monstro', 'level': 1, 'xp': 0,
    'status': {
        'hp': 100, 'mana': 0
    },
    'status_base': {
        'hp': 93, 'mana': 0, 'dano': 5
    },
    'status_max': {
        'hp': 100, 'mana': 0, 'dano': 25.5
    },
    'arma': {'classe': 'corporal', 'id': 1},
    'critic_chance': 6, 'critic_x': 1.50,
    'modifiers': {
        'level': {
            'hp': 7, 'mana': 0, 'dano': 5.5
        },
        'debuffs': {

        },
        'buffs': {

        },
    },
    'ataques': {
        1: {'id': 4},
        2: {'id': 5}
    }
},

2: {
    'nome': 'goblin', 'classe': 'monstro', 'level': 1, 'xp': 0,
    'status': {
        'hp': 125, 'mana': 0
    },
    'status_base': {
        'hp': 116.5, 'mana': 0, 'dano': 3
    },
    'status_max': {
        'hp': 125, 'mana': 0, 'dano': 17
    },
    'arma': {'classe': 'espadas', 'id': 2},
    'critic_chance': 5, 'critic_x': 1.30,
    'modifiers': {
        'level': {
            'hp': 8.5, 'mana': 0, 'dano': 4
        },
        'debuffs': {

        },
        'buffs': {

        },
    },
    'ataques': {
        1: {'id': 1},
        2: {'id': 2},
        3: {'id': 3}
    }
},

3: {
    'nome': 'orc', 'classe': 'monstro', 'level': 1, 'xp': 0,
    'status': {
        'hp': 150, 'mana': 0
    },
    'status_base': {
        'hp': 141, 'mana': 91, 'dano': 8
    },
    'status_max': {
        'hp': 150, 'mana': 100, 'dano': 33.5
    },
    'arma': {'classe': 'cutelos', 'id': 1},
    'critic_chance': 5, 'critic_x': 1.40,
    'modifiers': {
        'level': {
            'hp': 9, 'mana': 9, 'dano': 5.5
        },
        'debuffs': {

        },
        'buffs': {

        },
    },
    'ataques': {
        1: {'id': 1},
        2: {'id': 2},
        3: {'id': 6}
    }
}
}