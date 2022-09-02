import inquirer
from lib.logger import print_pokemon
from lib.helpers import loading, get_pokemon_name
from simple_chalk import chalk
import random


class Guesser:
    def __init__(self, guess=3):
        self.guess = guess
        self.guesses_left = self.guess
        self.score = 0

    def guess_name(self, name):
        print(name, self.name)
        if name == self.name:
            self.score += 1
            self.guesses_left = self.guess
            return True
        else:
            self.guesses_left -= 1
            return False

    def get_random_pokemon(self):
        loading("Pokemon Image")
        random_num = random.randint(1, 200)
        self.name = str(get_pokemon_name(random_num))
        print_pokemon(random_num)

    def get_guesses_left(self):
        return self.guesses_left

    def get_score(self):
        return self.score

    def reset_game(self):
        self.guesses_left = self.guess
        self.score = 0

    def get_name(self):
        return self.name


def play():
    question = [inquirer.List(
        'guesses', message="Choose number of guesses", choices=[1, 2, 3, 4, 5])]
    answer = inquirer.prompt(question)
    game = Guesser(answer['guesses'])
    game.get_random_pokemon()
    while True:
        print(chalk.red(f'Guess Left: {game.get_guesses_left()}'))
        print(chalk.magenta(f'Current Score: {game.get_score()}\n'))
        inp = input('Enter name: ').lower()
        if game.guess_name(inp):
            print(chalk.green(f'\nYOU WIN!! Score is {game.get_score()}\n'))
            if ask_to_continue():
                game.get_random_pokemon()
                continue
            else:
                break
        elif game.get_guesses_left() == 0:
            print(
                chalk.red(f'\nUhh, You Lost!! Your Score was {game.get_score()}\n'))
            print(f'Name of the pokemon is {chalk.green(game.get_name())}\n')
            if ask_to_continue():
                game.reset_game()
                game.get_random_pokemon()
                continue
            else:
                break
        else:
            print(chalk.red('\n----------------\nWrong!! Try Again\n----------------\n'))


def ask_to_continue():
    play = input('Continue ? (y/n): ').lower()
    return play == 'y'
