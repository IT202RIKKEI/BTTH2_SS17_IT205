teams_list = []

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
    
    teams_list.extend(cleaned_list_teams)
    
add_teams(teams_list)