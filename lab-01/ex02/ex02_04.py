# Tạo một danh sách rỗng để lưu kết quả
j = []

# Duyệt qua các số từ 2000 đến 3200 (bao gồm cả 3200)
for i in range(2000, 3201):
    # Kiểm tra chia hết cho 7 và không chia hết cho 5
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))  # Chuyển số thành chuỗi và thêm vào danh sách

# In kết quả, cách nhau bởi dấu phẩy
print(','.join(j))
