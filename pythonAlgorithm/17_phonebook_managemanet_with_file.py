import csv

class PhoneBook:
    def __init__(self, filename="phonebook.csv"):
        self.phonebook = {}
        self.filename = filename
        self.load_phonebook()

    def load_phonebook(self):
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                self.phonebook = {rows[0]: rows[1] for rows in reader}
                print("전화번호부가 파일에서 불러와졌습니다.")
        except FileNotFoundError:
            print(f"{self.filename} 파일이 존재하지 않아 새로 생성됩니다.")
        except Exception as e:
            print(f"전화번호부 불러오기에 실패했습니다: {e}")

    def save_phonebook(self):
        try:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                for name, phone_number in self.phonebook.items():
                    writer.writerow([name, phone_number])
            print("전화번호부가 파일에 저장되었습니다.")
        except Exception as e:
            print(f"전화번호부 저장에 실패했습니다: {e}")

    def insert(self, name, phone_number):
        self.phonebook[name] = phone_number
        print(f"{name} 이 전화번호부에 추가 되었습니다.")

    def delete(self, name):
        if name in self.phonebook:
            del self.phonebook[name]
            print(f"{name}이 전화번호부에서 삭제되었습니다.")
        else:
            print(f"{name}가(이) 전화번호부에 없습니다.")

    def modify(self, name, new_phone_number):
        if name in self.phonebook:
            self.phonebook[name] = new_phone_number
            print(f"{name}의 전화번호가 {new_phone_number}(으)로 수정되었습니다.")
        else:
            print(f"{name}가(이) 전화번호부에 없습니다.")

    def search(self, query):
        results = [f"{name}: {phone}" for name, phone in self.phonebook.items() if query in name or query in phone]
        if results:
            print("검색 결과:")
            for result in results:
                print(result)
        else:
            print(f"{query}가(이) 전화번호부에 없습니다.")

    def list(self):
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
            phonebook.save_phonebook()

        elif choice == '2':
            name = input("삭제할 이름을 입력하세요: ")
            phonebook.delete(name)
            phonebook.save_phonebook()

        elif choice == '3':
            name = input("수정할 이름을 입력하세요: ")
            new_phone_number = input("새 전화번호를 입력하세요: ")
            phonebook.modify(name, new_phone_number)
            phonebook.save_phonebook()

        elif choice == '4':
            query = input("검색할 이름 또는 전화번호를 입력하세요: ")
            phonebook.search(query)


        elif choice == '5':
            phonebook.list()

        elif choice == '6':
            phonebook.save_phonebook()  # 종료 시 파일에 저장
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

main()
