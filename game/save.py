import json
from database import players as p
from copy import deepcopy
from pathlib import Path
from game import entities as en

def load_save(arquivo = 'player1.json'):
        arquivo = Path("saves") / arquivo
        arquivo.parent.mkdir(parents=True, exist_ok=True)

        try:
            with open(arquivo, "r", encoding="utf-8") as archv:
                jogador = json.load(archv)
                en.load_weapon(jogador)
                json_int_keys(jogador)
                return jogador
            
        except (FileNotFoundError, json.JSONDecodeError):
            jogador = deepcopy(p.jogadores_database[1])
            with open(arquivo, "w", encoding="utf-8") as archv:
                json.dump(jogador, archv, indent=4, ensure_ascii=False)
            en.load_weapon(jogador)
            json_int_keys(jogador)
            return jogador

def save(player, arquivo="player1.json"):
    arquivo = Path("saves") / arquivo
    arquivo.parent.mkdir(parents=True, exist_ok=True)
    
    jogador_save = deepcopy(player)
    en.unload_weapon(jogador_save)
    with open(arquivo, "w", encoding="utf-8") as archv:
        json.dump(jogador_save, archv, indent=4, ensure_ascii=False)

def int_key(entity):
    novo = {}
    for k, v in entity.items():
        if isinstance(k, str) and k.isdigit():
            k = int(k)

        novo[k] = v
    return novo

def json_int_keys(entity):
    entity['ataques'] = int_key(entity['ataques'])
