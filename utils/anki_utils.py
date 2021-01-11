"""Anki Generator module"""
import genanki

DEFAULT_NAME = "Default Deck"

MODEL = genanki.Model(
    1283770623,
    "Default",
    fields=[{"name": "Question"}, {"name": "Answer"}],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Question}}",
            "afmt": '{{Question}}<hr id="answer">{{Answer}}',
        }
    ],
)

def generate_deck_id(deck_name):
    """Generates deck id from the deck name"""
    return hash(deck_name)

class AnkiGenerator:
    """Generates Anki Decks"""
    def __init__(self, deck_name=DEFAULT_NAME):
        self.deck_name = deck_name
        self.deck_id = generate_deck_id(self.deck_name)
        self.model = MODEL

    def create_deck(self):
        """Creates a new deck"""
        return genanki.Deck(self.deck_id, self.deck_name)

    def create_anki_note(self, note):
        """Creates a new anki note"""
        try:
            note_id = note[0]
            if note_id.endswith("\r\n"):
                note_id = note[0].rstrip("\r\n")
            fields = note[1:]
            return genanki.Note(model=self.model, guid=note_id, fields=fields)
        except ValueError:
            print("ValueError", note[0])

    def create_deck_file(self, deck):
        """Creates an .apkg deck file"""
        return genanki.Package(deck).write_to_file(f"{self.deck_name}.apkg")
