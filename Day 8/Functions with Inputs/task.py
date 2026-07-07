def life_in_weeks(age):
    years_left=90-age
    days_left=years_left*365
    weeks_left=int(days_left/7)
    print(f"You have {weeks_left} weeks left.")
age=int(input("What is ur age? "))
life_in_weeks(age)