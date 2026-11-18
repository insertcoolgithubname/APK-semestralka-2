# -*- coding: utf-8 -*-
from pathlib import Path
from math import inf


# ukladani mezivysledku, pokud se ptame dvakrat na stejnou vec
# dict, klic je tuple word a distance, value je set vracenych podobnych slov dane distance
seen = {}


def initialize(filepath, coding="cp1250"):
    '''
    vstup:
      * filepath - soubor se vstupním textem
      * coding - kódování vstupního textu
    výstup:
      * data - metoda vrací "objekt" data. může to být cokoliv - seznam, slovník, množina, tupple, či jen "identifikátor"
    '''
    all_words = set()
    with Path(filepath).open("r", encoding=coding) as f:
        for line in f:
            line_list = line.split()
            line_list
            for word in line_list:
                debug = word
                # nahradim nechtene znaky
                # mozna bude lepsi proste rstrip, lstrip
                chars_to_strip = r".\"',()[]-?!@:"
                # jenom na konci a zacatku
                word = word.lstrip(chars_to_strip).rstrip(chars_to_strip)
                # porovnavame jako lowercase
                word = word.lower()

                if any(char == word for char in ["-", "", "%"]):
                    continue
                all_words.add(word)

    return all_words


def find_similar(word: str, data, distance=0):
    ''' 
    vstup: 
      * word - hledané slovo
      * data - předzpracovaná data
      * distance - počet rozdílů nalezených slov od hledaného slova (word). jeden rozdíl je roven např. jedné záměně,
        jednomu chybějícímu či přebývajícímu písmenku
    výstup:
      * data - metoda vrací množinu obsahující výsledek
    '''
    # distance je presne ta vzdalenost, ne maximalne
    # Pozn.: budeme uvažovat max(distance) = 10

    # ma cenu porovnavat jenom rozdil vzdalenosti mensi nez chyba (nebo podobne)

    similar_words = set()
    len_of_word = len(word)
    # normalizace velkych pismen
    word = word.lower()
    if distance == 0:
        if word in data:
            return set([word])
    else:
        # zkontroluju, jestli uz jsem videl nekdy videl tuto otazku
        if (word, distance) in seen:
            return seen[(word, distance)]
        for data_word in data:
            # pokud je rozdil vetsi nez vzdalenost, nejde se na to slovo dostat, preskocim
            if abs(len(data_word) - len_of_word) > distance:
                continue
            data_distance = levenshtein(word, data_word, distance)
            if data_distance == distance:
                similar_words.add(data_word)

    # nez vratim, pridam ji do uz videnych otazek
    seen[(word, distance)] = similar_words
    return similar_words


def levenshtein(a, b, distance):
    # staci pocitat pas ve vzdalenosti (distance) od hlavni diagonaly
    # upravuji tuhle funkci pro hledani presne vzdalenosti, ne jako obecny levenshtein
    n, m = len(a), len(b)
    D = [[inf] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        # beru jenom pas o velikosti distance od hlavni diagonaly
        for j in range(max(1, i-distance), min(m, i+distance) + 1):
            D[i][j] = min(D[i-1][j] + 1,  # smazání
                          D[i][j-1] + 1,  # vložení
                          D[i-1][j-1] + (a[i-1] != b[j-1]))

    return D[n][m]


if __name__ == "__main__":
    data = initialize("CZ_KKY_APK_dump.txt", "utf-8")
    # print(find_similar(u"dobrý", data, 1))
    # print(find_similar(u"nemocenské", data, 5))
    # print(find_similar(u"jXXXXXednatřicetiletéhoXXXXX", data, 9))
    # print(levenshtein('kitten', 'sitting'))
    # print(levenshtein(['zapni', 'světlo'], ['zapni', 'světla']))
