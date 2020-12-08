"""Main generator module"""
import os
import sys
from utils.anki_utils import AnkiGenerator
from utils.file_utils import FileExplorer

if __name__ == "__main__":
    deck_name = sys.argv[1]

    file_explorer = FileExplorer(os.path.dirname(os.path.realpath(__file__)))
    anki_generator = AnkiGenerator(deck_name)

    files = file_explorer.list_all_files("md")

    notes = []
    for file in files:
        file_explorer.generate_question_ids(file)
        notes = notes + file_explorer.parse_file(file)

    deck = anki_generator.create_deck()
    anki_notes = [anki_generator.create_anki_note(note) for note in notes]

    # add all notes to deck
    for note in anki_notes:
        deck.add_note(note)

    # save to file
    anki_generator.create_deck_file(deck, f"{deck_name}.apkg")
