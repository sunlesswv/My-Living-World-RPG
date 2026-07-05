from utils import strings as st
from game import entities as en


def fimdojogo(hp, mp):
    if hp == 0:
        return 'loose'
    if mp == 0:
        return 'win'
    else:
        return 'continue'
    
def perfil(entity, progresso = True):
    st.lin(50)
    print(entity['nome'].upper().center(50))
    print(st.colors(f'vida : {entity['status']['hp']:.0f}', 6))

    if progresso == True:
        print(st.colors(f'nivel: {entity['level']:.0f}', 6))
        print(st.colors(f'xp : {entity['xp']:.0f}/{en.req_xp(entity):.0f}', 6))

def mostrar_ataques(jogador):
    st.linc('MENU DE ATAQUES', 50)
    for id_atq, ataque in jogador['ataques'].items():
        print(f'[{id_atq}]: {ataque['nome']}| dano: {ataque['dano']}')

    st.lin(50)

def escolha_ataques(jogador):
    while True:
        escolha = st.validnum('Escolha um ataque: ')
        st.lin(50)
        if escolha not in (jogador['ataques']):
            print(st.colors('erro, digite apenas 1,2 ou 3'), 1)
        else:
            return escolha