def timeConversion(s):
    time_string = s.split(sep=":")
    hours = int(time_string[0])
    minutes = time_string[1]
    seconds = time_string[2][:2]
    suffix = time_string[2][-2:]

    if suffix == "PM" and hours != 12:
        hours = (hours + 12) % 24
    elif suffix == "AM" and hours == 12:
        hours = 0

    return "{:02d}:{:02s}:{:s}".format(hours, minutes, seconds)
