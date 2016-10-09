#code from http://www.nltk.org/howto/childes.html

import nltk
from nltk.corpus.reader import CHILDESCorpusReader
corpus_root = ('/Users/callab/Documents/Projects/CHILDES/Corpora/')

def remove_non_ascii_1(text):
    return ''.join(i for i in text if ord(i)<128)

#providence = CHILDESCorpusReader(corpus_root, 'childes_corpora/Providence/.*.xml')
childes = CHILDESCorpusReader(corpus_root, '.*.xml')


#Some useful codes. 
#display the files names for Providence
childes.fileids()
#count the number of files
len(childes.fileids())
#printing properties of the corpus files
corpus_data = childes.corpus(childes.fileids())
print(corpus_data[0]['Lang'])
for key in sorted(corpus_data[1].keys()):
    print(key ,":", corpus_data[1][key])
#Printing participant information. CHI (target child), MOT(mother), INV (investigator)
#something is wrong in my print
corpus_participants = childes.participants(childes.fileids())
for this_corpus_participants in corpus_participants[3:5]:
    for key in sorted(this_corpus_participants.keys()):
        dct = this_corpus_participants[key]
        print(key, ": ", [(k, dct[k]) for k in sorted(dct.keys())])
#printing words
childes.words()[0:100]
#printing sentences
childes.sents()[0:100]
#use word stems (e.g., 'is' -> 'be-3PS') instread of the original words.
childes.words()[:30]
childes.words(stem=True)[:30]
#Printing age. When the argument month is true, the age information in the CHILDES format is converted into the number of months.
childes.age('/Providence/Alex/ale01.xml')
childes.age('Providence/Alex/ale01.xml', month=True)
#other schtuff, counting words.
for this_file in providence.fileids()[:10]:
    print(providence.corpus(this_file)[0]['Corpus'], providence.corpus(this_file)[0]['Media'])
    print("num of words: %i" % len(providence.words(this_file)))
    print("num of sents: %i" % len(providence.sents(this_file)))








#get all childes copora
CHILDES_all=' '.join(childes.words())
CHILDES_all_dropped = remove_non_ascii_1(CHILDES_all)
CHILDES_split = CHILDES_all_dropped.split(" ")
CHILDES_split = map(lambda x: x.encode('ascii'), CHILDES_split)
#drop unintelligible codes?
CHILDES_fixed= [x for x in CHILDES_split if x != 'yyy' and x != 'xxx' and x != 'www']
file= open("CHILDES_words_only.txt", "w")
file.write(CHILDES_fixed)
file.close()


#####trying to stem:
#CHILDES stemmer is problematic.
#CHILDES_all=' '.join(childes.words(stem=True))

#Snowball Stemmer is preferred (> Porter).
from nltk.stem.snowball import SnowballStemmer
stemmer= SnowballStemmer("english")
    
def get_stems(text):
    return ' '.join(stemmer.stem(i) for i in text)



childes_stemmed = get_stems(CHILDES_fixed)
with open("CHILDES_words_stemmed.txt", "a") as myfile:
    myfile.write(childes_stemmed)


#mother produced words
#mom_speech=' '.join(childes.words(speaker='MOT', replace=True))
#drop special characters (they cause problems)
#mom_dropped = remove_non_ascii_1(mom_speech)
#return to list where elements are whole words
#mom_split = mom_dropped.split(" ")
#mom_fixed = remove_missed_words(mom_split)
#mom_split = mom_fixed.split(" ")
#mom_words = get_stems(mom_split)
#with open("CHILDES_cds_stemmed.txt", "a") as myfile:
 #   myfile.write(mom_words)



#stemming the cdi words to allow for subsetting to those words later
file = open('all_cdi_words.txt', 'r')
lines = file.read().splitlines()
lines_stemmed = get_stems(lines)
cdi_stemmed=' '.join(lines_stemmed)
with open("cdi_words_stemmed.txt", "w") as myfile:
    myfile.write(lines_stemmed)


cdi_words = [stemmer.stem(x) for x in lines]
file = open('cdi_words_stemmed.txt', 'w')
for item in cdi_words:
    file.write("%s\n" % item)


