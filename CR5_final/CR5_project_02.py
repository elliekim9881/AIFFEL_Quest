# 전체 메뉴와 가격 
menu = ['americano', 'latte', 'mocha', 'yuza_tea', 'green_tea', 'choco_latte']
price = [2000, 3000, 3000, 2500, 2500, 3000]

class Kiosk: 
    def __init__(self):
        # 문제 2-1의 답을 입력하세요. 
        self.menu = menu
        self.price = price
    # 메뉴 출력 메서드
    def menu_print(self):
        for i in range(len(self.menu)):
            print(i + 1, self.menu[i], ' : ', self.price[i], '원')

    # 주문 메서드
    def menu_select(self):
        self.order_menu = []  # 주문 리스트
        self.order_price = []  # 가격 리스트

        n = 0
        while n < 1 or len(menu) < n:
            n = int(input("음료를 번호를 입력하세요 : "))  # 음료 번호 입력

            # 메뉴판에 있는 음료 번호일 때
            if 1 <= n & n <= len(menu):
                self.order_price.append(self.price[n-1])  # 가격 리스트에 추가합니다.
                self.price_sum = self.price[n-1]  # 합계 금액
                # 메뉴판에 없는 번호일 때
            else:  
                print("없는 메뉴입니다. 다시 주문해 주세요.")

        # 음료 온도 물어보기
        t = 0  # 기본값을 넣어주고
        while t != 1 and t != 2:  # 1이나 2를 입력할 때까지 물어보기
            t= int(input("HOT 음료는 1을, ICE 음료는 2를 입력하세요 : "))
            if t == 1:
                self.temp = "HOT"
            elif t == 2:
                self.temp = "ICE"  
            else:    
                print("1과 2 중 하나를 입력하세요.\n")

        self.order_menu.append(self.temp + ' ' + self.menu[n-1])  # 주문 리스트에 추가합니다.
        print(self.temp, self.menu[n-1], ' : ', self.price[n-1], '원')  # 온도 속성을 추가한 주문 결과를 출력합니다.

        # 추가 주문 또는 지불
        while n != 0:  # 지불을 선택하기 전까지 반복합니다.
            print()  # 줄 바꾸면서 
            n = int(input("추가 주문은 음료 번호를, 지불은 0을 누르세요 : "))  # 추가 주문 또는 지불
            if n > 0 and n < len(self.menu) + 1: 
                self.order_price.append(self.price[n-1])  # 가격 리스트에 추가합니다.
                self.price_sum += self.price[n-1]  # 합계 금액
                t = 0  # 기본값을 넣어주고
                while t != 1 and t != 2:  # 1이나 2를 입력할 때까지 물어보기
                    t= int(input("HOT 음료는 1을, ICE 음료는 2를 입력하세요 : "))
                    if t == 1:
                        self.temp = "HOT"
                    elif t == 2:
                        self.temp = "ICE"  
                    else:    
                        print("1과 2 중 하나를 입력하세요.\n")
                self.order_menu.append(self.temp + ' ' + self.menu[n-1])  # 주문 리스트에 추가합니다.    
                print('추가 주문 음료', self.temp, self.menu[n-1], ':', self.price[n-1], '원\n', '합계 : ', self.price_sum, '원')
            elif n == 0 :  # 지불을 입력하면
                print("주문이 완료되었습니다.")
                print(self.order_menu, self.order_price)  # 확인을 위한 리스트를 출력합니다.
            else :  # 없는 번호를 입력할 때
                print("없는 메뉴입니다. 다시 주문해 주세요.")

    def pay(self):
        print(f"지불할 금액은 {self.price_sum}입니다.")
        n=0
        while n != '1' and n != '2' and n != 'card' and n != 'cash':
            n = str(input("지불방법을 선택해주세요.(입력예시:cash or 1/ card or 2): "))
            if n == 'cash' or n == '1':
                print('직원을 호출하겠습니다.')
            elif n == 'card' or n == '2':
                print('IC칩 방향에 맞게 카드를 꽂아주세요.')
            else:
                print("올바른 지불방법을 선택해주세요.")

    def table(self):
        # 외곽
        print('⟝' + '-' * 30 + '⟞')
        for i in range(5):
            print('|' + ' ' * 31 + '|')

        # 주문 상품명 : 해당 금액
        for i in range(len(self.order_menu)):
            print(self.order_menu[i-1], ' : ', self.order_price[i-1])

        print('합계 금액 :', self.price_sum)

        # 외곽
        for i in range(5):
            print('|' + ' ' * 31+ '|')
        print('⟝' + '-' * 30 + '⟞')

a = Kiosk()  # 객체 생성
a.menu_print()  # 메뉴 출력
a.menu_select()  # 주문
a.pay() #지불
a.table() #주문표 출력
