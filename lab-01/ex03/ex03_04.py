def truy_cap_phan_tu(tuple_data):
    first_elenment = tuple_data[0]
    last_element = tuple_data[-1]
    return first_elenment, last_element
# nhập tuple từ người dùng
input_tuple = eval(input("nhập tuple, ví dụ (1,2,3):"))
first,last = truy_cap_phan_tu(input_tuple)
#in kết quả 
print(" phần tử đầu tiên:",first)
print(" phần tử cuối cùng:",last)