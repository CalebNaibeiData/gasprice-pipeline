import pandas as pd

def transform_data(raw_data):
    df = pd.json_normalize(raw_data['result']['cities'])

    # standardize columns
    df.columns = df.columns.str.lower()

    # select + rename + clean
    df = df.rename(columns={"name": "cities"})

    df = df[[
        "cities",
        "currency",
        "gasoline",
        "midgrade",
        "premium",
        "diesel"
    ]]

    return df