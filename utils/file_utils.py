"""File Explorer Module"""
import glob
import uuid

NOTES = '/notes'

class FileExplorer:
    """Handles files realted operations"""
    def __init__(self, root):
        self.root = root + NOTES

    def list_all_files(self, extension=".md"):
        """Lists all the files with passed extension (default='.md')"""
        return [f for f in glob.glob(self.root + f"**/*.{extension}", recursive=True)]

    def __trim_starting_chars(self, string):
        if string.startswith("- "):
            return string[2:]
        return string

    def parse_file(self, file_name):
        """Returns a list of note"""
        with open(file_name, "r", encoding="utf8") as file:
            data = file.readlines()

            notes = []

            for index, line in enumerate(data):
                if index == len(data) - 1:
                    break
                if line.startswith("---"):
                    note_id = self.__trim_starting_chars(data[index + 1])
                    question = self.__trim_starting_chars(data[index + 2])
                    answer = self.__trim_starting_chars(data[index + 3])
                    note = [note_id, question, answer]
                    notes.append(note)

            return notes

    def generate_question_ids(self, file_name):
        """Traverse files and generate rand ids for each question if not exist"""
        print('file', file_name)

        with open(file_name, "r", encoding="utf8") as reader:
            data = reader.readlines()


            for index, line in enumerate(data):
                if index == len(data) - 1:
                    break
                if line.startswith("---"):
                    note_id = self.__trim_starting_chars(data[index + 1])

                    if len(note_id) == 1:
                        new_id = str(uuid.uuid4()) + '\n'
                        data[index + 1] = f'- {new_id}'

        with open(file_name, "w", encoding="utf8") as writer:
            writer.writelines(data)
