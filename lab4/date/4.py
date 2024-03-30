from datetime import datetime

date1 = datetime(2023, 2, 20, 12, 0, 0)
date2 = datetime(2023, 2, 22, 18, 30, 15)

difference = abs((date2 - date1).total_seconds())

print("Difference in seconds:", difference)
