import spacy
nlp = spacy.load("ru_core_news_sm")

with open("kustsireni.txt", encoding="utf-8") as f:
    text = f.read()

doc = nlp(text)

def get_all_tokens(doc):
    return [token.text for token in doc]

all_tokens = get_all_tokens(doc)

print("Все токены:", get_all_tokens(doc))