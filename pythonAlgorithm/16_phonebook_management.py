class PhoneBook:
    def __init__(self):
        self.phonebook = {}

    def insert(self, name, phone_number):
        # 이름과 번호로 전화번호부에 추가
        self.phonebook[name] = phone_number
        print(f"{name} 이 전화번호부에 추가 되었습니다.")

    def delete(self, name):
        if name in self.phonebook:
            # 검색 성공
            del self.phonebook[name]
            print(f"{name}이 전화번호부에서 삭제되었습니다.")
        else:
            # 검색 실패
            print(f"{name}가(이) 전화번호부에 없습니다.")

    def modify(self, name, new_phone_number):
        if name in self.phonebook:
            # 검색 성공
            self.phonebook[name] = new_phone_number
            print(f"{name}의 전화번호가 {new_phone_number}(으)로 수정되었습니다.")
        else:
            # 검색 실패
            print(f"{name}가(이) 전화번호부에 없습니다.")

    def search(self, query):
        # 이름 또는 번호로 찾기
        results = [f"{name}: {phone}" for name, phone in self.phonebook.items()
                   if query in name or query in phone]
        if results:
            # 검색 성공
            print("검색 결과:")
            for result in results:
                print(result)
        else:
            # 검색 실패
            print(f"{query}가(이) 전화번호부에 없습니다.")

    def list(self):
        # 이름으로 정렬된 전화번호부 출력
        print("전화번호부 (이름으로 정렬):")
        for name in sorted(self.phonebook):
            print(f"{name}: {self.phonebook[name]}")


def main():
    phonebook = PhoneBook()

    while True:
        print("\n메뉴를 선택하세요:")
        print("1. 추가")
        print("2. 삭제")
        print("3. 수정")
        print("4. 검색")
        print("5. 목록 보기")
        print("6. 종료")

        choice = input("메뉴 번호를 입력하세요: ")

        if choice == '1':
            name = input("이름을 입력하세요: ")
            phone_number = input("전화번호를 입력하세요: ")
            phonebook.insert(name, phone_number)

        elif choice == '2':
            name = input("삭제할 이름을 입력하세요: ")
            phonebook.delete(name)

        elif choice == '3':
            name = input("수정할 이름을 입력하세요: ")
            new_phone_number = input("새 전화번호를 입력하세요: ")
            phonebook.modify(name, new_phone_number)

        elif choice == '4':
            query = input("검색할 이름 또는 전화번호를 입력하세요: ")
            phonebook.search(query)

        elif choice == '5':
            phonebook.list()

        elif choice == '6':
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 시도하세요.")


main()
