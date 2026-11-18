# -*- coding: utf-8 -*-
from pathlib import Path


def initialize(filepath, coding = "cp1250"):
    ''' 
    vstup: 
      * filepath - soubor se vstupním textem
      * coding - kódování vstupního textu
    výstup:
      * data - metoda vrací "objekt" data. může to být cokoliv - seznam, slovník, množina, tupple, či jen "identifikátor"
    '''
    all_words = {}
    with Path(filepath).open("r", encoding=coding) as f:
        for line in f:
            line_list = line.split()
            line_list
            for word in line_list:
                debug = word
                # nahradim nechtene znaky
                trans = str.maketrans({'.': None, '"': None, "'": None, ",": None, "(": None, ")": None,
                                       "-": None})
                # jenom na konci a zacatku
                if len(word) > 1:
                    word = word[0].translate(trans) + word[1:-1] + word[-1].translate(trans)
                # pokud je slovo jen o delce 1, nahrazuji na celem
                else:
                    word = word.translate(trans)
                # porovnavame jako lowercase
                word = word.lower()

                if any(char == word for char in ["-", "", "%"]):
                    continue
                if word in all_words.keys():
                    all_words[word] += 1
                else:
                    all_words[word] = 1

    # print(sorted(all_words.keys()))
    # print(all_words)
    return all_words


def find_similar(word, data, distance = 0):
    ''' 
    vstup: 
      * word - hledané slovo
      * data - předzpracovaná data
      * distance - počet rozdílů nalezených slov od hledaného slova (word). jeden rozdíl je roven např. jedné záměně, 
        jednomu chybějícímu či přebývajícímu písmenku 
    výstup:
      * data - metoda vrací množinu obsahující výsledek
    '''
    # distance je presne ta vzdalenost, ne maximalne takhle
    similar_words = set()
    return similar_words
    

if __name__ == "__main__":
    data = initialize("CZ_KKY_APK_dump.txt", "utf-8")
    # print(find_simiar(u"dobrý", data, 1))