# Nhập X và Y từ người dùng, cách nhau bởi dấu phẩy
input_str = input("Nhập X, Y: ")

# Tách và chuyển đổi chuỗi nhập thành hai số nguyên
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]

# Tạo mảng 2 chiều với giá trị mỗi phần tử là i * j
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col

# In kết quả
print(multilist)
