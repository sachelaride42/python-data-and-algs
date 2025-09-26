def add_time(start, duration, starting_day=None):
    result = ''

    period_list = ['AM', 'PM']
    day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    time_start = start.split(' ')
    hour_start = int(time_start[0].split(':')[0])
    min_start = int(time_start[0].split(':')[1])
    period = period_list.index(time_start[1])

    hour_duration = int(duration.split(':')[0])
    min_duration = int(duration.split(':')[1])
    total_duration = hour_duration * 60 + min_duration

    final_min = (min_start + total_duration) % 60
    if final_min < 10:
        final_min = f'0{final_min}'
    final_hour = (hour_start + (min_start + total_duration) // 60) % 12
    if final_hour == 0:
        final_hour = '12'
    result += f'{final_hour}:{final_min} '

    final_period_adder = ((hour_start + (min_start + total_duration) // 60) // 12) % 2
    final_period = period_list[((period + final_period_adder) % 2)]
    result += f'{final_period}'

    if period_list[period] == 'AM':
        days_after = (hour_start + (min_start + total_duration) // 60) // 24
    else:
        days_after = (12 + hour_start + (min_start + total_duration) // 60) // 24

    print(days_after)

    if starting_day is not None:
        for index, day in enumerate(day_list):
            if starting_day.lower() == day.lower():
                start_day_index = index
        final_day = day_list[(start_day_index + days_after) % 7]
        result += f', {final_day}'

    if days_after == 1:
        result += ' (next day)'
    elif days_after > 1:
        result += f' ({days_after} days later)'

    print(result)
    return result


add_time('3:00 PM', '3:10')
add_time('11:43 AM', '00:20')
add_time('8:16 PM', '466:02')
add_time('10:10 PM', '3:30')
add_time('11:43 PM', '24:20', 'tueSday')