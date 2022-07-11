from mimetypes import init
from pickle import APPEND


protein = 'aug111uga11auguga'

rf_index = 0
_codons = [[], [], []]


def rf_index_track(rf_index):
    rf_index += 1
    if rf_index == 3:
        rf_index = 0


def translation(i, rf_idx): #performs the actual parsing of the dna strand. i is the index value given at found 'aug'
    global rf_index
    print(f'translation called with {rf_idx}')
    for j in range(i, len(protein), 3): #starts at aug i = 0
        current_Codon = protein[j] + protein[j + 1] + protein[j + 2]
        if (current_Codon == 'uga' or current_Codon == 'uaa' or current_Codon == 'uag'):#if True, it does go through
            print(i , j, current_Codon, current_Codon == 'uga' or current_Codon == 'uaa' or current_Codon == 'uag', "breakpoint","\n")
            _codons[rf_idx].append('STOP')
            rf_index += 1
            if rf_index == 3:
                rf_index = 0
            break
        else:
            _codons[rf_idx].append(current_Codon)
            # i += 1
            print(i, "added index")

def ribosome(protein):
    global rf_index
    i = 0
    while i <= len(protein)-3:
        print(i, protein[i], "current index", rf_index, "reading frame", "\n")
        if protein[i] + protein[i + 1] + protein[i + 2] == 'aug':
            translation(i, rf_index)
            print(f'called translation with {i}, {rf_index}',"\n")
            i += 1
            # break
        print('past while')
        i += 1
        rf_index += 1
        if rf_index == 3:
            rf_index = 0





                # break



ribosome(protein)
print(len(protein))
# print(codons) #should print aug vvv zzz stop
print(_codons)
