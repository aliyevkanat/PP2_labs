from datetime import datetime, timedelta

current_date = datetime.today()
new_date = current_date - timedelta(days=5)

print("Current Date:", current_date.date())
print("Date 5 Days Ago:", new_date.date())
