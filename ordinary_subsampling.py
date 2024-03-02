import numpy as np
import pandas as pd
import random

class OrdinarySubsampler:
    def __init__(self, data:pd.DataFrame):    
        self._features = data.columns.tolist()


    def subsets_with_normal_distribution(self, nr_of_subsets=100, features_per_subset = None):
        if features_per_subset is None:
            features_per_subset = int(np.ceil(np.sqrt(len(self._features))))
        subsets = []
        for _ in range(nr_of_subsets):
            next_subset = random.sample(self._features, features_per_subset)
            subsets.append(next_subset)
        return subsets