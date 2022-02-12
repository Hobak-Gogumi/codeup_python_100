# codeup_python_100
[코드업 Python 기초 100제](https://codeup.kr/problemsetsol.php?psid=33)를 풀이한 리포지토리 입니다.

---
### 출력
+ 쉼표(,)로 구분하면 공백을 사이에 두고 출력
+ +로 구분하면 공백을 사이에 두지않음
+ 따옴표, 백슬래시 등을 출력하려면 앞에 백슬래시(\\)를 붙인다

### 입출력
+ input으로 받은 자료형은 문자열(str)
+ 형 변환시 int(변수), float(변수) 와 같이 `자료형(변수명)`으로 바꾼다
+ 파이썬의 실수는 float 형이다
+ 여러개의 값을 입력받고 싶을 땐 split을 사용
```python
a, b = input().split() # 공백을 기준으로 값을 나눔
c, d = input().split(',') # ,를 기준으로 값을 나눔
```
+ 값 사이마다 넣고 싶은 문자가 있다면 sep을 사용
```python
print(a, b, sep =":") # 콜론을 사이에 두고 a와 b를 출력
```