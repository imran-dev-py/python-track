# Convert days to seconds
def convert_days_to_seconds(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds


days = int(input('Provide a day for convert into miliseconds: '))
total__seconds = convert_days_to_seconds(days)
mili__seconds = total__seconds * 1000
print(f'{mili__seconds}ms')
