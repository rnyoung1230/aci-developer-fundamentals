# SPOTLIGHT SESSION - 3/4
# LIBRARIES AND MODULES REVIEW
# ------------------------

# get in the habit of importing this way ("from x import y" eliminates the need to type "datetime.datetime")
from datetime import datetime, date
today = datetime.today()
now = datetime.now()
just_date = date(year=1971, month=12, day=30)

print(today)
print(now)
print(just_date)

# FILES AND FILE HANDLING INTRO
# -------------------------------
