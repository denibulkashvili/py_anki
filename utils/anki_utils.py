"""Anki Generator module"""
import genanki

SETTINGS = {
    "deck_id": 2016547257,
    "deck_name": "My Deck",
    "model_id": 1283770623,
    "model_name": "My Model",
}


class AnkiGenerator:
    def __init__(
        self, deck_id=2016547257, deck_name="My Deck", model_id=1283770623, model_name="My Model"
    ):
        self.deck_id = deck_id
        self.deck_name = deck_name
        self.model_id = model_id
        self.model_name = model_name
        self.model = self.__create_model()

    def __create_model(self):
        return genanki.Model(
            self.model_id,
            self.model_name,
            fields=[{"name": "Question"}, {"name": "Answer"}],
            templates=[
                {
                    "name": "Card 1",
                    "qfmt": "{{Question}}",
                    "afmt": '{{Question}}<hr id="answer">{{Answer}}',
                }
            ],
        )

    def create_deck(self):
        return genanki.Deck(self.deck_id, self.deck_name)

    def create_anki_note(self, note):
        try:
            note_id = int(note[0].rstrip("\r\n"))
            fields = note[1:]
            # print(id)
            # print(fields)
            return genanki.Note(model=self.model, guid=id, fields=fields)
        except ValueError:
            print("except")
            print(note[0])

    def create_deck_file(self, deck, file_name="deck.apkg"):
        return genanki.Package(deck).write_to_file(file_name)
