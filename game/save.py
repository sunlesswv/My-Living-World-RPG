import json
from database import players as p
from copy import deepcopy
from pathlib import Path
from game import entities as en
from utils import strings as st


def load_save(arquivo):
        arquivo = Path("saves") / arquivo
        arquivo.parent.mkdir(parents=True, exist_ok=True)
        with open(arquivo, "r", encoding="utf-8") as archv:
            jogador = json.load(archv)
            en.load_weapon(jogador)
            en.load_skills(jogador)
            json_int_keys(jogador)
            return jogador
            
            
def save(player, arquivo="player1.json"):
    arquivo = Path("saves") / arquivo
    arquivo.parent.mkdir(parents=True, exist_ok=True)
    
    jogador_save = deepcopy(player)
    en.unload_weapon(jogador_save)
    en.unload_skills(jogador_save)
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

def choose_save():
    if not Path("saves").is_dir():
        Path("saves").mkdir()

    arquivos = []
    for arquivo in Path("saves").glob("*.json"):
        arquivos.append(arquivo.stem)

    print('SAVES REGISTRADOS'.center(50))
    st.lin(50)

    if not arquivos:
        while True:
            escolha = st.validnum('nenhum save criado\n[0] para criar um novo\n', int)
            if escolha != 0:
                print(st.colors('erro, digite apenas 0', 1))
            else:
                break
        return new_save()

    for c, arquivo in enumerate(arquivos):
        print(st.colors(f'[{c+1}]: {arquivo}', 6))
    st.lin(50)
    while True:
        escolha = st.validnum('qual save carregar?(0 para novo)\n', int)
        if escolha not in range(len(arquivos)+1):
            print(st.colors(f'erro, digite numeros apenas entre 0, {(len(arquivos))}', 1))
        else:
            break
    if escolha == 0:
        return new_save()
    else:
        save = f"{arquivos[escolha-1]}.json"
        return load_save(save), save
    
def new_save():
    while True:
        nome = st.valid_name(input('digite o nome do save a ser criado: '))
        save_path = Path("saves") / f"{nome}.json"
        if save_path.is_file():
            print(st.colors('erro, esse save ja existe', 1))
        else:
            jogador = deepcopy(p.jogadores_database[1])
            jogador['status']['hp'] = jogador['status_max']['hp']
            jogador['status']['mana'] = jogador['status_max']['mana']
            jogador['nome'] = st.valid_name(input('digite o do personagem: '))
            with open(save_path, "w", encoding="utf-8") as archv:
                json.dump(jogador, archv, indent=4, ensure_ascii=False)
            return load_save(save_path.name), save_path.name 
