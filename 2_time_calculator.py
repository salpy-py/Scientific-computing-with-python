def add_time(start, duration, wk_day=None):
    # -------- INITIALISING --------
    # to seperate hours and minutes for mathematical operations
    start_space = start.find(' ')
    start_colon = start.find(':')
    duration_col_seperate = duration.find(':')

    # initialising 'start' hours and minutes in integers
    start_hour = int(start[:start_colon])
    start_minutes = int(start[start_colon + 1: start_space])

    # initialising 'duration' hours and minutes in integers
    duration_hour = int(duration[:duration_col_seperate])
    duration_minutes = int(duration[duration_col_seperate + 1:])

    # initialising AM/PM
    day_session = start[start_space + 1:]

    # ------------------------------------------------------------------------

    def day_cycle(days):
        half_day = [0]
        day = 0
        cycle_list = []
        for i in range(days * 2):
            day += 12
            half_day.append(day)
        x = 0
        y = 1
        for __ in half_day:
            if x > len(half_day) or y > len(half_day):
                break
            if x >= len(half_day) - 1:
                am = str(half_day[-1]) + ' AM'
                cycle_list.append(am)
            else:
                am = str(half_day[x]) + ' AM'
                cycle_list.append(am)
                if y >= len(half_day):
                    break
                pm = str(half_day[y]) + ' PM'
                cycle_list.append(pm)
            x += 2
            y += 2
        cycle_list.pop(0)
        return cycle_list

    def week_cycle(num):
        wk_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        new_lst = list()
        for __ in range(num):
            new_lst += wk_days
        return new_lst

    total_hrs = start_hour + duration_hour
    total_mins = start_minutes + duration_minutes
    if day_session == 'PM' and start_hour >= 1 and start_hour < 12:
        total_hrs += 12
    if day_session == 'AM' and start_hour == 12:
        total_hrs -= 12
    if total_mins >= 60:
        total_mins = total_mins - 60
        total_hrs += 1

    if total_hrs == 0:
        total_days = 1.0
        x = total_days
    else:
        total_days = total_hrs / 24
    if total_hrs == 24 and day_session == 'PM':
        x = total_days + 1
    elif total_hrs == 24 and day_session == 'AM':
        x = total_days + 1
    else:
        x = total_days
    str_x = str(x)
    decimal_index = str_x.find('.')
    if int(str_x[decimal_index + 1:]) == 0 and total_hrs == 24:
        total_days = int(str_x[:decimal_index])
    else:
        total_days = int(str_x[:decimal_index]) + 1
    actual_days = total_days - 1

    if actual_days < 7:
        weeks = 1
    else:
        weeks = actual_days / 7
        x = weeks
        str_x = str(x)
        decimal_index = str_x.find('.')
        if int(str_x[decimal_index + 1:]) != 0:
            weeks = int(str_x[:decimal_index]) + 1
        else:
            weeks += 1

    if wk_day is None:
        pass
    elif wk_day != '':
        week_list = week_cycle(int(weeks))

        if actual_days == 0:
            wk_day = wk_day.capitalize()
        else:
            if wk_day.capitalize() in week_list:
                i = -1
                for x in week_list:
                    i += 1
                    if x == wk_day.capitalize():
                        break
                if duration_hour == 0:
                    wk_day = wk_day.capitalize()
                else:
                    c = week_list.count(week_list[i])
                    c = (7 * c) - 1
                    n = -1
                    if i == 0:
                        c = actual_days - c - i
                    elif i == 1:
                        c = (actual_days - c - i) + 1
                    elif i == 2:
                        c = (actual_days - c - i) + 3
                    elif i == 3:
                        c = (actual_days - c - i) + 5
                    elif i == 4:
                        c = (actual_days - c - i) + 7
                    elif i == 5:
                        c = (actual_days - c - i) + 9
                    elif i == 6:
                        c = (actual_days - c - i) + 11
                    elif i == 7:
                        c = (actual_days - c - i) + 13
                    answer_week = week_list[c]

    # -----------------------------------------------------------------
    new_day = day_cycle(total_days)
    space_ind = new_day[-2].find(' ')
    # -----------------------------------------------------------------

    if total_hrs < 12:
        day_session = new_day[-1][space_ind + 1:]
        new_hour = total_hrs
        if new_hour == 0:
            new_hour = 12
        if wk_day:
            new_time = str(new_hour) + ':' + str(f'{total_mins:02d}') + ' ' + day_session + ', ' + wk_day.capitalize()
        else:
            new_time = str(new_hour) + ':' + str(f'{total_mins:02d}') + ' ' + day_session

    elif total_hrs >= 12 and total_hrs < 24:
        day_session = new_day[-2][space_ind + 1:]
        new_hour = total_hrs - int(new_day[-2][:space_ind])
        if new_hour == 0:
            new_hour = 12
        if wk_day:
            new_time = str(new_hour) + ':' + str(f'{total_mins:02d}') + ' ' + day_session + ', ' + wk_day.capitalize()
        else:
            new_time = str(new_hour) + ':' + str(f'{total_mins:02d}') + ' ' + day_session

    elif total_hrs < int(new_day[-2][:space_ind]):
        day_session = new_day[-1][space_ind + 1:]
        new_hour = total_hrs - int(new_day[-3][:space_ind])
        if new_hour == 0:
            new_hour = 12
        if actual_days == 1:
            answer_day = ' (next day)'
        else:
            answer_day = f' ({actual_days} days later)'
        if wk_day:
            new_time = str(new_hour) + ':' + str(
                f'{total_mins:02d}') + ' ' + day_session + ', ' + answer_week + answer_day
        else:
            new_time = str(new_hour) + ':' + str(f'{total_mins:02d}') + ' ' + day_session + answer_day

    elif total_hrs >= int(new_day[-1][:space_ind]):
        day_session = new_day[-1][space_ind + 1:]
        new_hour = int(total_hrs) - int(new_day[-2][:space_ind])
        if new_hour == 0:
            new_hour = 12
        if actual_days == 1:
            answer_day = ' (next day)'
        else:
            answer_day = f' ({actual_days} days later)'
        if wk_day:
            new_time = str(new_hour) + ':' + str(
                f'{total_mins:02d}') + ' ' + day_session + ', ' + answer_week + answer_day
        else:
            new_time = str(new_hour) + ':' + str(f'{total_mins:02d}') + ' ' + day_session + answer_day

    elif total_hrs >= int(new_day[-2][:space_ind]):
        day_session = new_day[-2][space_ind + 1:]
        new_hour = int(total_hrs) - int(new_day[-2][:space_ind])
        if new_hour == 0:
            new_hour = 12
        if actual_days == 1:
            answer_day = ' (next day)'
        else:
            answer_day = f' ({actual_days} days later)'
        if wk_day:
            new_time = str(new_hour) + ':' + str(
                f'{total_mins:02d}') + ' ' + day_session + ', ' + answer_week + answer_day
        else:
            new_time = str(new_hour) + ':' + str(f'{total_mins:02d}') + ' ' + day_session + answer_day


    else:
        if total_hrs == 0:
            total_hrs = 12
        if actual_days == 1:
            answer_day = ' (next day)'
        else:
            answer_day = f' ({actual_days} days later)'
        if wk_day:
            new_time = str(total_hrs) + ':' + str(
                f'{total_mins:02d}') + ' ' + day_session + ', ' + answer_week + answer_day
        else:
            new_time = str(total_hrs) + ':' + str(f'{total_mins:02d}') + ' ' + day_session + answer_day

    print(new_time)
    return new_time


actual = add_time("8:16 PM", "466:02", "tuesday")
expected = "6:18 AM, Monday (20 days later)"