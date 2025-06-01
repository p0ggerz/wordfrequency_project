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

def lemmatize_tokens(token_objects):
    return [token.lemma_ for token in token_objects]

def count_frequency(items):
    return {item: items.count(item) for item in items}

def sort_freq_dct(freq):
    wordfreq_lst = list(freq.items())
    wordfreq_lst_sorted = sorted(wordfreq_lst, key=lambda x: (-x[1], x[0]))
    return wordfreq_lst_sorted


all_tokens = get_all_tokens(doc)
token_objects = filter_token_objects(doc)
filtered_tokens = convert_token_objects_to_lowercase(token_objects)
lemmas = lemmatize_tokens(token_objects)
freq = count_frequency(lemmas)
wordfreq_sorted = sort_freq_dct(freq)

n = int(input("Введите количество слов для подсчета их частотности: "))
print(f"Топ-{n} частотных слов:")
for lemma, count in wordfreq_sorted[:n]:
    print(f"{lemma}: {count} раз(а)")

print("Все токены:", all_tokens)
print("Токены без стоп-слов (нижний регистр):", filtered_tokens)
print("Леммы:", lemmas)
print("Частотность слов:", freq)
print("Отсортированные по частотности слова:", wordfreq_sorted)