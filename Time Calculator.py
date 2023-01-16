def add_time(origin: str, added: str, days=""):
    weekDays = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    )
    list_origin = origin.split(" ")
    list_added = added.split(" ")
    origin_hours = list_origin[0].split(":")[0]
    origin_min = list_origin[0].split(":")[1]
    added_hours = list_added[0].split(":")[0]
    added_min = list_added[0].split(":")[1]
    result_hours = int(origin_hours) + int(added_hours)
    result_min = int(origin_min) + int(added_min)
    result_periods = list_origin[1]
    num_ofdays_rest = result_hours / 24
    result_days = ""
    if result_hours < 12:
        num_ofdays_rest -= 1
    if type(num_ofdays_rest) == float and num_ofdays_rest > 1:
        num_ofdays_rest = int(num_ofdays_rest) + 1
    else:
        num_ofdays_rest = 0
    if result_min >= 60:
        result_min = result_min % 60
        result_hours += 1
    if result_hours > 12 or (result_hours == 12 and result_min > 0):
        result_hours = result_hours % 12
        if result_periods == "AM":
            result_periods = "PM"
        else:
            result_periods = "AM"
    if result_hours == 0:
        result_hours = 12
    print(result_hours)
    result_time = f"{str(result_hours)}:{str(result_min).rjust(2,'0')} {result_periods}"
    if days.capitalize() in weekDays:
        result_days += ","
        index_main_day = weekDays.index(days.capitalize())
        if (index_main_day + num_ofdays_rest) > len(weekDays):
            result_days += (
                f" {weekDays[(index_main_day+round(num_ofdays_rest)) - len(weekDays)]}"
            )
        else:
            result_days += f" {weekDays[index_main_day+round(num_ofdays_rest)]}"

    if num_ofdays_rest > 0:
        if num_ofdays_rest == 1:
            result_days += f" (next day)"
        else:
            result_days += f" ({num_ofdays_rest} days later)"
    # print(num_ofdays_rest)
    return result_time + result_days


# print(add_time("6:30 PM", "205:12"))
# print(add_time("11:43 PM", "24:20", "tueSday"))
# print(add_time("11:30 AM", "2:32","Monday"))
print(add_time("11:40 AM", "0:25"))
