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
