import spacy

# Load English tokenizer, POS tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

text = "Sankalp is learning Natural Language Processing."

# Process the text
doc = nlp(text)

# Display dependency parsing
for token in doc:
    print(f"{token.text} -> {token.dep_} -> {token.head.text}")
