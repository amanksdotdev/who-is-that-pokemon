from simple_chalk import chalk
import pokebase as pb

from lib.helpers import loading
from lib.logger import print_pokemon


def search_pokemon():
    loading('PokeDex')
    name = input('Enter Pokemon Name: ').lower()
    print(chalk.yellow('Searching....\n'))
    pokemon = pb.APIResource('pokemon', name)
    poke_id = pokemon.url.split('/')[-2]
    try:
        poke_id = int(poke_id)
        print_pokemon(poke_id)
    except:
        print(chalk.red('Not Found :('))