# import functions initialize and find_similar
from users.SP2_interface import initialize, find_similar
import pickle
import time

# or make your own
'''
def initialize(filepath, coding = "cp1250"):
    all_words = {}
    all_words['example'] = 999
    return all_words

def find_similar(word, data, distance = 0):
    similar_words = set()
    return similar_words
'''

# read all data to object data


start = time.time()
data = initialize("CZ_KKY_APK_dump.txt", "utf-8")
print("počet slov:", len(data), " - doba načtení:", time.time() - start)
#print("all words", data.keys())

#test
similar = find_similar("tabulka", data, distance = 1)
print("podobná slova:", similar)

# load test/reference data


ref_files = ["CZ_KKY_APK_dump.ref-1.pkl", "CZ_KKY_APK_dump.ref-2.pkl", "CZ_KKY_APK_dump.ref.pkl"]
refs = {}
for ref_file in ref_files:
    with open(ref_file, "rb") as f:
        refs[ref_file] = pickle.load(f)
    print(ref_file, "- počet dotazů:", len(refs[ref_file]))

# ukázka: klíč je (hledané slovo, vzdálenost), hodnota je množina nalezených slov
ref = refs[ref_files[0]]
print(list(ref.items())[:5])
print(ref[("sazky", 2)])

# test my code
for ref_file, ref in refs.items():
    chyb = 0
    cas = 0.0
    for word, dist in ref:
        start = time.time()
        similar = find_similar(word, data, distance = dist)
        cas += time.time() - start
        #print(word, dist, similar)
        chyb_local = ref[(word, dist)].symmetric_difference(similar)   # prvky jen v jedné z množin
        if len(chyb_local) > 0:
            print("\nchyba    :", word, dist)
            print("nalezeno :", similar)
            print("správně  :", ref[(word, dist)])
        chyb += len(chyb_local)
    print("\n%s - počet chyb: %d, čas find_similar: %.4f s\n" % (ref_file, chyb, cas))