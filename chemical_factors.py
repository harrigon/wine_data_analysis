import pandas as pd
import statsmodels.api as sm


def red_wine_analysis():
    pd.set_option('display.expand_frame_repr', False)
    df = pd.read_csv('winequality-red.csv', delimiter=';')

    print_data(df)

    Y = df[['quality']]
    X = df[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']]
    model = sm.OLS(Y, X.astype(float)).fit()
    predictions = model.predict(X)
    print_model = model.summary()
    print(print_model)

def white_wine_analysis():
    pd.set_option('display.expand_frame_repr', False)
    df = pd.read_csv('winequality-white.csv', delimiter=';')

    print_data(df)

    Y = df[['quality']]
    X = df[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']]
    model = sm.OLS(Y, X.astype(float)).fit()
    predictions = model.predict(X)
    print_model = model.summary()
    print(print_model)


def print_data(df):
    print(df)

white_wine_analysis()



red_wine_analysis()
white_wine_analysis()
