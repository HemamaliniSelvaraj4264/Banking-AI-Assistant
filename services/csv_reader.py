import pandas as pd

def read_csv(upload_file):
    data = pd.read_csv(upload_file)
    return data

