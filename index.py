import pickle
from collections import defaultdict
from os import path
import gzip

from preprocessing import tokenize_stem, count_tokens, max_count_token

from load_dataset import load_wikidata, clean_wikidata


_filename = path.join("databases", "pokemon_pages_current.json.gz")

def indexing(filename):
    index = defaultdict(dict)

    for doc_no, doc in enumerate(load_wikidata(filename)):
        tokens = tokenize_stem(clean_wikidata(doc["text"]))
        if len(tokens) == 0:
            continue
        token_counts = count_tokens(tokens)
        max_token_count = max_count_token(token_counts)
        token_set = token_counts.keys()
        for token in token_set:
            tf = token_counts[token] / max_token_count
            index[token][doc_no] = tf
    return index


def save_build_index(filename_index):
    index = indexing(_filename)
    with open(filename_index, "wb") as file:
        pickle.dump(index, file)
    return index


def save_build_titles(filename_titles):
    doc_titles = [doc["title"] for doc in load_wikidata(_filename)]
    with open(filename_titles, "wb") as file:
        pickle.dump(doc_titles, file)
    return doc_titles


def load_index(filename_index):
    if filename_index.endswith(".gz"):
        return load_index_gzip(filename_index)
    else:
        return load_index_normal(filename_index)


def load_index_gzip(filename_index):
    index = defaultdict(dict)
    if path.isfile(filename_index):
        with gzip.open(filename_index, "rb") as file:
            index = pickle.load(file)
    else:
        print("File not found; building index")
#        index = save_build_index(filename_index)
    return index


def load_index_normal(filename_index):
    index = defaultdict(dict)
    if path.isfile(filename_index):
        with open(filename_index, "rb") as file:
            index = pickle.load(file)
    else:
        print("File not found; building index")
#        index = save_build_index(filename_index)
    return index


def load_titles(filename_titles):
    doc_titles = []
    if path.isfile(filename_titles):
        with open(filename_titles, "rb") as file:
            doc_titles = pickle.load(file)
    else:
        print("File not found; building titles")
        doc_titles = save_build_titles(filename_titles)
    return doc_titles
