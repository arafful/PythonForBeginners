"""
    TIC TAC TOE - JOGO DA VELHA
"""
import numpy as np
import random
from time import sleep

def new_frame():
    return np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

def blank_spaces(frame):
    sp = []

    for a in range(len(frame)):
        for b in range(len(frame)):
            if frame[a][b] == 0:
                sp.append((a, b))

    return sp

def next_move(frame, gamer):
    picked = blank_spaces(frame)
    chosen_block = random.choice(picked)
    frame[chosen_block] = gamer
    return frame

def vert(frame, gamer):
    for c in range(len(frame)):
        game_win = True
        for d in range(len(frame)):
            if frame[c, d] != gamer:
                game_win = False
                continue
    return game_win

def horiz(frame, gamer):
    for c in range(len(frame)):
        game_win = True
        for d in range(len(frame)):
            if frame[c, d] != gamer:
                game_win = False
                continue

    return game_win

def across(frame, gamer):
    game_win = True
    d = 0
    for c in range(len(frame)):
        if frame[c, c] != gamer:
            game_win = False

    if game_win:
        return game_win

    game_win = True
    if game_win:
        for c in range(len(frame)):
            d = len(frame) - 1 - c
            if frame[c, d] != gamer:
                game_win = False

    return game_win

def win_check(frame):
    victor = 0

    for gamer in [1,2]:
        if(horiz(frame, gamer) or
            vert(frame, gamer) or
            across(frame, gamer)):
            victor = gamer

    if np.all(frame != 0) and victor == 0:
        victor = -1

    return victor

def game():
    frame, victor, turns = new_frame(), 0, 1
    print(frame)
    sleep(2)

    while victor == 0:
        for gamer in [1, 2]:
            frame = next_move(frame, gamer)
            print("Tic-tac-toe move", str(turns))
            print(frame)
            sleep(2)
            turns += 1
            victor = win_check(frame)
            if victor != 0:
                break

    return victor

print(str(game()),"wins this round.")


