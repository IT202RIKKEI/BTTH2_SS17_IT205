# Chức năng 2: Sắp xếp thông minh (list.sort với key) Hệ thống gọi hàm sắp xếp lại product_list.
product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]


def sort_product(item):
    part = item.split("-")
    
    rating = float(part[3])
    price = int(part[2])
    
    return (-rating, price)

# sắp xeeos rating và giá tiền
def sort_list(product_list: list):
    print("--- TỔNG GIÁ TRỊ KHO ---")
    for index, item in enumerate(product_list, start=1):
        part = item.split("-")
        
        price = part[2]
        rating = part[3]
        
        product_list.sort(key=sort_product)


    for index, item in enumerate(product_list, start=1):
        # in ra
        print(f"{index}. {item}")




