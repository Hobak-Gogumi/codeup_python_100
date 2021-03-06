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

### 조건/선택실행구조
+ 조건문 형식
``` python
if 조건식1:
    실행문 # 조건식의 평가값이 True일 경우 실행시킬 명령을 들여쓰기로 적음
    ...
elif 조건식2:
    실행문
    ...
elif 조건식3:
    실행문
    ...
else:
    실행문
    ...
```
+ 조건문 안에 조건문을 여러 번 중첩할 수 있다
+ 한 소스코드 내에서 들여쓰기 길이와 방법은 같아야 한다
+ 들여쓰기를 기준으로 코드블록을 구분하므로, 들여쓰기를 정확히 해준다

### 반복실행구조
+ while문
```python
while 조건식:
    실행블록
# 조건식의 평가 결과가 True 동안만 들여쓰기 된 실행블록 반복 실행, False 인 경우 반복 중단
```
+ for문
```python
for i in range(n + 1):
    print(i)
# range는 숫자 리스트를 자동으로 만들어준다
# range(n)은 0, 1, 2, ..., n-2, n-1 까지의 수열
```

### 종합
+ 조건문이나 반복문의 코드블록 안에서 `continue`가 실행되면, 반복 블록 안에 있는 나머지 부분을 실행하지 않고, 다음 반복 단계로 넘어간다
```python
for i in range(1, n+1):
    if i % 2 == 0:
        continue       # 다음 반복 단계로 넘어간다
    print(i, end=' ')  # i가 짝수가 아닐때만 실행된다
# 홀수만 출력하는 예시
```

### 리스트
+ 앞에서 사용했던 `input().split()`의 결과는 문자열 리스트. 변수를 하나만 사용하면 공백을 기준으로 잘라 리스트에 저장한다
```python
a = input().split() # 공백을 기준으로 잘라 a에 순서대로 저장
```
+ 리스트는 대괄호`[]` 를 사용
+ 리스트에 마지막에 원하는 값을 추가할 때는 `append`를 사용
```python
d = []
d.append(2)
```
+ 원하는 요소에 접근할 때 인덱스 사용(번호는 0부터 시작)
+ for문을 사용하여 리스트에 있는 값 거꾸로 출력하기
```python
for i in range(n-1, -1, -1): # n은 리스트 크기. 세번째 인자는 증감
    print(a[i], end= " ")
```
+ 리스트의 최소값, 최대값을 구하려면 `min(리스트명)`, `max(리스트명)`을 사용
+ 2차원 리스트
    - 리스트가 들어있는 리스트를 만들면 2차원 리스트를 생성 가능
    - `리스트이름[번호][번호]` 형식으로 접근 가능
```python
d = []

for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

# 크기가 20 * 20 이고, 0으로 채워진 2차원 리스트 만들기

# d = [[0 for j in range(20)] for i in range(20)]
# 이렇게 간단히 생성도 가능(List Comprehensions)
```