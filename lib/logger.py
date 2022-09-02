import climage
from simple_chalk import chalk
import pokebase as pb


def print_image(src, width=80):
    image = climage.convert(src, is_unicode=True,
                            is_truecolor=True, is_256color=False, width=width)
    print(image)


def show_banner():
    print_image('static/pokeapi.png')


def show_instructions():
    print(chalk.yellow(
        'Use Up(↑) and Down(↓) arrow keys to change selection and Enter(⏎) to confirm choice.'))
    print()


def welcome():
    show_banner()
    print(chalk.green.bold.underline("Welcome to the game !!\n"))
    show_instructions()


def print_pokemon(id: int):
    poke_image = pb.SpriteResource('pokemon', id)
    print_image(poke_image.path, width=40)