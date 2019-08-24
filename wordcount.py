import itertools
from collections import Counter



def word_counter(dataframe):
    l = [message.split() for message in dataframe]
    l_combined = list(itertools.chain.from_iterable(l))
    l_count = Counter(l_combined)
    return l_count
