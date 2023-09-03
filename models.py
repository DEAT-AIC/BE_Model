import numpy as np
# import tensorflow as tf
# import h5py
# from tensorflow.keras.models import Model
from gensim.models import Word2Vec

class models:
    def sinonim(self,kata):
        model_path = "my_model.bin"
        loaded_model = Word2Vec.load(model_path)
        print(loaded_model.summary())
        result = []

        if kata in loaded_model.key_to_index:
            print(f"Synonyms for '{word}':")
            synonyms = loaded_model.most_similar(word, topn=5)
            for synonym, score in synonyms:
                print(f"- {synonym} (score: {score:.2f})")
                temp = [synonym, f'{score:.2f}']
                result.append(temp)
            print("\n")
        else:
            print(f"'{word}' is not in the model's vocabulary.\n")

        return result