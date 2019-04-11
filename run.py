print("ACCESSING SUCCESSFUL!")
from flask import Flask, render_template,url_for, request

# Tạo ra lớp user để lưu trữ thông tin của người truy cập
class user:
    def __init__(self,name,introduce,img):
        self.name = name
        self.introduce = introduce
        self.img = img

# Vì lí do 1 chương trình server khi thực hiện là đã đọc toàn bộ nội dung của các module
# Cho nên nếu ta gọi 1 biến Login thông thường thì người dùng đầu tiên đăng nhập thì sẽ
# có giá trị là LoginSuccess những người sau không cần đăng nhập vẫn kiểm soát được.
# Do đó ta phải kiểm soát tình trạng đăng nhập trên 1 đối tượng.
class Login:
    def __init__(self,admin):
        self.admin = admin
    
    def isAdmin(self):
        return self.admin
    def set_admin(self,admin):
        self.admin = admin

app = Flask(__name__)

def success():
    return True

admin = Login(False)

@app.route("/login",methods=["POST"])
def login():
    if success() == True:
        admin.set_admin(True)
        return render_template("login_success.html")
    else:
        admin.set_admin(False)
        return render_template("login.html")

@app.route("/sign-up",methods=["POST"])
def sign_up():
    return ""

@app.route("/",methods=["POST","GET"])
def hello():
    if admin.isAdmin() == False:
        return render_template("index.html")
    if admin.isAdmin() == True:
        x = url_for('static',filename='camgiang.jpg')
        intro = "Công Nghệ Sinh Học- Đại Học Khoa Học Tư Nhiên, Bộ môn Hóa Sinh"
        _user = user("Nguyễn Thị Cẩm Giang",intro,x)
        return render_template("home.html",user = _user)

@app.route("/home")
def home():
    x = url_for('static',filename='camgiang.jpg')
    intro = "Công Nghệ Sinh Học- Đại Học Khoa Học Tư Nhiên, Bộ môn Hóa Sinh"
    _user = user("Nguyễn Thị Cẩm Giang",intro,x)
    return render_template("home.html",user = _user)


if __name__ == '__main__':
    app.run()
