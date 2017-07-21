import os

stopword = ['alors', 'au', 'aucuns', 'aussi', 'autre', 'avant', 'avec',
            'avoir', 'bon', 'car', 'ce', 'cela', 'ces', 'ceux', 'chaque',
            'ci', 'comme', 'comment', 'dans', 'des', 'du', 'dedans', 'dehors',
            'depuis', 'devrait', 'doit', 'donc', 'dos', 'début', 'elle', 'elles',
            'en', 'encore', 'essai', 'est', 'et', 'eu', 'fait', 'faites', 'fois',
            'font', 'hors', 'ici', 'il', 'ils', 'je', 'juste', 'la', 'le', 'les',
            'leur', 'l', 'là', 'ma', 'maintenant', 'mais', 'mes', 'mine', 'moins',
            'mon', 'mot', 'même', 'ni', 'nommés', 'notre', 'nous', 'ou', 'où',
            'par', 'parce', 'pas', 'peut', 'plupart', 'pour', 'pourquoi', 'quand',
            'que', 'quel', 'quelle', 'quelles', 'quels', 'qui', 'sa', 'sans', 'ses',
            'seulement', 'si', 'sien', 'son', 'sont', 'sous', 'soyez', 'sujet', 'sur',
            'ta', 'tandis', 'tellement', 'tels', 'tes', 'ton', 'tous', 'tout', 'trop',
            'très', 'tu', 'voient', 'vont', 'votre', 'vous', 'vu', 'ça', 'étaient',
            'état', 'étions', 'été', 'être', 't', 'c', 's', 'd']

lem_dict = {}

def init_dic():
    global lem_dict
    print('Loading lem_dictionary')
    print('[', end='')
    for f in os.listdir('dico/'):
      print('.', end='')
      ofile = open('dico/' + f, "r", encoding='ISO-8859-1')
      a_lines = ofile.readlines()
      ofile.close()
      for line in a_lines:
        a_word = line.split('\t')
        lem_dict[a_word[0]] = a_word[1]
    print('] Done')

def find_ngram(a_text, n):
    return list(zip(*[a_text[i:] for i in range(n)]))

def ngrammize(a_text):
    d_gram = {}
    for n in range(2, 7):
      ngram = find_ngram(a_text, n)
      for gram in ngram:
        value = ' '.join(gram)
        if value in d_gram:
          d_gram[value] += 1
        else:
          d_gram[value] = 1
    return d_gram

def lemmizer(a_text):
   r_text = []
   for word in a_text:
     if word in lem_dict:
       r_text.append(lem_dict[word])
     else:
       r_text.append(word)
   return r_text

def rcheck(a_text):
   r_text = []
   for word in a_text:
     if word not in stopword:
       r_text.append(word)
   return r_text

def qcheck(text):
    text = text.lower()
    for ch in ['\n', '-', ';', '.', ',', '?', '!', '\'', '\"', ':', '(', ')']:
      if ch in text:
        text=text.replace(ch, ' ')
    a_text = text.split(' ')
    a_text = list(filter(bool, a_text))
    return a_text

def extract(textfile):
    f = open(textfile, "r", encoding='utf-8')
    text = f.read()
    f.close()
    return text

def generate_ngram(textfile):
    text = extract(textfile)
    a_text = qcheck(text)
    a_text = rcheck(a_text)
    a_text = lemmizer(a_text)
    d_gram = ngrammize(a_text)
    return d_gram

def merge_gram(n_gram1, n_gram2):
    for k, v in n_gram2.items():
      if k in n_gram1:
        n_gram1[k] += v
      else:
        n_gram1[k] = v
    return n_gram1
