from log_parser import parse_logs
from anomaly_detector import detect_anomalies
from report_generator import generate_report

df = parse_logs("../logs/sample_test.log")
df = detect_anomalies(df)
generate_report(df)
