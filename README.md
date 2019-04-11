# Nội dung đề cập trong tuần 4.

### 1. Điều khiển cách tạo thư mục trên python bằng thư viện os

#### - Để sử dụng thư viện os ta cần import lệnh sau
```python
import os #Operating System
import sys #System
```
#### - Ta quay lại với việc sử dụng đóng mở 1 file trước. Các câu lệnh để đóng mở 1 file:
```python
# -*- coding: utf-8 -*-
# dòng ở trên dùng để cho phép python có thể hiểu được utf-8 trên các máy linux, hay macos ...
#<tên biến> = open(<tên file, hay đường dẫn tới file>,<kiểu thực hiện 'r','w','r+'>)
#ví dụ
path = 'README.md'
file = open(path,'r+') # trong đó r+ tức là vừa đọc vừa ghi, khi gọi sẽ đọc trước rồi ghi sau
# đọc file
file.read()
# ghi file
content = '#test write file in python'
file.write(content)
# đóng file
file.close()
```

#### - Như ta đã biết nếu sử dung 'w' trong hàm open của python, nếu file chưa có, thì nó sẽ tạo ra 1 file mới, nếu file đó đã tồn tài nó sẽ ghi đè toàn bộ nội dung mới vô file đó. Ngoài ra khi sử dụng hàm open theo cách open(path,'a') thì sẽ ghi thêm vào đuôi của file đã có sẵn, nếu chưa sẽ tạo ra 1 file mới. Đây là 1 số kĩ thuật xử lý file mà ta dùng chung với thư viện os và sys
```python
# coding=utf-8
import os

path = 'hello.txt'
if os.path.exists(path):
    #os.path.exists(path) là kiểm tra xem có tồn tại file path trong thư mục không, nếu có sẽ trả #về giá trị True
    # Vì có file thì ta sẽ dùng phương thức read để đọc các giá trị của file path
    file = open(path,"r")
    print(u"Đọc file thành công giá trị của file là: ")
    print(file.read())
    # sau khi xử lý xong file đóng file lại mới có thể thực hiện tiếp các lệnh sau
    file.close()
else:
    print(u"File không tồn tại!!!")
    print(u"Sau đây ta sẽ tạo file %s ",path)
    # Nếu không tìm thấy file path ta sẽ tạo ra file path đó bằng mode = 'w'
    file = open(path,"w")
    content="hello world"
    file.write(content)
    file.close()
    print(u"Ghi file thành công, nội dung của file là")
    # Cũng như trên ta sẽ đóng file lại và khi đó ta mới có thể kiểm tra tiếp giá trị của file
    file = open(path,"r")
    print(file.read())
    file.close()
```

#### - Ở trên ta có 2 ví dụ về kiểm tra file tồn tại hay chưa trong thư viện os của hệ thống python. Bây giờ ta sẽ làm việc với 1 vài phương thức khác trong thư viện os của python.
```python
import os,sys
_dir = "hello"
if os.path.isdir(_dir):
    print("Thư mục đã tồn tại.")
    filename = "test.txt"
    file = open(_dir + "//" + filename,"w")
    file.write("SUCCESS")
    file.close()
    # Bởi vì phải thêm 1 kí tự bất kì thì mới có thể tạo file nên ta thêm 1 kí tự
    # có tính dễ nhớ để lần sau khi thêm file dễ dàng xóa nó đi ở đây ta chọn từ SUCCESS
    print("Tạo 1 file trong thư mục cũ thành công")
else:
    print("Thư mục chưa tồn tại, ta bắt đầu tạo thư mục")
    os.mkdir(_dir)
    print("Tạo thư mục thành công ta tạo 1 file trong thư mục này làm dấu")
    path = _dir + "//" + "test.txt"
    file = open(path,"w")
    file.write("SUCCESS")
    file.close()
    print("Tạo file trong thư mục mới tạo thành công")
```

### 2. nhắc lại cách lấy dữ liệu của 1 POST từ 1 trang web gửi về server

#### - Nhận dữ liệu về từ dạng form
```python
#coding=utf-8
# import các thư viện cần dùng
from flask import Flask, request,url_for,render_template
import json

#Bắt đầu tạo 1 server qua biến app
app = Flask(__name__)

#Tạo bộ định tuyến(route) để nhận các giá trị từ trang web gửi về
# Ví dụ Website gửi về đường dẫn như sau "/sign-up-form với phương thức POST ta tạo
@app.route("/sign-up-form",methods=["post"])
# tạo hàm thực hiện tác vụ
def sign_up_form():
    # giả sử trên form gửi về ta có các name của các input như sau id,password,name,email
    # thì ta sẽ tạo các giá trị để nhận các name này bằng thư viện request đã import ở trên.
    # Ta tạo 1 biến id để nhận giá trị từ input có name là id từ website như sau
    id = request.form["id"]
    # tương tự với các cái phía sau
    pwd = request.form["password"]
    name = request.form["name"]
    email = request.form["email"]
```

### 3. Bài tập vận dụng đầu tiên:

#### - Tạo 1 lớp để biểu diễn thông tin người dùng đăng ký.
#### - Tạo 1 lớp để lưu trữ các thông tin người dùng đăng ký. Mỗi 1 người dùng đăng ký đều có 1 Folder riêng để lưu trữ thông tin. Nội dung folder đó như sau:
+ Folder có tên là id hoặc địa chỉ email của người dùng.
+ Bên trong folder đó là các folder con 1 folder lưu trữ hình ảnh hay âm thanh lưu lại của người dùng, 1 folder lưu trữ thông tin người dùng.

#### - Tạo 1 lớp để kiểm soát tình trạng đăng nhập của người dùng, gồm các phương thức sau:
1. Tạo và lưu trữ thông tin người dùng thông qua class mà ta đã tạo ở trên.
2. Tạo và lưu trữ id đăng nhập và password ở trong 1 folder riêng.
3. Kiểm tra xem tài khoản người dùng đã tồn tại hay chưa.
4. Kiểm tra xem người dùng đã đăng nhập tài khoản của mình chưa.
5. Nếu tài khoản có tồn tại và đã đăng nhập, trả về dữ liệu người dùng.
6. Tạo 1 route bắt sự kiện từ việc tạo tài khoản của người dùng từ website và sử dụng gọi lại phương thức đã tạo trong bài tập 1 và 2
7. Bài tập nâng cao, làm mịn tất cả dữ liệu người dùng và nghĩ xem 1 đối tượng người dùng có bao nhiêu thuộc tính, càng nhiều càng tốt.

### Nội dung tuần 4 xoay quanh việc kĩ thuật sử dụng các nội dung đã đề cập ở tuần 3. Bài tập khá là khó nên mọi người có thể làm chung. Để hiểu được các thuật toán và quy trình phát triển lên các thuật toán xử lý ảnh. Mình cần làm có các bạn nắm rõ được bản chất của dữ liệu trước, sau đó là 1 chút thông tin về machine learning, rồi từ nhưng dữ liệu cơ bản đối với 1 con người bình thường sẽ bắt đầu áp dụng qua từng pixel ảnh, từ machine learning sẽ phát triển lên các thuật toán deep learning trong xử lý ảnh nên mọi người chịu khó tham gia đầy đủ và làm chung bài tập.