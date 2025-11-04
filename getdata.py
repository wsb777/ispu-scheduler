from testdata import test_request,test_time
from datetime import datetime, timedelta,date

days = ["monday", "thuesday", "wednesday", "thuersday", "friday", "saturday", "sunday"]

def getDay(text:str) -> str:
    match text:
        case "ПН":
            return "monday"
        case "ВТ":
            return "thuesday"
        case "СР":
            return "wednesday"
        case "ЧТ":
            return "thuersday"
        case "ПТ":
            return "friday"
        case "СБ":
            return "saturday"
        
def calculateDate(count_from_day) -> tuple[int, str]:
    today = date.today() + timedelta(days=count_from_day)
    week_day = days[today.weekday()]
    date_for_first_week = datetime.strptime(test_request["date_for_first_week"], '%d.%m.%Y').date()
    difference = today - date_for_first_week
    circle = difference.days / 14
    circle = circle - int(circle)
    if circle < 0.5:
        week = 0
    else: 
        week=1
    print(f"{week}  -  {week_day}")
    return week, week_day
        
def getMessage(week:int,day :str) -> str:
    message = "Расписание:"
    if test_request["data"][week][day] is None or day == "sunday":
        message += "\n\nНа данный день расписание у группы отсутствует"
    else:
        for lesson_time in test_request["data"][week][day]:
            time = test_time[lesson_time]
            lesson = test_request["data"][week][day][lesson_time]
            message += f"\n\n{time}:\n{lesson}"
    return message