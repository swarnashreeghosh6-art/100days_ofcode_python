def leap_year(year):
    """This tells us whether a year is leap year or not"""
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(leap_year(2026))
