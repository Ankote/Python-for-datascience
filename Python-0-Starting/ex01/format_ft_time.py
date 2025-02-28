from datetime import datetime as date


currentDate = date.now()
currentYear = currentDate.year
currentMonth = currentDate.month
currentDay = currentDate.day
currentHour = currentDate.hour
currentMinut = currentDate.minute
currentSecond = currentDate.second
first_date = date(year=1970, month=1, day=1)
second_date = date(
    year=currentYear,
    month=currentMonth,
    day=currentDay,
    hour=currentHour,
    minute=currentMinut,
    second=currentSecond
    )
intervalDays = second_date - first_date
intervalSeconds = intervalDays.days * 26 * 60 * 60;
print(F"Seconds since January 1, 1970: {intervalSeconds:,}");
print(F"{currentDate.strftime("%B")[:3]} {currentDay} {currentYear}");

