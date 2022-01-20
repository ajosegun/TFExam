import csv
import numpy as np
import os
import pandas as pd
import urllib.request


def retrieve_url(url, filename):
    if not os.path.exists(filename) and not os.path.isfile(filename):
        urllib.request.urlretrieve(url, filename)
    else:
        print(f'{filename} already exists! Nothing to download.')

def get_csv(filename):
    csv_data = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            csv_data.append(row)

    return csv_data

if __name__ == '__main__':
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/concrete/slump/slump_test.data'
    data_path = '../data'
    filename = f'{data_path}/concrete.csv'

    retrieve_url(url, filename)

    concrete_data = get_csv(filename)
    print(concrete_data[:5])

    concrete_df = pd.read_csv(filename)
    print(concrete_df.head(5))

    concrete_df_np = np.array(concrete_data[1:], dtype=float)
    print(concrete_df_np[:5])

    concrete_df_np = concrete_df.to_numpy()
    print(concrete_df_np[:5])

