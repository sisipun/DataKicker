import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from util.constant import PLAYERS_COUNT


def get_kicker_data():
    df = pd.read_csv('../data/kicker_data.csv')

    y = df['red_won'].map({True: 1, False: 0})

    for i in range(1, PLAYERS_COUNT + 1):
        red_team_players = 'red_team_' + str(i)
        df[red_team_players] = np.where(df['red_team_p1_id'] == i, 1, np.where(df['red_team_p2_id'] == i, 1, 0))

    for i in range(1, PLAYERS_COUNT + 1):
        yellow_team_players = 'yellow_team_' + str(i)
        df[yellow_team_players] = np.where(df['yellow_team_p1_id'] == i, 1,
                                           np.where(df['yellow_team_p2_id'] == i, 1, 0))

    df.drop(['red_won', 'red_team_goals', 'yellow_team_goals', 'played_on', 'yellow_team_p1_id', 'yellow_team_p2_id',
             'red_team_p1_id', 'red_team_p2_id'], axis=1, inplace=True)
    x = df.values
    return x, y


def get_kicker_split_data():
    x, y = get_kicker_data()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=17)
    return x_train, x_test, y_train, y_test


def get_prediction_data(red_team_first_player, red_team_second_player, yellow_team_first_player,
                        yellow_team_second_player):
    df = pd.DataFrame(index=[0])

    for i in range(1, PLAYERS_COUNT + 1):
        red_team_players = 'red_team_' + str(i)
        df[red_team_players] = 1 if i == red_team_first_player or i == red_team_second_player else 0

    for i in range(1, PLAYERS_COUNT + 1):
        yellow_team_players = 'yellow_team_' + str(i)
        df[yellow_team_players] = 1 if i == yellow_team_first_player or i == yellow_team_second_player else 0

    return df.values
