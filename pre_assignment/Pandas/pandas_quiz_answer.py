import pandas as pd

### 1. 데이터를 로드하세요. 데이터는 ","  기준으로 구분되어 있습니다.
# 데이터 출처 : https://www.kaggle.com/code/youngprize33/py-pandas-tutorial/input?select=games.csv
# lol.csv 파일을 불러와서 df 변수에 저장합니다.

df = pd.read_csv('\lol.csv')

### 2. 데이터의 상위 5개 행을 출력하세요

print(df.head())

### 3. 6번째 컬럼명을 출력하세요

print(df.columns[5])

### 4. 6번째 컬럼의 데이터 타입을 확인하세요

print(df.dtypes[5])

### 5. 6번째 컬럼의 3번째 값은 무엇인가?

print(df.loc[2,df.columns[5]])

### 6. 수치형 변수를 가진 컬럼을 출력하세요

z = df.select_dtypes(include=['int64','float64'])
print(z.columns)

### 7. 각 수치형 변수의 분포(사분위, 평균, 표준편차, 최대 , 최소)를 확인하세요

print(df.describe())

### 8. map을 활용하여 결과 화면과 같이 나타내세요.

df= pd.read_csv(r'\NA_handling_method.csv', encoding='cp949')
print('Original Dataframe')
print(df,end='\n\n')
def f1(x):
    x = x.split()[0]
    return x


df['Argument'] = df['Description'].map(f1)

def f2(x):
    x = x.split()[1:]
    x = " ".join(x)    
    return x

df['Description'] = df['Description'].map(f2)

df = df.reindex(columns=['Argument', 'Description'])

print('New DataFrame')
print(df)

### 9. 결측값 데이터를 처리하는 함수들을 활용하여 결과 화면과 똑같이 나타내세요.

from numpy import nan as NA

data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],
                     [NA, NA, NA], [NA, 6.5, 3.]])
print('Original DataFrame')
print(data, end='\n\n')

cleaned = data.dropna(axis=0) 
print('결측값을 제거하세요')
print(cleaned, end='\n\n')

filled = data.fillna(0)
print('결측값을 0으로 채우세요.')
print(filled, end='\n\n')

filled2 = data.fillna({1:0.5, 2:1})
print('컬럼 1의 결측값은 0.5, 컬럼 2의 결측값은 1로 채우세요')
print(filled2, end='\n\n')

### 10. Filtering 기법을 사용하여 결과 화면과 똑같이 나타내세요.

import numpy as np

data = pd.read_csv(r'quiz\filtering.csv')
print(data.columns)
data.describe()

print('"0" 컬럼의 값이 -2.5보다 작거나 2.5보다 큰 row만 남깁니다.')
k = data[(data['0'] < -2.5) | (data['0'] > 2.5)]
print(k)
