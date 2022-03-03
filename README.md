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
+ 문자열은 인덱싱, 슬라이싱 가능

### 값변환
+ 16진수 입력받기
```python
a = input()
a = int(a, 16)
```
+ 서식 지정자로 8진수 출력하기
```python
print("%o" % a)
```
+ 문자를 10진수 유니코드 **값**으로 변환하려면 `ord()` 사용 (A → 65) (str → int)
+ 정수 값을 입력받아 유니코드 **문자**로 변환하려면 `chr()` 사용 (65 → A) (int → str)
+ 실수 원하는 자리까지 출력하기
```python
a = 3.141592
print(format(a, ".2f")) # 3.14
```

### 출력변환
+ 서식 지정자로 16진수 출력하기
```python
a = 255
print("%x" % a) # ff # 소문자로 출력
print("%X" % a) # FF # 대문자로 출력
```

### 산술연산
+ `문자열 * 정수` 또는 `정수 * 문자열`은 문자열을 정수만큼 반복한 문자열로 만들어준다
```python
w, n = input().split()
print(w * int(n))
```
+ 거듭제곱 연산자는 `**`
```python
print(a ** b) # a의 b승 출력
```
+ 몫 연산자는 `//`, 나머지 연산자는 `%`
```python
a = 10
b = 3
print(a // b) # 3
print(a % b) # 1
```
+ 반올림 함수 `round()`
    - 오사오입 원칙을 따른다
    - 5의 앞자리가 홀수인 경우엔 올림, 짝수인 경우엔 버림
```python
round(4.5) # 4
round(3.5) # 4

round(3.1415 , 2) # 3.14 # 소수점 이하 둘째 자리까지의 정확도로 출력
```

### 비트시프트연산
+ 비트단위 시프트 연산자 `<<, >>`
```python
n = 10

print(n << 1) # 10의 2배인 20 출력 
print(n >> 1) # 10의 1/2배인 5 출력
print(n << 2) # 10의 4(2^2)배인 40 출력
print(n >> 2) # 10의 1/4(2^-2)배인 2 출력 (반으로 나누고 한 번 더 나눔)
```

### 비교연산
+ 불(bool) 자료형은 True(참), False(거짓) 두개의 값만 가짐

### 논리연산
+ 파이썬에서 정수 0은 False(거짓)로 평가되고, 그 외의 값들은 모두 True(참)로 평가
+ 참 또는 거짓의 논리값을 반대로 바꾸기 위해서 `not` 을 사용
+ 불(bool) 값을 다루어주는 예약어는 not, and, or가 있다

### 비트단위논리연산
+ 비트단위 연산자는 `~(bitwise not)`, `&(bitwise and)`, `|(bitwise or)`, `^(bitwise xor)`, `<<(bitwise left shift)`, `>>(bitwise right shift)`가 있다.
+ -n = ~n + 1

### 3항연산
+ `x if C else y`의 형태로 작성
    - C: 조건식
    - x: C의 평가 결과가 True 일 때 사용할 값
    - y: C의 평가 결과가 False 일 때 사용할 값
+ 예시
```python
c = (a if (a>=b) else b)
# a, b 중 큰 값을 구하는 법
```