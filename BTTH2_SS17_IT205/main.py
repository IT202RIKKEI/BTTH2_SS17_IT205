from functools import reduce

product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5", #trường hợp return 0 cho hàm phụ trợ
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]



# ============================================
#  CÁC HÀM PHỤ TRỢ
# ============================================



# hàm chuyển đổi 
def check_and_cast(value):
    if isinstance(value, str) and value.isdigit():
        return int(value)
    elif isinstance(value, (int, float)):
        return int(value)
    
    return 0  
    # trả về 0 nếu chứa ký tự đặc biệt

# ============================================
#  CÁC HÀM CHÍNH
# ============================================

def sort_product(item):
    part = item.split("-")

    if len(part) != 4:
        return (0, 0)

    rating = float(part[3])
    price = check_and_cast(part[2])

    return (-rating, price)


def display_product_label(product_list: list):
    template_tem_nhan = "Mã: {product_id:<10} | Tên: {product_name:<18} | Giá: {product_price:<10,} VND | Rating: {product_rate}*"

    print("--- DANH SÁCH TEM NHÃN ---")

    for product in product_list:
        part = product.split("-")

        if len(part) != 4:
            print(f"Dữ liệu sai định dạng: {product}")
            continue

        product_id = part[0]
        product_name = part[1]
        product_price = check_and_cast(part[2])

        try:
            product_rate = float(part[3])
        except ValueError:
            product_rate = 0

        print(template_tem_nhan.format_map(locals()))


def sort_list(product_list: list):
    print("--- DANH SÁCH SAU KHI SẮP XẾP ---")

    product_list.sort(key=sort_product)

    for index, item in enumerate(product_list, start=1):
        print(f"{index}. {item}")


def calculate_total_value(product_list: list):
    value_list = []

    for product in product_list:
        part = product.split("-")

        if len(part) != 4:
            continue

        value_list.append(check_and_cast(part[2]))

    total_value = reduce(lambda acc, value: acc + value, value_list, 0)

    total_string = f"{total_value:,} VND"

    return total_value, total_string
    

def main():
    while True:
        try:
            choice = int(input("""
============= E-COMMERCE ANALYTICS =============
1. Hiển thị tem nhãn sản phẩm (format_map & F-String)
2. Sắp xếp sản phẩm thông minh (sort key)
3. Tính tổng giá trị kho hàng (reduce)
4. Đóng hệ thống
================================================
Chọn chức năng (1-4): """))

            if choice < 1 or choice > 4:
                print("Lựa chọn không hợp lệ, vui lòng nhập từ 1-4!")
                continue

            match choice:
                case 1:
                    display_product_label(product_list)
                case 2:
                    sort_list(product_list)
                case 3:
                    _, total_string = calculate_total_value(product_list)
                    
                    print("--- TỔNG GIÁ TRỊ KHO ---")
                    print(f"Tổng giá trị các mặt hàng hiện tại là: {total_string}")

                case 4:
                    print("Đóng hệ thống thành công!")
                    break

        except ValueError:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-4!")
            
if __name__ == "__main__":
    main()