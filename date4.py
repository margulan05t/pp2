from datetime import datetime

def date_difference_in_seconds(date1, date2):
    difference = abs(date1 - date2)
    return difference.total_seconds()

date1 = datetime(2023, 1, 1, 12, 0, 0) 
date2 = datetime(2023, 1, 2, 12, 0, 0)  

difference_seconds = date_difference_in_seconds(date1, date2)
print("Difference between dates in seconds:", difference_seconds)
