import os
import nltk
import nltk.corpus
os.listdir(nltk.data.find('corpora'))
nltk.corpus.gutenberg.fileids()
hamlet=nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
hamlet
sent=[]
for word in hamlet[:500]:
    print(word, sep=' ', end=' ')
    sent.append(word)

sent ='''[ The Tragedie of Hamlet by William Shakespeare 1599 ] Actus Primus . Scoena Prima . Enter Barnardo and Francisco two Centinels . Barnardo . Who ' s there ? Fran . Nay answer me : Stand & vnfold your selfe Bar . Long liue the King Fran . Barnardo ? Bar . He Fran . You come most carefully vpon your houre Bar . ' Tis now strook twelue , get thee to bed Francisco Fran . For this releefe much thankes : ' Tis bitter cold , And I am sicke at heart Barn . Haue you had quiet Guard ? Fran . Not a Mouse stirring Barn . Well , goodnight . If you do meet Horatio and Marcellus , the Riuals of my Watch , bid them make hast . Enter Horatio and Marcellus . Fran . I thinke I heare them . Stand : who ' s there ? Hor . Friends to this ground Mar . And Leige - men to the Dane Fran . Giue you good night Mar . O farwel honest Soldier , who hath relieu ' d you ? Fra . Barnardo ha ' s my place : giue you goodnight . Exit Fran . Mar . Holla Barnardo Bar . Say , what is Horatio there ? Hor . A peece of him Bar . Welcome Horatio , welcome good Marcellus Mar . What , ha ' s this thing appear ' d againe to night Bar . I haue seene nothing Mar . Horatio saies , ' tis but our Fantasie , And will not let beleefe take hold of him Touching this dreaded sight , twice seene of vs , Therefore I haue intreated him along With vs , to watch the minutes of this Night , That if againe this Apparition come , He may approue our eyes , and speake to it Hor . Tush , tush , ' twill not appeare Bar . Sit downe a - while , And let vs once againe assaile your eares , That are so fortified against our Story , What we two Nights haue seene Hor . Well , sit we downe , And let vs heare Barnardo speake of this Barn . Last night of all , When yond same Starre that ' s Westward from the Pole Had made his course t ' illume that part of Heauen Where now it burnes , Marcellus and my selfe , The Bell then beating one Mar . Peace , breake thee of : Enter the Ghost . Looke where it comes againe Barn . In the same figure , like the King that ' s dead Mar . Thou art a Scholler ; speake to it Horatio Barn . Lookes it not like the King ? Marke it Horatio Hora . Most like : It harrowes me with fear & wonder Barn . It would be spoke too Mar . Question it Horatio Hor . What art'''
sent
from nltk.tokenize import word_tokenize

type(sent)
    
sent_token=word_tokenize(sent)
len(sent_token)

from nltk.probability import FreqDist

freq=FreqDist()

for words in sent_token:
    freq[words.lower()]+=1
freq

from nltk.util import bigrams,trigrams,ngrams

tok=word_tokenize(sent)
tok
bi=list(bigrams(sent))
bi
tri=list(trigrams(sent))
tri
sent_token
for token in sent_token:
    print(nltk.pos_tag(token))

