
import os
import inquirer
import prompt
import sys
import select
import time
import minimax
import random
clear = lambda: os.system('clear')

def start():
    frame = 192
    fps = frame
    stop = False
    while True:
        clear()
        print('Welcome to the match stick game !')
        fps = fps - 1
        if fps <= frame / 2:
            print('')
            if fps == 0:
                fps = frame
        else :
            print('please press Enter to continue !')
        while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            if sys.stdin.readline() == "\n":
                stop = True 
        if stop:
            break
    clear()
    result = Todo()
    if result is not None:
        if result['Todo'] == "Play against a friend":
            playHuman()

        else:
            choseAi()
    else:
        print('bye')
        return

def Todo():
    return prompt.WhatToDo()

def playHuman():
    humanNames = prompt.askPlayerName()
    human =  [ humanNames['Name1'], humanNames['Name2']]
    sticks = 11
    playingturn = 0
    while sticks > 0:
        displayGame(sticks)
        print("\nIt's the turn of : " + human[playingturn])
        while True:
            playing = input('How many sticks you want to remove ?')
            if sticks >= int(playing, 10) and int(playing, 10) <= 3 and int(playing, 10) >= 1:
                break
            else:
                print('please enter a correct value !')
        sticks = sticks - int(playing, 10)
        looser = human[playingturn]
        if playingturn == 0:
            playingturn = playingturn + 1
        else :
            playingturn = playingturn - 1
        winner = human[playingturn]
    conditionalVictory( winner , looser)


def choseAi():
    clear()
    result = prompt.Ai()
    if result is not None:
        if result['AI'] == "Stupid":
            playAgainstAi(1)
        elif result['AI'] == "Normal":
            playAgainstAi(2)
        else:
            playAgainstAi(7)
    else:
        print('bye')
        return


def playAgainstAi(depth):
    clear()
    players = ["You", "Ai"]
    random.shuffle(players)
    sticks = 11
    playingturn = 0
    while sticks > 0:
        print("It's the turn of : " + players[playingturn])
        displayGame(sticks)
        while True:
            if players[playingturn] == "You":
                playing = input('\nHow many sticks you want to remove ?')
            else:
                playing = minimax.Max(sticks, depth, 1)
                print('\n' + players[playingturn] + " removed " + playing)
            if sticks >= int(playing, 10) and int(playing, 10) <= 3 and int(playing, 10) >= 1:
                break
            else:
                print('please enter a correct value !')
        sticks = sticks - int(playing, 10)
        looser = players[playingturn]
        if playingturn == 0:
            playingturn = playingturn + 1
        else :
            playingturn = playingturn - 1
            winner = players[playingturn]
    AiConditional( winner , looser)


def displayGame(sticks):
    while sticks > 0:
        print('|',  end = '')
        sticks =  sticks - 1

def conditionalVictory(winner , looser):
        print("Well played " + winner + " you destroyed " + looser)
        print("You will be redirected to main menu in 5 seconds ! ")
        print(" Ty for playing :)") 
        time.sleep(5)
        start()

def AiConditional( winner , looser):
    if winner == "Ai":
        print("AHAHAH YOU LOSE AGAINST ME IM 2 STRONG FOR YOU")
        print("HUMAN SUCK :)")
        print(" Ty for playing :)") 
        time.sleep(5)
        start()
    else:
        print("I lost... snif... but I’ll get you next time!!")
        print("Human still suck (:")
        print(" Ty for playing :)") 
        time.sleep(5)
        start()
