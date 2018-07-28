from flask import *
import mlab
from models.user import User
from models.lover import Lover
from gmail import *
from datetime import datetime  
from datetime import timedelta  

app = Flask(__name__)
mlab.connect()
app.secret_key = "Dat ultra super handsome"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/love', methods=["GET", "POST"])
def love():
    if request.method == "GET":
        return render_template('love.html')
    elif request.method == "POST":
        form = request.form 
        user_id = session['user_id']
        fullname = form['fullname']
        date = form['date']
        year = form['year']
        age = 2018 - int(year)
        gender = form['gender']
        city = form['city']
        like = form.getlist('like')
        description = form['description']


        new_lover = Lover(
            user_id = user_id,
            fullname = fullname,
            date = date,
            year = year,
            age = age,
            gender = gender,
            city = city,
            like = like,
            description = description
        )
        new_lover.save()
        return render_template('love.html', fullname=fullname, age=age, like=like,gender = gender)
    

@app.route('/newlover')
def newlover():
    return render_template('newlover.html')

@app.route('/register', methods = ['POST','GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        form = request.form
        fullname = form['username']
        dob = form['day']+"/"+form['month']+"/"+form['year'] 
        gender = form['gender']
        email = form['email']
        username = form['username']
        phone = form['phone']
        password = form['password']
        confirmpassword = form['confirmpassword']
        if fullname == '' or email == '' or username =='' or password =='':
            return render_template('register.html') + "Bạn chưa điền hết các ô"
        elif ' ' in username or ' ' in password:
            return render_template('register.html') + "Tài khoản hoặc mật khẩu không được chứa dấu cách"
        elif not ( 5 < len(username) < 23):
            return render_template('register.html') + "Tài khoản phải từ 6-22 ký tự"
        elif not ( 5 < len(password) < 23):
            return render_template('register.html') + "Password phải từ 6-22 ký tự"
        elif User.objects(username= username):
            return render_template('register.html') + "Tài khoản đã có người sử dụng"
        elif User.objects(email=email):
            return render_template('register.html') + "Email đã có người sử dụng"
        elif password != confirmpassword:
            return render_template('register.html') + "Bạn chưa nhập lại mật khẩu chính xác"
        else:
            new_user = User(
                fullname= fullname,
                email = email,
                username = username,
                password = password,
                phone= phone,
                dob=dob,
                gender = gender
            )
            new_user.save()
            return redirect('/')

@app.route('/login', methods=['GET','POST'])
def login():
    if "loggedin" in session:
        return "Mày đăng nhập rồi mà"
    else:
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            form = request.form
            username = form['username']
            password = form['password']
            all_user=User.objects()
            if User.objects(username= username, password=password):
                session['loggedin'] = True
                all_user = User.objects(username = username)
                for item in all_user:
                    session['user_id'] = str(item.id)
                    session['username'] = username
                return redirect('/')
            else:
                return "Đăng nhập thất bại"

@app.route('/logout')
def logout():
    del session['loggedin']
    return redirect('/')

@app.route('/changepassword', methods = ['POST','GET'])
def changepassword():
    if "loggedin" not in session:
        return "Ban hay dang nhap"
    elif "loggedin" in session:
        if request.method == 'GET':
            return render_template('changepassword.html')
        elif request.method == 'POST':
            form = request.form 
            password = form['password']
            newpassword = form['newpassword']
            confirmpassword = form['confirmpassword']
            all_user = User.objects.get(id=session['user_id'])
            if newpassword == confirmpassword:
                if password == all_user.password:
                    all_user.update(password = newpassword)
                    return "Thanh cong"
                else:
                    return "Mat khau khong dung"
            else:
                return 'Hay nhap lai mat khau chinh xac'

@app.route('/forgotpassword', methods = ['POST','GET'])
def forgotpassword():
    if request.method == 'GET':
        return render_template('forgotpassword.html')
    elif request.method == 'POST':
        form = request.form
        all_user = User.objects(email = form['email'])
        for item in all_user:
            email = item.email
            password = item.password
            gmail=GMail('nguyenduydat1027@gmail.com','dat12345678')
            html = "<p>Mật khẩu của bạn l&agrave;:</p> {{abc}}"
            html_content = html.replace("{{abc}}", password)
            msg=Message('Khôi phục mật khẩu',to=email, html=html_content)
            gmail.send(msg)
            return ('/')

@app.route('/lover', methods = ['POST','GET'])
def lover():
    # all_lover = Lover.objects(user_id = session['user_id'])
    
    # return render_template('lover.html', all_lover = all_lover)

    if request.method == 'GET':
        all_lover = Lover.objects(user_id = session['user_id'])
        return render_template('lover.html', all_lover = all_lover)
    elif request.method == 'POST':
        form = request.form
        target = form['target']
        one_lover = Lover.objects(id=target)
        # target.fullname = one_lover.fullname
        # session['target.fullname'] = target.fullname
        return target


@app.route('/health')
def health():
    return render_template('health.html')

# @app.route('/health/bmi')
# def bmi():
#     return render_template('bmi.html')

@app.route('/gowhere')
def bmi():
    all_lover = Lover.objects(user_id = session['user_id'])
    return render_template('gowhere.html')

app.run(debug=True)
 