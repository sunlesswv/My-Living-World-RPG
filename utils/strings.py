from time import sleep

def moneyf(p=0, m='R$'):
    return f'{m}{p:.2f}'.replace('.',',')

def lin(l=30, c = '-'):
    print(c*l)

def linf(msg = ' '):
    lin(len(msg)+4)
    print(f'  {msg}  ')
    lin(len(msg)+4)

def linc(msg=' ',espaces=30):
    lin(espaces)
    print(msg.center(espaces))
    lin(espaces)
        
def validnum(msg = 'digite um numero: ', tipo=float):
    while True:
        try: 
            return tipo(input(msg))
        except ValueError:
            if tipo == float:
                print(f'\033[31merro, digite apenas numeros reais {ValueError}\033[m')
            else: 
                print(f'\033[31merro, digite apenas numeros inteiros {ValueError}\033[m')
        except KeyboardInterrupt:
            print(f'\033[31merro, numero não informado {KeyboardInterrupt}\033[m')

def cadastro(menu):
    lin(42)
    for pos, c in enumerate(menu):
        print(f'\033[33m{pos+1} - \033[36m{c}\033[m')
    lin(42)

def valid_name(name):
    while True:
        if name.strip() == '':
            print(f'\033[31merro, nome invalido\033[m')
            name = input('digite o nome novamente: ')
        else:
            return name
        
def colors(text= '', color = 0):
    """
    :param1 text: texto a ser colorido
    :param2 color: cor escolhida(apenas as letras)
    :return: texto colorido e cores retiradas no fim
    """
    c = ('\033[m', #0 - sem cores
     '\033[31m',   #1 - vermelho         
     '\033[32m',   #2 - verde
     '\033[33m',   #3 - amarelo
     '\033[34m',   #4 - roxo
     '\033[35m',   #5 - rosa
     '\033[36m',   #6 - azul
     '\033[37m'    #7 - branco
    )
    if color not in range(len(c)):
        print(f'{c[1]}Erro: cor inválida. Usando a cor padrão.{c[0]}')
        color = 0
    return f'{c[color]}{text}{c[0]}'
    
def pontos(vezes=6, tempo=0.5):
    for c in range(vezes):
        print('.',end='', flush=True)
        sleep(tempo)

def validfim():
    while True:
        fim = input('vc quer continuar?[S]/[N] ').strip().upper()
        if fim not in ('S', 'N'):
            print('Erro, digite apenas S ou N')   
        elif fim == 'S':
            return False
        elif fim == 'N':
            return True