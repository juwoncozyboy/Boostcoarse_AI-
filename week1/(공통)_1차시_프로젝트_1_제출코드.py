## TODO1 ##
import sys
print(sys.version)

## TODO1 ##
import pandas as pd

## 코드시작 ##

df_csv = pd.read_csv('/Users/juwonkim/Desktop/네이버 부스트코스 AI 엔지니어/1주차/(공통) 1차시_프로젝트 1 코드자료/zen of python.csv')

## 코드종료 ##

print(df_csv)

## TODO1 ##
#pip install numpy
import numpy as np

# 주어진 리스트
data = [10, 25, 40, 55, 70]

## 코드시작 ##
# 1. numpy 배열로 변환하여 출력하세요.
array = np.array(data)
print(array)

# 2. 리스트의 모든 원소의 합을 계산하여 출력하세요.
sums = np.sum(array)
print(sums)
# 3. 리스트의 모든 원소의 평균을 계산하여 출력하세요.
means = np.mean(array)
print(means)
# 4. 리스트의 최댓값과 최솟값을 출력하세요.
mins = np.min(array)
print(mins)
maxs = np.max(array)
print(maxs)

# 5. 각 원소를 10으로 나누는 연산을 수행하고 결과를 출력하세요.
divide = array / 10
print(divide)
# 6. 각 원소를 3으로 거듭제곱하는 연산을 수행하고 결과를 출력하세요.
cubed = array ** 3
print(cubed)
## 코드종료 ##