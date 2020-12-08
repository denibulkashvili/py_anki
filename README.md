## Description

`py_deck` is a Python script to generate new Anki decks from Markdown files recursively.

## Tools used

* [@kerrickstaley / genanki: A Library for Generating Anki Decks](https://github.com/kerrickstaley/genanki)

## Instructios 

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

### 4. Generate new deck

```
python generate.py [deck_name]
```