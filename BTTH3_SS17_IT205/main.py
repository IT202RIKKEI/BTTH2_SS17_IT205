import itertools



teams_list = []

# ============================================
#  CÁC HÀM CHÍNH
# ============================================

# Chức năng 1: Nhập danh sách Đội tuyển Yêu cầu người dùng nhập tên các đội tuyển trên cùng một dòng, cách nhau bởi dấu phẩy. Hệ thống gọi hàm xử lý:

def add_teams(teams_list: list):
    print("--- NHẬP DANH SÁCH ---")
    while True:
        input_teams = input("Nhập các đội (cách nhau bởi dấu phẩy): ").strip()
        
        if not input_teams:
            print("Không được để trống!")
            continue
        break
    # lọc khoảng trắng và viết hoa
    
    list_team = input_teams.split(",")
    
    cleaned_list_teams = [team.strip().upper() for team in list_team]
    
    print(f"Thêm {cleaned_list_teams} thành công")
    teams_list.extend(cleaned_list_teams)
    
# Chức năng 2: Tạo lịch thi đấu (itertools.combinations) Hệ thống gọi hàm tạo trận đấu:
def create_match(teams_list: list) -> list:

    pairs = list(itertools.combinations(teams_list,2))
    
    return pairs


# Chức năng 3: Tạo mã trận đấu tự động Hệ thống gọi hàm xử lý danh sách trận đấu vừa tạo ở chức năng 2
def auto_create_match_id(match_data: list):
    for position, match in enumerate(match_data, start=1):
        
        left_team_name = f"{match[0][:3]:X<3}"
        right_team_name = f"{match[1][:3]:X<3}"
        
        
        auto_match_id = f"Trận {position} ({match[0]} vs {match[1]}) -> ID: M{position:02d}-{left_team_name}-{right_team_name}"
        
        
        print(auto_match_id)

def main():

    while True:
        try:
            choice = int(input("""
============= ESPORTS MATCHMAKER =============
1. Nhập danh sách Đội tuyển
2. Tạo lịch thi đấu (Combinations)
3. Tạo mã trận đấu tự động (F-String & Cắt chuỗi)
4. Đóng hệ thống
==============================================
Chọn chức năng (1-4): """))

            if choice < 1 or choice > 4:
                print("Lựa chọn không hợp lệ, vui lòng nhập từ 1-4!")
                continue

            match choice:
                case 1:
                    add_teams(teams_list)
                case 2:
                    if teams_list == []:
                        print("Chưa có trận đấu để tạo!")
                        continue
                    # tạo trận đấu tự động
                    match_data = create_match(teams_list)
                    # duyệt qua để in
                    for position,match in enumerate(match_data, start=1):
                        print(f"{position} {match[0]} vs {match[1]}")
                    
                    print(f"Tổng số trận đấu: {len(match_data)}")
                case 3:
                    match_data = create_match(teams_list)
                    if match_data == []:
                        print("Chưa có trận đấu để tạo! ")
                        continue
                    auto_create_match_id(match_data)

                case 4:
                    print("Đóng hệ thống thành công!")
                    break

        except ValueError:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-4!")


if __name__ == "__main__":
    main()