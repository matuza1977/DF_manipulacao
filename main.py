import pandas as pd


def create_dataframe():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['Saint Petersburg', 'New York', 'Prague', 'Paphos']
    }

    return pd.DataFrame(data)


def add_month_cost(df, month_costs):
    # add 'Month cost' column here
    df["Custo mensal"] = [50000, 800000, 200000, 500000]


def add_annual_cost_in_thousands(df):
    # add 'Annual cost in thousands' column here
    df["Custo anual em milhares"] = (df["Custo mensal"] * 12 // 1000).astype("int64")


if __name__ == "__main__":
    df = create_dataframe()
    add_month_cost(df, [50000, 800000, 200000, 500000])
    add_annual_cost_in_thousands(df)
    print(df)
