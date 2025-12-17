from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    df["error_flag"] = df["level"].apply(lambda x: 1 if x == "ERROR" else 0)

    model = IsolationForest(contamination=0.2, random_state=42)
    df["anomaly"] = model.fit_predict(df[["error_flag"]])

    return df
