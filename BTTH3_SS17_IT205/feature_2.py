# Chức năng 2: Tạo lịch thi đấu (itertools.combinations) Hệ thống gọi hàm tạo trận đấu:
import itertools


teams_list = ['T1', 'GEN.G', 'WBG', 'BLG']


def create_match(teams_list: list) -> list:

    pairs = list(itertools.combinations(teams_list,2))
    
    return pairs
