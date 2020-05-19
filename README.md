## Description

`py_deck` is a Python tool to generate new Anki decks from a collection of Markdown files.

## Tools used

* Python 3
* [@kerrickstaley / genanki: A Library for Generating Anki Decks](https://github.com/kerrickstaley/genanki)
* [@njvack / Markdown to JSON converter](https://github.com/njvack/markdown-to-json)

## Instructios 

### 1. Install dependencies 
```
pip install markdown-to-json genanki 
```

### 2. Add new cards to `.md` files inside `notes/` directory. Each card should include:
  * id
  * question 
  * answer

Example 
```
# ID
116636636
# Question
What is the value of `PI`?
# Answer
3.14
```

### 3. Convert `.md` files to `.json` 

```
md_to_json -o deck.json ./notes/**/*.md
```

### 4. Generate new deck

```
python generate.py
```