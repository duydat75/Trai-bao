from models.user import User
from models.lover import Lover
from datetime import datetime  
from datetime import timedelta  
import mlab


mlab.connect()
all_lover = Lover.objects()
for item in all_lover:
    print (item.date - timedelta(days=1))