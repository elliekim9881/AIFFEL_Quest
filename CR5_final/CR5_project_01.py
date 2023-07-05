class Square:
    def __init__(self):
        square = int(input('넓이를 구하고 싶은 사각형의 숫자를 써주세요.\n 1.직사각형 2.평행사변형 3.사다리꼴 \n >>>'))

        if square == 1:
            print('직사각형 함수는 rect()입니다.')

        elif square == 2:
            print('평행사변형 함수는 par()입니다.')
        
        elif square == 3:
            print('사다리꼴 함수는 trape()입니다.')
        
        else:
            print('1, 2, 3 중에서 다시 입력해주세요')

    def rect(self):
        width, vertical = map(int, input('가로, 세로를 입력하세요. 예시 : 가로,세로\n >>> ').split(','))
        area = width * vertical
        result = '직사각형의 넓이는 : ' + str(area)
        return result

    def par(self):
        width, vertical = map(int, input("밑변과 높이의 길이를 입력하시오. 예시:3,5\n >>> ").split(","))
        areaP= width*vertical
        result = '평행사변형의 넓이는 : ' + str(areaP)
        return result

    def trape(self):
        width, vertical, height = map(float, input("윗변과 밑변,높이의 길이를 입력하시오. 예시:3,5,2\n >>> ").split(","))
        areaT= (width+vertical)*height/2
        result = '사다리꼴의 넓이는 : ' + str(areaT)
        return result

a = Square()
print(a.rect())
print(a.par())
print(a.trape())