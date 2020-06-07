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

### 4. Generate new deck

```
python generate.py
```