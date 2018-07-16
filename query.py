from models.user import User
import mlab


mlab.connect()
all_user = User.objects(email = "asd@gmail.com")
for item in all_user:
    print (len(item.username))
    print (item.email)
