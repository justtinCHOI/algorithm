import calendar

def is_leap_year(year):
    """윤년 여부를 판단하는 함수"""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def print_calendar(year, month):
    """입력받은 년, 월의 달력을 출력하는 함수"""
    # 달력 출력
    print(calendar.month(year, month))

def main():
    try:
        # 사용자로부터 년, 월 입력 받기
        year = int(input("년도를 입력하세요 (예: 2024): "))
        month = int(input("월을 입력하세요 (1-12): "))

        # 입력값 유효성 검사
        if month < 1 or month > 12:
            print("올바른 월을 입력하세요. (1-12)")
            return

        # 윤년 여부 출력
        if is_leap_year(year):
            print(f"{year}년은 윤년입니다.")
        else:
            print(f"{year}년은 윤년이 아닙니다.")

        # 달력 출력
        print_calendar(year, month)

    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력하세요.")

main()

