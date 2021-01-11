"""Main generator module"""
import os
import sys
from utils.anki_utils import AnkiGenerator
from utils.file_utils import FileExplorer
import utils.script as Scripts

if __name__ == "__main__":
    deck_name, dir_name = Scripts.get_args(sys.argv)

    # Init utils
    file_explorer = FileExplorer(os.path.dirname(os.path.realpath(__file__)))
    anki_generator = AnkiGenerator(deck_name)

    # Explorer
    files = file_explorer.list_all_files(dir_name)
    notes = file_explorer.get_notes_from_files(files)

    # Anki
    deck = anki_generator.create_deck()
    anki_notes = [anki_generator.create_anki_note(note) for note in notes]
    # add all notes to deck
    for note in anki_notes:
        deck.add_note(note)

    # save to file
    anki_generator.create_deck_file(deck)

    print(f'File {deck_name}.apkg successfully generated!')
