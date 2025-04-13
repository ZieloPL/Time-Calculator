def add_time(start, duration, day_of_week=''):
    # Parse start time
    start_hour, start_minute = map(int, start[:-3].split(':'))
    period = start[-2]

    # Parse duration
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Days of the week
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Calculate total minutes
    total_minutes = start_minute + duration_minute
    extra_hours = total_minutes // 60
    new_minutes = total_minutes % 60

    # Calculate total hours
    total_hours = start_hour + duration_hour + extra_hours
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24

    # Determine AM/PM switch
    period_switches = ((start_hour % 12 + duration_hour + extra_hours) // 12) % 2
    if period == 'P' and (start_hour % 12 + duration_hour + extra_hours) // 12 >= 1:
        days_later += 1
    if (start_hour % 12 + duration_hour + extra_hours) // 12 >= 1:
        period = 'A' if period == 'P' else 'P'
    period = 'AM' if period == 'A' else 'PM'

    # Convert 24-hour format to 12-hour
    display_hour = final_hour_24 % 12
    if display_hour == 0:
        display_hour = 12

    # Format minutes
    display_minute = f'{new_minutes:02}'

    # Handle day of the week (if provided)
    day_info = ''
    if day_of_week:
        day_index = days.index(day_of_week.strip().capitalize())
        new_day = days[(day_index + days_later) % 7]
        day_info = f', {new_day}'

    # Handle days later message
    if days_later == 1:
        later_info = ' (next day)'
    elif days_later > 1:
        later_info = f' ({days_later} days later)'
    else:
        later_info = ''

    # Build the final time string
    new_time = f"{display_hour}:{display_minute} {period}{day_info}{later_info}"
    return new_time


print(add_time('8:16 PM', '466:02', 'tuesday'))
