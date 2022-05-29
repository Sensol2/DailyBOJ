from datetime import datetime, timedelta, timezone

print(datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d"))
