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
                # mozna bude lepsi proste rstrip, lstrip
                trans = str.maketrans({'.': None, '"': None, "'": None, ",": None, "(": None, ")": None,
                                       "-": None, "?": None, "!": None, "@": None, "[": None, "]": None})
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
    # distance je presne ta vzdalenost, ne maximalne
    # Pozn.: budeme uvažovat max(distance) = 10

    similar_words = set()
    return similar_words


def levenshtein(a, b):
    n, m = len(a), len(b)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i-1][j] + 1,  # smazání
                          D[i][j-1] + 1,  # vložení
                          D[i-1][j-1] + (a[i-1] != b[j-1]))

    return D[n][m]


if __name__ == "__main__":
    data = initialize("CZ_KKY_APK_dump.txt", "utf-8")
    print(find_similar(u"dobrý", data, 1))
    # print(levenshtein('kitten', 'sitting'))
    # print(levenshtein(['zapni', 'světlo'], ['zapni', 'světla']))
