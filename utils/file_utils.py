"""File Explorer Module"""
# import glob
import uuid
import os

class FileExplorer:
    """Handles files realted operations"""
    def __init__(self, root):
        self.root = root + '/'

    def __trim_starting_chars(self, line):
        """Trim starting character '-' from the beginning of the line"""
        if line.startswith("- "):
            return line[2:]
        if line.startswith("-"):
            return line[1:]
        return line

    def list_all_files(self, dir_name, extension=".md"):
        """Lists all the files with passed extension (default='.md')"""
        path = self.root
        if dir_name:
            path = dir_name
        files = [os.path.join(root_dir, file) 
                        for root_dir, dirs, files in os.walk(os.path.abspath(path)) if len(files)
                        for file in files if file.endswith(extension)]
        return files

    def get_notes_from_files(self, files):
        """Gets all the notes from a list of files"""
        notes = []
        for file in files:
            self.generate_question_ids(file)
            notes = notes + self.parse_file(file)
        return notes

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
