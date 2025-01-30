chosen_year = int(input("Enter the year: "))

def is_leap_year(year):
    """Takes the year and decides wether it's a leap year or not"""
    if not year % 4 == 0:
        return False
    else:
        if not year % 100 == 0:
            return True
        else:
            if year % 400 == 0:
                return True
            else:
                return False

print(is_leap_year(chosen_year))

# a second way to define the function:
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(chosen_year))