
teams_list = []


import itertools


teams_list = ['T1', 'GEN.G', 'WBG', 'BLG']


def create_match(teams_list: list) -> list:

    pairs = list(itertools.combinations(teams_list,2))
    
    return pairs

# Chức năng 3: Tạo mã trận đấu tự động Hệ thống gọi hàm xử lý danh sách trận đấu vừa tạo ở chức năng 2

match_data = create_match(teams_list)

# duyệt qua để tạo id tự động
for position, match in enumerate(match_data, start=1):
    
    left_team_name = f"{match[0][:3]:X<3}"
    right_team_name = f"{match[1][:3]:X<3}"
    
    
    auto_match_id = f"Trận {position} ({match[0]} vs {match[1]}) -> ID: M{position:02d}-{left_team_name}-{right_team_name}"
    
    
    print(auto_match_id)