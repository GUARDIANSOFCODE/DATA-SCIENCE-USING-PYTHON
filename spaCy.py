import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp("The quick brown fox jumps over the lazy dog")
for token in doc:
    print(token.text, token.pos_)
