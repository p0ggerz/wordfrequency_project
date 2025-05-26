import spacy
nlp = spacy.load("ru_core_news_sm")

with open("kustsireni.txt", encoding="utf-8") as f:
    text = f.read()

doc = nlp(text)

def get_all_tokens(doc):
    return [token.text for token in doc]

def filter_token_objects(doc):
    return [token for token in doc if token.is_alpha and not token.is_stop and not token.ent_type_]

def convert_token_objects_to_lowercase(token_objects):
    return [token.lower_ for token in token_objects]


all_tokens = get_all_tokens(doc)
token_objects = filter_token_objects(doc)
filtered_tokens = convert_token_objects_to_lowercase(token_objects)

print("Все токены:", get_all_tokens(doc))
print("Токены без стоп-слов (нижний регистр):", filtered_tokens)