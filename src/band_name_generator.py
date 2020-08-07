import numpy as np
import pandas as pd

words = pd.read_csv(r"C:\Users\Christian\Desktop\band_name_words.csv")

def pattern_1():
    adjective = get_adjective()
    noun = get_noun()

    print(adjective, noun)

def pattern_2():
    adjective_0 = get_adjective()
    noun_0 = get_noun()
    adjective_1 = get_adjective()
    noun_1 = get_noun()

    print(adjective_0, noun_0, adjective_1, noun_1)

def pattern_3():
    verb = get_verb()
    noun = get_noun()

    print('the', verb, noun)

def get_noun():
    noun = words.nouns.dropna().sample(n=1)
    noun = noun.values[0]

    return noun
    

def get_adjective():
    adjective = words.adjectives.dropna().sample(n=1)
    adjective = adjective.values[0]

    return adjective

def get_verb():
    verb = words.verbs.dropna().sample(n=1)
    verb = verb.values[0]

    return verb

print(pattern_1())
print(pattern_2())
print(pattern_3())







