"""
1. Sơ đồ ERD: 
   Student (1) - (N) Registration (N) - (1) Workshop.
   Student (N) - (N) Workshop (Thông qua bảng trung gian Registration).
2. Vị trí khóa ngoại: 
   Bảng Registration (Bảng con). Đặt student_id và workshop_id ở đây để tham chiếu trực tiếp đến khóa chính 2 bảng gốc nhằm ngăn chặn dữ liệu rác, đảm bảo tính toàn vẹn dữ liệu.
3. Đánh đổi cấu hình: 
   - Dùng tham số `secondary`: Truy xuất trực tiếp nhanh gọn, nhưng không lấy được các trường phụ (như thời gian đăng ký) trên bảng trung gian.
   - Truy xuất tuần tự 2 quan hệ 1-N: Truy xuất phức tạp, dài dòng hơn nhưng có thể lấy trọn vẹn thông tin từ bảng trung gian.
"""

from fastapi import FastAPI
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
