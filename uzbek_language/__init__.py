from uzbek_language.transliterate import to_cyrillic, to_latin
from uzbek_language import uzwords_latin, uzwords

from difflib import get_close_matches



class Translator:
    def __init__(self, text:str) -> None:
        self.text: str = text

    def latin(self) -> str:
        return to_latin(text=self.text)
    
    def cyrillic(self) -> str:
        return to_cyrillic(text=self.text)
    
    def auto(self):
        if self.text.isascii():
            return to_cyrillic(text=self.text)
        else:
            return to_latin(text=self.text)
        

class Spelling:
    def __init__(self, word: str, word_type: str="latin", n:int=5) -> None:
        self.__words_lanin: list = uzwords_latin.words
        self.__words: list = uzwords.words
        self.__word: str = word.lower()
        self.__word_type: str = word_type
        self.__n: int = n

    def get_words(self):
        if self.__word_type == "latin":
            return self.__words_lanin
        else:
            return self.__words

    def __checkWord(self):
        word: str = self.__word
        words: list = self.get_words()
        n: int = self.__n

        matches = set(get_close_matches(word, words, n=n))

        availible: bool = False

        if word in matches:
            availible: bool = True
            matches: str = word
        elif 'ҳ' in word:
            word = word.replace('ҳ', 'х')
            matches.update(get_close_matches(word, words, n=n))
        elif 'х' in word:
            word = word.replace('х', 'ҳ')
            matches.update(get_close_matches(word, words, n=n))
        elif 'x' in word:
            word = word.replace('x', 'h')
            matches.update(get_close_matches(word, words, n=n))
        elif 'h' in word:
            word = word.replace('h', 'x')
            matches.update(get_close_matches(word, words, n=n))


        return [availible, matches]
    
    def is_availible(self):
        return self.__checkWord()[0]
    
    def get_matches(self):
        return self.__checkWord()[1]