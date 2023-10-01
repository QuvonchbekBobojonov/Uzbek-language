# Uzbek-language



This package was created to correct Uzbek spelling mistakes and translate from Latin to Cyrillic

### Install package

```bash
pip install uzbek-language
```
### Use in translator
```python
from uzbek_language import Translator

text = "salom dunyo"

translate = Translator(text=text)

# output text converted to latin
print(transtale.latin())

# output text converted to cyrillic
print(transtale.cyrillic())

# auto output the modified text
print(transtale.auto())
```
### Use in spelling
```python
from uzbek_language import Spelling

s = Spelling(word='salom')

# if the word is a mistake, it will say the same word
print(s.get_matches())

# determine whether the word is correct or incorrect

print(s.is_availible())
```
#### Developed by Quvonchbek Bobojonov (c) 2023