import xgboost as xgb
from sklearn.metrics import accuracy_score
from data.kicker_data import get_kicker_split_data
import math

X_train, X_test, y_train, y_test = get_kicker_split_data()
xgb_params = {'booster': 'gbtree', 'max_depth': 3, 'eta': 0.1,
              'silent': 1, 'objective': 'binary:logistic', 'nthread': 4}

bst = xgb.train(xgb_params, xgb.DMatrix(X_train, label=y_train),
                num_boost_round=100)

bst_pred = bst.predict(xgb.DMatrix(X_test))
print(accuracy_score(y_test, [math.fabs(round(i)) for i in bst_pred]))
