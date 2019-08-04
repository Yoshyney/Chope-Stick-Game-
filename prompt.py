import inquirer
from inquirer import errors

def WhatToDo():
    questions = [
    inquirer.List('Todo',
                message="What do you want to do ? ",
                choices=["Play against a friend", "Play Against an AI"],
            ),
]
    return inquirer.prompt(questions)

def Ai():
    questions = [
    inquirer.List('AI',
                message="Choose Your Ai ! ",
                choices=["Stupid", "Normal", "Smart"],
            ),
]
    return inquirer.prompt(questions)

def askPlayerName():
    questions = [
    inquirer.Text('Name1', message="Name of the first player ", validate=name_validation),
    inquirer.Text('Name2', message="Name of the second player ", validate=name_validation),
    ]
    return inquirer.prompt(questions)


def name_validation(answers, current):
    if current == "":
        raise errors.ValidationError('', reason='Plz enter a correct name :)')

    return True