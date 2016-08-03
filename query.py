from collections import defaultdict
import math

from index import load_index, load_titles, save_build_index
from preprocessing import tokenize_stem

index = defaultdict(dict)


def and_query():
    while True:
        query_tokens = tokenize_stem(input("Query: "))
        results = [doc_no for doc_no in index[query_tokens[0]]]
        results_titles = [doc_titles[_no] for _no in results]

        for number, title in zip(results, results_titles):
            print(number, title)
        print(len(results), len(results_titles))


def or_query(query, dataset="smallwiki"):
    doc_titles = load_titles("smallwikititles.pickle")
    N = len(doc_titles)
    index = load_index("smallwikiindex.pickle")

    # while True:
    # query_tokens = tokenize_stem(input("Query: "))
    query_tokens = tokenize_stem(query)

    all_docs = []
    for token in query_tokens:
        all_docs += index[token]
    all_docs = set(all_docs)

    stemmed_titles = {doc_no: tokenize_stem(doc_titles[doc_no]) for doc_no in all_docs}

    doc_scores = {}
    idf_values = {token: math.log(N / len(index[token])) for token in query_tokens}
    for doc_no in all_docs:
        score = 0
        for token in set(query_tokens):
            if doc_no in index[token]:
                tf = index[token][doc_no]
                idf = idf_values[token]
                score += tf * idf
            if token in stemmed_titles:
                tf = 15
                idf = idf_values[token]
                score += tf * idf
        doc_scores[doc_no] = score


    ranked_docs = sorted(doc_scores, key=doc_scores.get, reverse=True)
    total_results = [doc_titles[doc_no] for doc_no in ranked_docs]
    # print(len(total_results))
    # print(total_results[:10])
    # print(len(ranked_docs))

    return (total_results[:10])

if __name__ == "__main__":
    doc_titles = load_titles("smallwikititles.pickle")
    N = len(doc_titles)
    index = load_index("smallwikiindex.pickle")
    print(N)

#or_query()

