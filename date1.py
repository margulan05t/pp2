from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)

print("Five days ago from today:", five_days_ago)
