#code from http://www.nltk.org/howto/childes.html

import nltk
from nltk.corpus.reader import CHILDESCorpusReader
corpus_root = ('/Users/bmorris/documents/uchicago/childes/')

def remove_non_ascii_1(text):
    return ''.join(i for i in text if ord(i)<128)

providence = CHILDESCorpusReader(corpus_root, 'childes_corpora/Providence/.*.xml')
childes = CHILDESCorpusReader(corpus_root, 'childes_corpora/.*.xml')


#display the files names for Providence
providence.fileids()

#count the number of files
len(providence.fileids())

#printing properties of the corpus files
corpus_data = providence.corpus(providence.fileids())
print(corpus_data[0]['Lang'])
for key in sorted(corpus_data[1].keys()):
    print(key ,":", corpus_data[1][key])

#Printing participant information. CHI (target child), MOT(mother), INV (investigator)
#something is wrong in my print
corpus_participants = providence.participants(providence.fileids())
for this_corpus_participants in corpus_participants[:2]:
    for key in sorted(this_corpus_participants.keys()):
        dct = this_corpus_participants[key]
        print(key, ": ", [(k, dct[k]) for k in sorted(dct.keys())])

#printing words
providence.words('Providence/Alex/ale01.xml')


#printing sentences
providence.sents('Providence/Alex/ale01.xml')[0:100]

#specifying the speaker
providence.words(speaker=['MOT'])
providence.words(speaker = ('MOT', 'OPE', 'INV'))


#tagged_words() and tagged_sents() return the usual (word,pos) tuple lists. POS tags in the CHILDES are automatically assigned by MOR and POST programs (MacWhinney, 2000).
providence.tagged_words('Providence/Alex/ale01.xml')[:30]
providence.tagged_sents('Providence/Alex/ale01.xml')[:30]

#use word stems (e.g., 'is' -> 'be-3PS') instread of the original words.
providence.words('Providence/Alex/ale01.xml')[:30]
providence.words('Providence/Alex/ale01.xml', stem=True)[:30]

#???When the argument replace is true, the replaced words are used instread of the original words.
providence.words('Providence/Alex/ale01.xml')[30]
providence.words('Providence/Alex/ale01.xml', replace=True)[30]

#When the argument relation is true, the relational relationships in the sentence are returned. See Sagae et al. (2010) for details of the relational structure adopted in the CHILDES.
providence.words('Providence/Alex/ale01.xml', relation=True)[:30]

#Printing age. When the argument month is true, the age information in the CHILDES format is converted into the number of months.
providence.age()
providence.age('Providence/Alex/ale01.xml')
providence.age('Providence/Alex/ale01.xml', month=True)
providence.age('Providence/Alex/ale01.xml', month=True)

#Printing MLU. The criteria for the MLU computation is broadly based on Brown (1973).
providence.MLU()
providence.MLU('Providence/Alex/ale01.xml')


#other schtuff, counting words.
for this_file in providence.fileids()[:10]:
    print(providence.corpus(this_file)[0]['Corpus'], providence.corpus(this_file)[0]['Media'])
    print("num of words: %i" % len(providence.words(this_file)))
    print("num of sents: %i" % len(providence.sents(this_file)))


#try dumping just one file from providence
providence_ale01=' '.join(providence.words('Providence/Alex/ale01.xml'))
file= open("providence_ale01.txt", "w")
file.write(providence_ale01)
file.close()


#child produced words...
kid_pro=' '.join(childes.words(speaker='CHI'))

#get all childes copora
CHILDES_all=' '.join(childes.words())
CHILDES_all_dropped = remove_non_ascii_1(CHILDES_all)
file= open("CHILDES_words_only.txt", "w")
file.write(CHILDES_all_dropped)
file.close()


#other schtuff, counting words.
for this_file in childes.fileids()[:10]:
    print(childes.corpus(this_file)[0]['Corpus'], childes.corpus(this_file)[0]['Media'])
    print("num of words: %i" % len(childes.words(this_file)))
    print("num of sents: %i" % len(childes.sents(this_file)))

