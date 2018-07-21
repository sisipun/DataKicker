import pandas as pd
from sklearn.model_selection import train_test_split


def get_kicker_data():
    df = pd.read_csv('kicker.csv')

    y = df['red_won']
    df.drop(['red_won', 'red_team_goals', 'yellow_team_goals'], axis=1, inplace=True)
    df = pd.get_dummies(df, columns=['red_team_p1_id', 'red_team_p2_id', 'yellow_team_p1_id', 'yellow_team_p2_id'])
    x = df.values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=17)
    return x_train, x_test, y_train, y_test
