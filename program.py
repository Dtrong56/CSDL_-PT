import os
import string

#Start Câu a
print("Start Câu a:")
def load_stopwords(stoplist_path):
    with open(stoplist_path, 'r', encoding='utf-8') as f:
        return set(word.strip().lower() for word in f.readlines())

def tokenize(text):
    # Tách từ, loại bỏ dấu câu
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator).lower().split()

def CreateIndex(Dir, StopList):
    stoplist_path = os.path.join(Dir, StopList)
    stopwords = load_stopwords(stoplist_path)

    inverted_index = {}
    doc_table = {}
    doc_id = 0

    for filename in os.listdir(Dir):
        if filename == StopList:
            continue
        filepath = os.path.join(Dir, filename)
        if os.path.isfile(filepath):
            # Ghi nhận vào DocTable
            doc_table[doc_id] = filename
            doc_id += 1

            with open(filepath, 'r', encoding='utf-8') as f:
                words = tokenize(f.read())
                for word in words:
                    if word in stopwords:
                        continue
                    if not word.lower().startswith('c'):  # xử lý cả chữ C hoa/thường
                        continue
                    if word not in inverted_index:
                        inverted_index[word] = {}
                    if filename not in inverted_index[word]:
                        inverted_index[word][filename] = 0
                    inverted_index[word][filename] += 1

    return inverted_index, doc_table

index, doctable = CreateIndex("documents", "stoplist.txt")
print("Inverted Index:")
print(index)
print("\nDocTable:")
print(doctable)

#Start Câu a
print("End Câu a!")