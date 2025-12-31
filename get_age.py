from datetime import date #For getting current date

#Comparing current year with model year to get age
def years_since (year_in):
    now = date.today()
    now_year = now.year
    age = int(now_year)-int(year_in)
    return age