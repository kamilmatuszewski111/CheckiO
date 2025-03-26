"""
 You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next rules:

    - the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday);
    - if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'.

Input: Time in the 24-hour format (as a string).

Output: Time in the 12-hour format (as a string).
"""


def time_converter(time: str) -> str:
    lista = time.split(":")
    if int(lista[0]) > 12:
        return ":".join([str(int(lista[0]) - 12), str(lista[1])]) + " p.m."
    elif int(lista[0]) == 12:
        return ":".join([str(lista[0]), str(lista[1])]) + " p.m."
    elif lista[0] == "00":
        return ":".join([str(12), str(lista[1])]) + " a.m."
    else:
        return ":".join([str(int(lista[0])), str(lista[1])]) + " a.m."


print("Example:")
print(time_converter("12:30"))

assert time_converter("12:30") == "12:30 p.m."
assert time_converter("09:00") == "9:00 a.m."