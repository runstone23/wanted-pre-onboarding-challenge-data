import numpy as np

### 1. 값이 10~49인 numpy array를 만드세요

z = np.arange(10,50)
print(z)

### 2. z를 반전하세요.

a = np.sort(z)[::-1]
print(a)

### 3. 반전시킨 z 매트릭스를 10 x 4 매트릭스로 바꾸세요.

b = a.reshape(10,4)
print(b) 

### 4. x에서 0이 아닌 요소의 색인을 찾아보세요.

x = np.array([5,6,8,0,1,0,7])
nz_idx = np.where(x != 0)
print(nz_idx)

### nan 값 이해하기

print(np.nan == np.nan)  #False, nan은 자신과도 동일하지 않음
print(np.nan == None)  #False, nan은 None과도 당연히 동일하지 않음
print(np.nan is None)  #False
print(np.isnan(np.nan))  #isnan을 사용하면 nan값을 테스트 가능

import math
print(0.3 == 3 * 0.1)  #python에서는 소수 계산 시 부동 소수점이기에 정확하지 않음
print(math.isclose(0.1 + 0.2, 0.3))

### 5. 12 x 12 매트릭스를 만들어 바둑판 패턴으로 0과 1을 채우세요

x = np.zeros((12, 12))
print(x, end='\n\n')

x[::2,::2] = 1
x[1::2,1::2] = 1
x = 1 - x

print(x)

### 6. np.tile 을 이용해서 동일한 바둑판 배턴을 만들어보세요

a = np.array([[0,1],[1,0]])
x = np.tile(a,(6,6))
print(x)

### 7. 1차원 배열이 x에서 값이 5~10인 요소를 0으로 바꾸세요

x = np.array([2,5,3,8,3,34,23,7,10])
print(x)

a = (5 <= x)& (x <= 10)
x[a]=0

print(x)

### 8. 0에서 100 사이의 값으로 크기가 10인 1차원 array를 만드세요

y = np.random.rand(10) * 100  #임의의 값 추출
print(y)
x = np.random.randint(0,100,10)  #정수 값 추출
print(x)

### 9. np.allclose() 함수를 사용하여 2개의 array가 같은지를 확인해보세요

A = np.array([1e10,1e-8])
B = np.array([1.00001e10,1e-9])

equal = np.allclose(A, B)
print(equal)

### 10. 데카르트 좌표를 나타내는 랜덤 8 x 2 행렬을 고려하여 극좌표로 변환해보세요.

coord = np.random.random((10,2))
x, y = coord[:,0], coord[:,1]
r = np.sqrt(x**2+y**2)
theta = np.arctan2(x,y)
ploar_coord = np.concatenate([r[:,np.newaxis], theta[:,np.newaxis]],axis=1)
print(ploar_coord)
