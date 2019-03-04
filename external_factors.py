
import pandas as pd
import statsmodels.api as sm


def main():
    pd.set_option('display.expand_frame_repr', False)
    df = pd.read_csv('data1000.csv', delimiter='%')

    for elem in df['country'].unique():
        df[str(elem)] = df['country'] == elem

    for elem in df['color'].unique():
        df[str(elem)] = df['color'] == elem

    for elem in df['wine_type'].unique():
        df[str(elem)] = df['wine_type'] == elem

    for elem in df['vintage'].unique():
        df['age'] = 2019 - df['vintage']

    for index, row in df.iterrows():
        if row['country'] in {"France", "Italy", "Spain", "Sicily"}:

            world = 'old'
        else:

            world = 'new'

        df.set_value(index, 'world', world)

    for elem in df['world'].unique():
        df[str(elem)] = df['world'] == elem

    Y = df[['score']]
    print_data(df)
    regress_colour(df, Y)
    regress_countries(df, Y)
    regress_type(df, Y)
    regress_vintage(df, Y)
    regress_model_1(df, Y)
    regress_model_2(df, Y)



def print_data(df):
    print(df)


def regress_countries(df, Y):
    print("\n\n\n\n-------------------COUNTRIES-------------------")
    X = df[['France', 'Italy', 'Argentina', 'New Zealand', 'Usa', 'Lebanon', 'Spain', 'Chile','Australia','South Africa', 'Germany', 'Sicily',]]
    # #super negligable
    model = sm.OLS(Y, X.astype(float)).fit()
    predictions = model.predict(X)
    print_model = model.summary()
    print(print_model)


def regress_colour(df, Y):
    print("\n\n\n\n-------------------COLOUR-------------------")
    X = df[['Red', 'White', 'Pink']]
    model = sm.OLS(Y, X.astype(float)).fit()
    predictions = model.predict(X)
    print_model = model.summary()
    print(print_model)


def regress_type(df, Y):
    print("\n\n\n\n-------------------TYPE-------------------")
    X = df[['sparkling', 'sweet', 'dry']]
    model = sm.OLS(Y, X.astype(float)).fit()
    predictions = model.predict(X)
    print_model = model.summary()
    print(print_model)
    # #actually a slight difference


def regress_vintage(df, Y):
    print("\n\n\n\n-------------------VINTAGE-------------------")
    X = df[['age']]
    model = sm.OLS(Y, X.astype(float)).fit()
    predictions = model.predict(X)
    print_model = model.summary()
    print(print_model)


def regress_model_1(df, Y):
    X = df[['Red', 'White', 'Pink','age','sparkling', 'sweet', 'dry',]]
    model = sm.OLS(Y, X.astype(float)).fit()
    predictions = model.predict(X)
    print_model = model.summary()
    print(print_model)


def regress_model_2(df, Y):
    X = df[['old', 'new', 'age']]
    model = sm.OLS(Y, X.astype(float)).fit()
    predictions = model.predict(X)
    print_model = model.summary()
    print(print_model)


main()
