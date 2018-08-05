import xgboost as xgb
from data.kicker_data import get_kicker_data

xgb_params = {'booster': 'gbtree', 'max_depth': 3, 'eta': 0.1,
              'silent': 1, 'objective': 'binary:logistic', 'nthread': 4}


def xg_boost():
    x, y = get_kicker_data()
    return xgb.train(xgb_params, xgb.DMatrix(x, label=y),
                     num_boost_round=100)
