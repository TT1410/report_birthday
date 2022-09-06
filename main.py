from datetime import datetime, timedelta
from copy import deepcopy


WEEK = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}


def get_birthdays_per_week(users: list) -> None:
    today = datetime.now()  # сьогоднішня дата

    start_current_week = (today - timedelta(2 + today.weekday()))  # дата початку цього тижня (не з понеділка, а з суботи минулого)
    end_current_week = (today + timedelta(4 - today.weekday()))  # дата кінця поточного тижня (п'ятниця)
    end_next_week = (today + timedelta(4 - today.weekday() + 7))  # дата кінця наступного тижня (п'ятниця)

    this_week = deepcopy(WEEK)
    next_week = deepcopy(WEEK)

    for user in users:
        birthday: datetime = user["birthday"].replace(year=today.year)

        if datetime(today.year, 1, 7) >= today:
            if birthday.month == 12 and birthday > datetime(today.year, 1, 1):
                birthday = birthday.replace(year=today.year-1)

        elif datetime(today.year, 12, 24) <= today:
            if birthday.month == 1 and birthday > datetime(today.year, 1, 1):
                birthday = birthday.replace(year=today.year+1)

        if (birthday >= start_current_week) and (birthday <= end_next_week):
            name_weekday = "Monday" if birthday.weekday() in (5, 6) else birthday.strftime("%A")

            if birthday < end_current_week:
                this_week[name_weekday].append(user['name'])

            else:
                next_week[name_weekday].append(user['name'])

    report_birthday(
        this_week,
        next_week,
        "{} - {}".format(start_current_week.strftime("%d.%m.%Y"), end_current_week.strftime("%d.%m.%Y")),
        "{} - {}".format(end_current_week.strftime("%d.%m.%Y"), end_next_week.strftime("%d.%m.%Y"))
    )


def report_birthday(this_week: dict, next_week: dict, this_dates: str, next_dates: str) -> None:
    this_week = ["{:<11}: {}".format(day, ', '.join(names)) for day, names in this_week.items() if names]
    next_week = ["{:<11}: {}".format(day, ', '.join(names)) for day, names in next_week.items() if names]

    if this_week:
        print(this_dates)

        for day in this_week:
            print(day)

    if next_week:
        print('\n' + next_dates)

        for day in next_week:
            print(day)


USERS = [
    {
        "name": "Taras",
        "birthday": datetime(1999, 9, 7)
    },
    {
        "name": "Olha",
        "birthday": datetime(1999, 9, 10)
    },
    {
        "name": "Iryna",
        "birthday": datetime(1994, 9, 16)
    },
    {
        "name": "Maksym",
        "birthday": datetime(1997, 9, 8)
    },
    {
        "name": "Dmytro",
        "birthday": datetime(1993, 1, 2)
    },
    {
        "name": "Ivan",
        "birthday": datetime(2000, 12, 31)
    }
]


if __name__ == '__main__':
    get_birthdays_per_week(USERS)
