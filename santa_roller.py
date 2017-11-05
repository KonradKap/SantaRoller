#!/bin/python3

import random # potrzebne po randint

#lista zjebów
zjebs_kto = ["Azahiel", "Memotosz", "Boro", "Nathel", "Kozak", "Udrii", "Piket", "Vador", "Vuko", "Deczu", "Fipek"]
sam_sobie = True # czy kupuje sam sobie

while sam_sobie: # jesli ktos kupuje sam sobie
    zjebs_komu = zjebs_kto[:] # skopiuj zjebow
    kto_komu = {kto : zjebs_komu.pop(random.randint(0, len(zjebs_komu)-1)) for kto in zjebs_kto} # skopiowane z SO
    sam_sobie = any(kto == komu for kto, komu in kto_komu.items()) # tez

for kto, komu in kto_komu.items(): # przeiteruj po zjebach
    print("{} kupuje {}owi".format(kto, komu)) # wypisz kto komu kupuje prezent
