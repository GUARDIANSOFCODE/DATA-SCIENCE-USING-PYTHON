import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
sentence = "The quick brown fox jumps over the lazy dog"
words = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(words)
print(tagged)
