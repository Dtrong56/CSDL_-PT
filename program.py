import os
import string
import math

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
print("TermTable:")
print(index)
print("\nDocTable:")
print(doctable)
#Start Câu a
print("End Câu a!")

# Start Câu b 
print("\nStart Câu b:")

def calculate_idf(word, term_table, doc_table):
    total_docs = len(doc_table)
    docs_with_term = len(term_table[word])
    return math.log(total_docs / docs_with_term) if docs_with_term > 0 else 0

def Find(Word, Weight, N):
    Word = Word.lower()
    if Word not in index:
        print(f"'{Word}' not found in the index.")
        return []

    scores = {}
    idf = calculate_idf(Word, index, doctable)

    for doc_name, tf in index[Word].items():
        score = tf * Weight * idf
        scores[doc_name] = score

    top_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:N]

    print(f"Top {N} documents for word '{Word}' (weight={Weight}):")
    for doc, score in top_docs:
        print(f"  {doc}: {score:.4f}")

    return top_docs

# Ví dụ chạy thử câu b:
Find("cat", 2, 3)
print("End Câu b!")



#Start Câu c
print("\nStart Câu c:")
def calculate_idf(word, index, doc_table):
    total_docs = len(doc_table)
    docs_with_term = len(index[word])
    return math.log(total_docs / docs_with_term) if docs_with_term > 0 else 0

def Find(WordFile, N):
    # Read query terms from file
    query_terms = {}
    with open(WordFile, 'r', encoding='utf-8') as file:
        for line in file:
            word, weight = line.strip().split()
            query_terms[word.lower()] = int(weight)
    
    # Calculate scores for each document
    doc_scores = {}
    for word, weight in query_terms.items():
        if word in index:  # using global index
            for doc_name, tf in index[word].items():
                idf = calculate_idf(word, index, doctable)  # using global doctable
                score = tf * idf * weight
                
                if doc_name not in doc_scores:
                    doc_scores[doc_name] = 0
                doc_scores[doc_name] += score
    
    # Sort and get top N documents
    return sorted(doc_scores.items(), key=lambda x: x[1], reverse=True)[:N]

# Test the function
wordfile_path = "query/query.txt"  # Đường dẫn đến file query
N = 3  # Số lượng document cần trả về
results = Find(wordfile_path, N)
print(f"\nTop {N} matching documents:")
for doc, score in results:
    print(f"Document: {doc}, Score: {score:.2f}")
print("End Câu c!")