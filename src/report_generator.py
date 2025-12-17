def generate_report(df):
    total = len(df)
    errors = df[df["level"] == "ERROR"].shape[0]
    anomalies = df[df["anomaly"] == -1].shape[0]

    print("===== Test Quality Report =====")
    print(f"Total log entries: {total}")
    print(f"Errors detected: {errors}")
    print(f"Anomalies detected: {anomalies}")

    if anomalies:
        print("⚠️ Investigation recommended")
    else:
        print("✅ Test execution normal")
