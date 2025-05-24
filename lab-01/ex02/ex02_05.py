# Nhập số giờ làm mỗi tuần và mức lương giờ từ người dùng
so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))

# Định nghĩa số giờ tiêu chuẩn
gio_tieu_chuan = 44

# Tính số giờ vượt chuẩn (nếu có)
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)

# Tính tổng thu nhập:
# Giờ làm trong giới hạn + giờ vượt chuẩn tính 150%
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5

# In kết quả
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")
