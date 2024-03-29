# dates are easily constructed and formatted
from datetime import date
now = date.today()
now
# datetime.date(2003, 12, 2)            output
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'           output

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
age.days
# 14368                 output