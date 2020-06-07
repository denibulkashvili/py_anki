import os
import glob

NOTES = '/notes'

class FileExplorer:
    def __init__(self, root):
        self.root = root + NOTES

    def list_all_files(self, extension=".md"):
        """Lists all the files with passed extension (default='.md')"""
        return [f for f in glob.glob(self.root + f"**/*.{extension}", recursive=True)]

    def __trim_starting_chars(self, str):
        if str.startswith("- "):
            return str[2:]
        return str

    def parse_file(self, file_name):
        """Returns a list of note"""
        with open(file_name, "r", encoding="utf8") as file:
            data = file.readlines()

            notes = []

            for index, line in enumerate(data):
                if index == len(data) - 1:
                    break
                if line.startswith("---"):
                    id = self.__trim_starting_chars(data[index + 1])
                    question = self.__trim_starting_chars(data[index + 2])
                    answer = self.__trim_starting_chars(data[index + 3])
                    note = [id, question, answer]
                    notes.append(note)

            return notes
