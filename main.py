# external library
import inquirer

# internal library
from lib.logger import welcome
from lib.options import Operation
from game import play
from pokedex import search_pokemon


welcome()

ask_operation = [
    inquirer.List('operation', message="What you want to do today ?",
                  choices=[Operation.POKEDEX.value, Operation.RANDOMPOKEMON.value])
]

choice = inquirer.prompt(ask_operation)


if choice['operation'] == Operation.POKEDEX.value:
    search_pokemon()

if choice['operation'] == Operation.RANDOMPOKEMON.value:
    play()
