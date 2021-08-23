"""
This module contains functions to train word embeddings on an input corpus.
"""
from gensim.models import Word2Vec
from WordVectors import WordVectors
from nltk.tokenize import word_tokenize
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_corpus", type=str, help="Path to input corpus (sentencized)")
    parser.add_argument("output", type=str, help="Output embedding path")
    parser.add_argument("--vector_size", type=int, default=100, help="Size of embedding vectors")
    parser.add_argument("--window", type=int, default=5, help="Size of context windows")
    parser.add_argument("--min_count", type=int, default=20, help="Minimum word count")
    parser.add_argument("--workers", type=int, default=64, help="No. of worker threads")

    args = parser.parse_args()
    path_in = args.input_corpus
    path_out = args.output

    w2v_params = {
        "vector_size": args.vector_size,
        "window": args.window,
        "min_count": args.min_count,
        "workers": args.workers
    }

    print("Reading corpus...")
    with open(path_in) as fin:
        sentences = [word_tokenize(s) for s in fin.readlines()]

    print("Training...")
    model = Word2Vec(sentences=sentences, **w2v_params)
    wv = WordVectors(words=model.wv.index_to_key, vectors=model.wv.vectors)

    wv.save_txt(path_out)


if __name__ == "__main__":
    main()

