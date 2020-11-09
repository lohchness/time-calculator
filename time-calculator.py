start = ""
duration = ""
startingday = ""

def day_of_week(x):
  return {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7,
  }[x]

def day_of_week_numkey(x): 
  return {
      1: "Monday",
      2: "Tuesday",
      3: "Wednesday",
      4: "Thursday",
      5: "Friday",
      6: "Saturday",
      7: "Sunday",
  }[x]

start = ""
duration = ""
startingday = ""

def add_time(start, duration, *startingday):
  days_later = 0

  start_split = start.split() # Split into time and period first
  a = start_split[0]
  b = a.split(':')

  start_hour = b[0] # HOUR:minutes
  start_minutes = b[1] # hour:MINUTES
  start_period = start_split[1] # AM OR PM
  # checked, code above is fine 

  # CONVERTING INTO 24 HOUR TIME
  if start_period == "PM":
    if start_hour == "12":
      start_hour_24 = start_hour
    else:
      start_hour_24 =  int(start_hour) + 12
  else: # if start_period == "AM":
    if len(start_hour) == 1:
      start_hour_24 = str("0") + str(start_hour)
    elif start_hour == "12":
      start_hour_24 = 0
    else:
      start_hour_24 = start_hour

  duration_time = duration.split(':') 
  duration_hours = int(duration_time[0])
  duration_minutes = int(duration_time[1])

  if duration_hours > 24:
    duration_hours_days = int(duration_hours) // 24
    days_later += duration_hours_days
    duration_hours -= duration_hours_days*24

  final_hour_24_calc = int(start_hour_24) + duration_hours # start hour + remaining duration hours after subtracting the amount of 24s that can fit
  # below 2 lines run if final_hour_24_calc > 24.
  days_later += final_hour_24_calc // 24
  final_hour_24_remaining = final_hour_24_calc - ((final_hour_24_calc//24)*24) # floor division * 24 
  # need to check again after final_minutes_24_calc in case minutes > 60, therefore increasing the hour by 1.
  # working

  final_minutes_24_calc = int(start_minutes) + int(duration_minutes)
  if final_minutes_24_calc > 60:
    final_hour_24_remaining += 1
    final_minutes_24_calc -= 60

  if final_hour_24_remaining > 23:
    days_later += final_hour_24_remaining // 24
    final_hour_24_remaining = final_hour_24_remaining - ((final_hour_24_remaining//24)*24)

  if final_hour_24_remaining > 12: # Ensures that the final hour time is under 12
    final_hour_24_remaining -= 12
    final_period = "PM"
  elif final_hour_24_remaining == 12 and start_period == "AM": # for 12PM times
    final_period = "PM"
  else:
    final_period = "AM"
    if final_hour_24_remaining == 0:
      final_hour_24_remaining = "12"

  # DAY OF THE WEEK
  if startingday:
    for sday in startingday:
      day = sday.title()
      dayNumber = day_of_week(day)
      dayNumber2 = dayNumber + days_later
      while dayNumber2 > 7:
        dayNumber2 -= 7
      dayFinal = day_of_week_numkey(dayNumber2)

  finalTimeString = str(final_hour_24_remaining) + ":" + str(final_minutes_24_calc).rjust(2, '0')

  if startingday and days_later == 0:
    new_time = f"{finalTimeString} {final_period}, {dayFinal}"
  elif not startingday and days_later == 0:
    new_time = f"{finalTimeString} {final_period}"
  elif startingday and days_later == 1:
    new_time = f"{finalTimeString} {final_period}, {dayFinal} (next day)"
  elif not startingday and days_later == 1:
    new_time = f"{finalTimeString} {final_period} (next day)"
  elif not startingday and days_later > 1:
    new_time = f"{finalTimeString} {final_period} ({days_later} days later)"
  else: # if days_later > 1 and startingday is true
    new_time = f"{finalTimeString} {final_period}, {dayFinal} ({days_later} days later)"

  return new_time