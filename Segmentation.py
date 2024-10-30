import nltk
nltk.download('punkt')  # Downloading the necessary resources

from nltk.tokenize import sent_tokenize

text = "Hello! My name is Sankalp. I am learning NLP. It's fascinating!"
sentences = sent_tokenize(text)
print(sentences)
