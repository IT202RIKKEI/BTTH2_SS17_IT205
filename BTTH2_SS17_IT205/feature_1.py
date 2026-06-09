product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]


# ============================================
#  CÁC HÀM CHÍNH
# ============================================


# Chức năng 1: Hiển thị tem nhãn. Hệ thống gọi một hàm duyệt qua product_list.
def display_product_label (product_list: list):
    
    template_tem_nhan = "Mã: {product_id:<6} | Tên: {product_name:<18} | Giá: {product_price:<6,} VND | Rating: {product_rate}*"
    
    print("--- DANH SÁCH TEM NHÃN ---")
    for product in product_list:
        part = product.split("-")
        
        # lấy ra từng thông tin
        product_id = part[0]
        product_name = part[1]
        product_price = float(part[2])
        product_rate = float(part[3])
        
        # locals cho phép template và format cho phép lấy các biến hiện tại trong phạm vi 
        print(template_tem_nhan.format_map(locals()))

display_product_label(product_list)