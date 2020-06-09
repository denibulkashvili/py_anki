"""Anki Generator module"""
import genanki

DEFAULT = {
    "id": 2016547257,
    "name": "My Deck"
}

MODEL = genanki.Model(
    1283770623,
    "My Model",
    fields=[{"name": "Question"}, {"name": "Answer"}],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Question}}",
            "afmt": '{{Question}}<hr id="answer">{{Answer}}',
        }
    ],
)

def _generate_deck_id(deck_name):
    """Generates deck id from the deck name"""
    return deck_name.lower().replace(" ", "_")

class AnkiGenerator:
    """Generates Anki Decks"""
    def __init__(self, deck_id=DEFAULT["id"], deck_name=DEFAULT["name"]):
        self.deck_id = deck_id
        self.deck_name = deck_name
        self.model = MODEL
   
    def create_deck(self):
        """Creates new deck"""
        return genanki.Deck(self.deck_id, self.deck_name)

    def create_anki_note(self, note):
        """Creates new anki note"""
        try:
            note_id = note[0]
            if note_id.endswith("\r\n"):
                note_id = note[0].rstrip("\r\n")
            fields = note[1:]
            return genanki.Note(model=self.model, guid=note_id, fields=fields)
        except ValueError:
            print("ValueError", note[0])

    @classmethod
    def create_deck_file(cls, deck, file_name="deck.apkg"):
        """Creates an .apkg deck file"""
        return genanki.Package(deck).write_to_file(file_name)
