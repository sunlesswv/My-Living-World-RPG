from utils import strings as st
from game import entities as en


def fimdojogo(hp, mp):
    if hp == 0:
        return 'loose'
    if mp == 0:
        return 'win'
    else:
        return 'continue'
    
def perfil(jogador):
    print(st.colors(f'sua vida é: {jogador['status']['hp']:.0f}', 6))
    print(st.colors(f'seu nivel é: {jogador['level']:.0f}', 6))
    print(st.colors(f'seu xp é: {jogador['xp']:.0f}/{en.req_xp(jogador):.0f}', 6))