def get_level(): 
    level = input("난이도(초급 1 중급 2 고급 3)를 숫자로 입력해주세요. : ")
    while level not in ("1","2","3"):
        level = input("난이도(초급 1 중급 2 고급 3)를 숫자로 입력해주세요. : ")
    if level == "1":
        return 30
    elif level == "2":
        return 41
    else:
        return 50
