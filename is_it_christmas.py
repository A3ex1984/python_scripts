

def check_date (day,month, year):
    day_diff = 0
    if day == 24 and month == 12:
        return "It is Christmas today"
    else:
        if month < 12: #Check wether it is a previous month
            day_diff = (12 - month)*30 #Assuming 30 days in a month
            day_diff += 24 - day
        else: #Check wether it is a previous day
            day_diff += 24 - day
        return "It is not Christmas. It still is {} days until Christmas".format(day_diff)

print (check_date(23,12,12))