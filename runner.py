# import functions initialize and find_similar
import users.SP2_interface as optimized
import pickle
import time
import users.SP2_interface_prvotni_verze as prvni

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
data = prvni.initialize("CZ_KKY_APK_dump.txt", "utf-8")
print("počet slov:", len(data), " - doba načtení:", time.time() - start)

start = time.time()
data = optimized.initialize("CZ_KKY_APK_dump.txt", "utf-8")
print("počet slov:", len(data), " - doba načtení:", time.time() - start)

similar = optimized.find_similar("tabulka", data, distance = 1)
# print("podobná slova:", similar)

# load test/reference data


ref_files = ["CZ_KKY_APK_dump.ref-1.pkl", "CZ_KKY_APK_dump.ref-2.pkl", "CZ_KKY_APK_dump.ref.pkl"]
refs = {}
for ref_file in ref_files:
    with open(ref_file, "rb") as f:
        refs[ref_file] = pickle.load(f)
    # print(ref_file, "- počet dotazů:", len(refs[ref_file]))

# ukázka: klíč je (hledané slovo, vzdálenost), hodnota je množina nalezených slov
ref = refs[ref_files[0]]
# print(list(ref.items())[:5])
# print(ref[("sazky", 2)])

pocet_opakovani = 10

prvni_total_time = 0
real_total_time = 0

for _ in range(pocet_opakovani):
    # reset 'seen' pro optimalizovanou verzi
    optimized.seen = {}

    total_chyby_prvni = 0
    for ref_file, ref in refs.items():
        chyb = 0
        cas = 0.0
        for word, dist in ref:
            start = time.time()
            similar = prvni.find_similar(word, data, distance = dist)
            cas += time.time() - start
            #print(word, dist, similar)
            chyb_local = ref[(word, dist)].symmetric_difference(similar)   # prvky jen v jedné z množin
            # if len(chyb_local) > 0:
            #     print("\nchyba    :", word, dist)
            #     print("nalezeno :", similar)
            #     print("správně  :", ref[(word, dist)])
            chyb += len(chyb_local)
        total_chyby_prvni += chyb
        prvni_total_time += cas
        print("\n%s - počet chyb: %d, čas find_similar: %.4f s\n" % (ref_file, chyb, cas))

    total_chyby_optimalizovane = 0
    for ref_file, ref in refs.items():
        chyb = 0
        cas = 0.0
        for word, dist in ref:
            start = time.time()
            similar = optimized.find_similar(word, data, distance = dist)
            cas += time.time() - start
            #print(word, dist, similar)
            chyb_local = ref[(word, dist)].symmetric_difference(similar)   # prvky jen v jedné z množin
            # if len(chyb_local) > 0:
            #     print("\nchyba    :", word, dist)
            #     print("nalezeno :", similar)
            #     print("správně  :", ref[(word, dist)])
            chyb += len(chyb_local)
        total_chyby_optimalizovane += chyb
        real_total_time += cas
        print("\n%s - počet chyb: %d, čas find_similar: %.4f s\n" % (ref_file, chyb, cas))

print(f"extra pocet chyb optimalizovane: {total_chyby_optimalizovane - total_chyby_prvni}")
print(f"pomer zrychleni: {prvni_total_time/real_total_time}")
