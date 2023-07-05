# AIFFEL Campus Online 5th Code Peer Review Templete
- 코더 : 김소연
- 리뷰어 : 전요한


# PRT(PeerReviewTemplate) 
각 항목을 스스로 확인하고 토의하여 작성한 코드에 적용합니다.

- [O] 코드가 정상적으로 동작하고 주어진 문제를 해결했나요?<br>
- <b>import time을 주고 sleep함수를 이용해 2초 간격으로 반복되게 잘 동작하고 컴프리헨션과 제너레이터를 사용하여 잘 나타냈다.</b><hr>
- [O] 주석을 보고 작성자의 코드가 이해되었나요?<br>
  왜 이걸 사용했는지와 어떻게 사용했는지가 나와있어 이해하기 쉬웠다.<hr>
- [O] 코드가 에러를 유발할 가능성이 없나요?<br>
  코드를 작성하다가 잘못 기재해 싱택스에러가 일어나지 않는 이상 에러를 유발하지는 않을 것 같다.<hr>
- [O] 코드 작성자가 코드를 제대로 이해하고 작성했나요?<br>
  챌린지로 사용자에게 리스트를 입력받아 함수를 호출하고 출력하는 코드도 만들어 놓으신거 보면 제대로 이해한 후 심화까지 작성하신거라 생각되기에
  제대로 이해를 하신 것 같다.<hr>
- [O] 코드가 간결한가요?<br>
  import와 함수의 집합 생성 후 리스트를 생성한 후에 함수의 출력 순으로 간결하게 작성해주셨고 띄어쓰기와 들여쓰기도 잘 되어있어 보기도 편하게
  되어있다.<hr>

# 예시
1. 코드의 작동 방식을 주석으로 기록합니다.
2. 코드의 작동 방식에 대한 개선 방법을 주석으로 기록합니다.
3. 참고한 링크 및 ChatGPT 프롬프트 명령어가 있다면 주석으로 남겨주세요.
```python
import time #sleep함수 이용하기 위해 import

def fish_compre(fish_list) : #생선리스트 컴프리헨션으로 출력하는 함수 생성
  return [f"{fish['이름']} is swimming at {fish['speed']} m/s" for fish in fish_list]

def fish_gen(fish_list) : #생선리스트 제너레이터로 출력하는 함수 생성
  for fish in fish_list:
    yield f"{fish['이름']} is swimming at {fish['speed']} m/s"


fish_list = [
{"이름": "Nemo", "speed": 3},
{"이름": "Dory", "speed": 5},
] #생선리스트 생선

print("Using Comprehension:")
compre_result =fish_compre(fish_list) #fish_compre함수 호출
for result in compre_result : #생선 리스트 컴프리헨션으로 출력
    print(result)
    time.sleep(2) #2초 간격으로 출력

print("Using Generator:")
gen_result =fish_gen(fish_list) #fish_gen함수 호출
for result in compre_result : #생선 리스트 제너레이터로 출력
    print(result)
    time.sleep(2) #2초 간격으로 출력
```

# 참고 링크 및 코드 개선
```python
as t 를 사용할 시 무려 3글자나 생략 가능하기에 as 를 생활화 하시는 걸 추천드립니다.

```
