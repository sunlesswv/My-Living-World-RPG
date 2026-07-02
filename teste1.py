from utils import strings as st
from game import combat as cb
from game import entities as en
from game import menu as mn
from game import save as sv
from database import skills as s
from database import players as p
from database import monstros as m
from database import items as i
from database import weapons as w
from random import randint
from time import sleep
from copy import deepcopy

en.refresh_entity(p.jogadores_database[1])
print(p.jogadores_database[1])