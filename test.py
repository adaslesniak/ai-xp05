from uniform_subsampling import UniformSubsampler
from ordinary_subsampling import OrdinarySubsampler
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

nr_of_features = 16
# dummy data frame, I don't care about values
data = np.random.rand(1, nr_of_features) # Adjust the number of rows as needed
columns = [f'x{i+1}' for i in range(nr_of_features)]
df = pd.DataFrame(data, columns=columns)

ord_sampling = OrdinarySubsampler(df).subsets_with_normal_distribution()
uni_sampling = UniformSubsampler(df).subsets_with_uniform_distribution()


fig, axs = plt.subplots(1, 2, figsize=(15, 6))

ordinary_samples = [item for sublist in ord_sampling for item in sublist]
ordinary_samples = Counter(ordinary_samples)
axs[0].bar(ordinary_samples.keys(), ordinary_samples.values())
axs[0].set_title('Ordinary')

uni_samples = [item for sublist in uni_sampling for item in sublist]
uni_samples = Counter(uni_samples)
axs[1].bar(uni_samples.keys(), uni_samples.values())
axs[1].set_title('Uniform')

# Display the figure
plt.tight_layout()
plt.show()
