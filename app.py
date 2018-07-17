from flask import *
import mlab
from models.user import User
from models.lover import Lover
from gmail import *

app = Flask(__name__)
mlab.connect()
app.secret_key = "Dat ultra super handsome"


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        form = request.form 
        user_id = session['user_id']
        fullname = form['fullname']
        dob = form['dob']
        gender = form['gender']
        city = form['city']
        like = form.getlist('like')
        hate = form.getlist('hate')
        description = form['description']

        new_lover = Lover(
            user_id = user_id,
            fullname = fullname,
            dob = dob,
            gender = gender,
            city = city,
            like = like,
            hate = hate,
            description = description
        )
        new_lover.save()
        return redirect(url_for('index'))

@app.route('/#form-lover')
def lover():
    return render_template('lover.html')

@app.route('/register', methods = ['POST','GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        form = request.form
        fullname = form['username']
        email = form['email']
        username = form['username']
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
                password = password
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
                return redirect('/')
            else:
                return "Đăng nhập thất bại"

@app.route('/logout')
def logout():
    del session['loggedin']
    return redirect(url_for('index'))

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

if __name__ == '__main__':
  app.run(debug=True)
 