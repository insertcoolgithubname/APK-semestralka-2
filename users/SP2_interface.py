# -*- coding: utf-8 -*-

def initialize(filepath, coding = "cp1250"):
    ''' 
    vstup: 
      * filepath - soubor se vstupním textem
      * coding - kódování vstupního textu
    výstup:
      * data - metoda vrací "objekt" data. může to být cokoliv - seznam, slovník, množina, tupple, či jen "identifikátor"
    '''
    all_words = {}
    all_words['example'] = 999
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
    similar_words = set()
    return similar_words
    

if __name__ == "__main__":
    data = initialize("CZ_KKY_APK_dump.txt", "utf-8")
    print(find_simiar(u"dobrý", data, 1))