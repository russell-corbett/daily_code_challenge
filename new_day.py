import shutil
from datetime import date, timedelta
from os.path import isfile

original = r'template.py'

today = date.today()
day_one = date(2023, 2, 21)
delta = today - day_one
day_num = delta.days + 1

for i in range(day_num):
    date = day_one + timedelta(days=i)
    num = i+1
    target = rf'{date} - Day {num}.py'
    if not isfile(f'{date} - Day {num}.py'):
        shutil.copyfile(original, target)
