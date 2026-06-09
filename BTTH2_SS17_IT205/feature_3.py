
from functools import reduce


product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]

# Chức năng 3: Tính tổng giá trị (functools.reduce) Hệ thống gọi hàm tính toán:
def calculate_total_value(product_list: list)-> int | str:
    
    # list comprehension lấy ra các item chỉ chứa value
    value_list = [int(product.split("-")[2]) for product in product_list]
    
    # sử dụng hàm reduce để tính tổng
    total_value = reduce(lambda acc, value: acc + value, value_list)
    
    total_string = f"{total_value:,} VND"
    
    return total_value, total_string
    
    
calculate_total_value(product_list)