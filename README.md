## Description

`py_anki` is a Python script to generate new [Anki](https://apps.ankiweb.net/) decks from Markdown files recursively.

## Tools used

* [@kerrickstaley / genanki: A Library for Generating Anki Decks](https://github.com/kerrickstaley/genanki)

## Instructions 

### 1. Install dependencies 
```
pip install genanki 
```

### 2. Add new cards to `.md` files inside `notes/` directory. Each card should include:
  * id
  * question 
  * answer
  * should be separated by `---`
  * each line should should start with `-`

Example 
```
---
- 116636636
- What is the value of `PI`?
- 3.14
---
```

### 3. Generate new deck

```
python generate.py [deck_name] [path]
```
Examples
```
python generate.py my_deck notes
python generate.py my_deck /home/abs/path/to/my/dir/
```