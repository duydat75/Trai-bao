from models.user import User
from models.lover import Lover
from datetime import datetime  
from datetime import timedelta  
import mlab

mlab.connect()



all_lover = Lover.objects(user_id = '5b50ab59c0bfbc1705d47c72')
print ("Đây là danh sách người yêu của bạn:")
for item in all_lover:
    print (item.fullname,"",end='')
name = input("\nBạn muốn đi chơi với ai: ")
for item in all_lover:
    if item.fullname == name:   
        print (item.age)
        print (item.like)
