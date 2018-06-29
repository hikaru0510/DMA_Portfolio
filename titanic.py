import numpy as np
import tflearn
from tflearn.datasets import titanic

tav = 0
c = 0

aav = 0
ca = 0
titanic.download_dataset('titanic_dataset.csv')
from tflearn.data_utils import load_csv
data, labels = load_csv('titanic_dataset.csv', target_column=0, categorical_labels=True, n_classes=2,
                        columns_to_ignore=[7])

for fare in data: # average fare
    tav += float(fare[6])
    c += 1
    av = tav / c
    print(av)

for age in data: # average age
    aav += float(age[3])
    ca += 1;
    avv = aav / ca
    print(avv)