from datetime import datetime, date, datetime
def display_current_datetime():
  current_date = datetime.now().replace(microseconds = 0)
  print(current_date)
