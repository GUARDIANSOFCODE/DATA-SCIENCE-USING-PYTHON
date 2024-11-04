import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def recognize_entities(text):
    # Process the text
    doc = nlp(text)
    
    # Extract entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

if __name__ == "__main__":
    text = "Apple is looking at buying U.K. startup for $1 billion."
    entities = recognize_entities(text)
    print("Named Entities, Phrases, and Concepts:")
    for entity in entities:
        print(entity)

