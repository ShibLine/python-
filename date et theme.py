date et theme 
from datetime import datetime

from datetime import datetime

now = datetime.now()

print(now)

from datetime import datetime
now = datetime.now()

print now.year
print now.month
print now.day

from datetime import datetime
now = datetime.now()
print '%02d/%02d/%04d' % (now.month, now.day, now.year)
rom datetime import datetime
now = datetime.now()

print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

from datetime import datetime
now = datetime.now()

print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
