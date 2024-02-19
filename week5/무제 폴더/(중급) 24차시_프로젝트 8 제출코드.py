# 재현을 위해 필요한 코드 및 함수들을 다시 정의하고 실행해 보겠습니다.

import numpy as np

# 입력 데이터
X = np.array([0, 0, 1, 1, 0, 1, 0, 1]).reshape(2,4)  # 입력 데이터
Y = np.array([0, 1, 1, 0]).reshape(1,4)  # 정답 레이블

# 가중치 초기화 함수
def init_parameters(num_hidden_units=2):
    W1 = np.random.randn(num_hidden_units, 2)  # 첫번째 레이어 가중치
    B1 = np.zeros((num_hidden_units, 1))  # 첫번째 레이어 바이어스
    W2 = np.random.randn(1, num_hidden_units)  # 두번째 레이어 가중치
    B2 = np.zeros((1, 1))  # 두번째 레이어 바이어스
    return W1, B1, W2, B2

# Affine 변환 함수
def affine(W, X, B):
    return np.dot(W, X) + B

# Sigmoid 함수
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 이진 크로스 엔트로피 손실 함수
def binary_cross_entropy(Y, YHat):
    N = Y.shape[1]  # 총 샘플의 수
    loss = -(1/N) * np.sum(Y * np.log(YHat) + (1 - Y) * np.log(1 - YHat))
    return loss

# 순방향 연산 및 손실 계산
def forward_loss(X, Y, _params):
    W1, B1, W2, B2 = _params

    # 첫번째 레이어 연산
    Z1 = affine(W1, X, B1)  # 1) affine 함수
    H = sigmoid(Z1)  # 2) sigmoid 함수

    # 두번째 레이어 연산
    Z2 = affine(W2, H, B2)  # 3) affine 함수
    YHat = sigmoid(Z2)  # 4) sigmoid 함수

    # 손실함수 계산
    loss = binary_cross_entropy(Y, YHat)  # 5) 이진 크로스 엔트로피 함수

    return Z1, H, Z2, YHat, loss

# 파라미터 초기화 및 손실 계산
np.random.seed(42)
W1, B1, W2, B2 = init_parameters(num_hidden_units=2)
result = forward_loss(X, Y, [W1, B1, W2, B2])[-1]

def get_gradients(X, Y, _params):
    W1, B1, W2, B2 = _params
    m = X.shape[1]  # 샘플의 수

    # 포워드 패스
    Z1, H, Z2, YHat, loss = forward_loss(X, Y, _params)

    # dLoss/dZ2
    dLdZ2 = (1/m) * (YHat - Y)

    # dLoss/dW2
    dLdW2 = np.dot(dLdZ2, H.T)

    # dLoss/dB2
    dLdB2 = np.sum(dLdZ2, axis=1, keepdims=True)

    # dLoss/dH
    dLdH = np.dot(W2.T, dLdZ2)

    # dLoss/dZ1
    dLdZ1 = dLdH * H * (1 - H)

    # dLoss/dW1
    dLdW1 = np.dot(dLdZ1, X.T)

    # dLoss/dB1
    dLdB1 = np.sum(dLdZ1, axis=1, keepdims=True)

    return [dLdW1, dLdB1, dLdW2, dLdB2], loss

# 모델 학습하기
def optimize (X, Y, _params, learning_rate = 0.1, iteration = 1000):

    params = [np.copy(param) for param in _params] # 파라미터 복사
    loss_trace = [] # 손실 값 저장

    for epoch in range(iteration): # 학습 반복
        dparams, loss = get_gradients(X, Y, params) # 그레디언트 추출
        for param, dparam in zip(params, dparams):
            param += - learning_rate * dparam # 경사하강법 구현

        if (epoch % 100 == 0): # 손실값 저장
            loss_trace.append(loss)

    Z1, H, Z2, Y_hat_predict, loss = forward_loss(X, Y, params)


    return params,loss_trace, Y_hat_predict


X = np.array([0, 0, 1, 1, 0, 1, 0, 1]).reshape(2,4) # 입력
Y = np.array([0, 1, 1, 0]).reshape(1,4) # 정답

params = init_parameters(2) # 파라미터 세팅
new_params, loss_trace, Y_hat_predict = optimize(X, Y, params, 0.1, 150000) # 학습 및 추론

print(Y_hat_predict) # 정답 Y와 유사한 값이 나왔다면 학습이 잘 진행된 것 입니다.

# 손실함수 값 출력하기
import matplotlib.pyplot as plt

# Plot learning curve (with costs)
plt.plot(loss_trace)
plt.ylabel('loss')
plt.xlabel('iterations (per hundreds)')
plt.show()

