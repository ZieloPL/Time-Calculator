def add_time(start, duration, day_of_week=''):
    hours = int(start.split(':')[0])
    minutes = int(start.split(':')[1][0:2])
    time_of_day = start[-2]

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    new_day = ''
    days_later = 0
    message = ''

    new_hours = int(duration.split(':')[0])
    new_minutes = int(duration.split(':')[1])

    if new_hours + hours >= 24:
        days_later = (new_hours + hours) // 24
        new_hours += hours - days_later * 24
    else:
        new_hours += hours

    if minutes + new_minutes >= 60:
        if new_hours == 11 and time_of_day == 'P':
            time_of_day = 'A'
            days_later += 1
        elif new_hours == 11 and time_of_day == 'A':
            time_of_day = 'P'
        new_hours += (minutes + new_minutes) // 60
        new_minutes = (minutes + new_minutes) % 60
    else:
        new_minutes += minutes

    if new_minutes <= 9:
        new_minutes = '0' + str(new_minutes)

    if new_hours > 12:
        if time_of_day == 'P':
            days_later += 1
        time_of_day = 'AM' if time_of_day == 'P' else 'PM'
        new_hours -= 12
    else:
        time_of_day += 'M'


    if days_later == 1:
        message = ' (next day)'
    elif days_later > 1:
        message = f' ({days_later} days later)'
    else:
        message = ''


    new_time = str(new_hours) + ':' + str(new_minutes) + ' ' + time_of_day

    if day_of_week != '':
        new_day = ', '+ days[(days.index(day_of_week.casefold().capitalize()) + days_later) % 7]
        new_time += new_day


    new_time += message
    return new_time

print(add_time('8:16 PM', '466:02', 'tuesday'))
