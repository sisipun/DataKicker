from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from data.kicker_data import get_kicker_data


def log_regression():
    x, y = get_kicker_data()
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    lr = LogisticRegression(C=1)
    lr.fit(x_scaled, y)
    return lr
