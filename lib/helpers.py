from simple_chalk import chalk
import pokebase as pb

def loading(text: str):
    print(chalk.yellow(f"Loading {text}...\n"))

def get_pokemon_name(id):
    return pb.APIResource('pokemon', id)