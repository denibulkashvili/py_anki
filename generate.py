import os
from utils.anki_utils import AnkiGenerator
from utils.file_utils import FileExplorer


if __name__ == "__main__":

    file_explorer = FileExplorer(os.path.dirname(os.path.realpath(__file__)))
    anki_generator = AnkiGenerator()

    files = file_explorer.list_all_files("md")

    notes = []
    for file in files:
        notes = notes + file_explorer.parse_file(file)

    print(notes[:4])

    deck = anki_generator.create_deck()
    anki_notes = [anki_generator.create_anki_note(note) for note in notes]

    # add all notes to deck
    [deck.add_note(note) for note in anki_notes]

    # save to file
    anki_generator.create_deck_file(deck, "deck.apkg")
