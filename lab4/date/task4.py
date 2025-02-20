from datetime import datetime
d1 = datetime.today()  
d2 = datetime(2025, 2, 19, 20, 30, 0)  # Feb 21 2025 at 20:30:00
#difference is 73006.322912

difference = d1 - d2
difference_in_seconds = difference.total_seconds()

print("Difference in seconds:", difference_in_seconds)