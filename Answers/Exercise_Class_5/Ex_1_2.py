import numpy as np

from compsci.data import State

def apply_HO_force(state:State):
    state.force=-state.position

