##[TODO 1]##
import numpy as np

xy = np.array([[1., 2., 3., 4., 5., 6.],
              [10., 20., 30., 40., 50., 60.]])

## 코드시작 ##

x_train = xy[0,:]    # ... 에 알맞은 코드를 작성해보세요.

y_train = xy[1,:]    # ... 에 알맞은 코드를 작성해보세요.


## 코드종료 ##

print(x_train, x_train.shape)
print(y_train, y_train.shape)

##[TODO 2]##
## 코드시작 ##
beta_gd = np.random.rand(1)
bias = np.random.rand(1)




## 코드종료 ##

print(beta_gd, bias)

##[TODO 3]##

learning_rate = 0.001

## 코드시작 ##
for i in range(1000):
    prediction = beta_gd * x_train + bias
    
    error = y_train - prediction
    
    cost = np.mean(np.square(error))
    
    weight_gradient = -(2/len(x_train)) * sum(x_train * error)  
    bias_gradient = -(2/len(x_train)) * sum(error) 
    
    weight = beta_gd - learning_rate * weight_gradient
    bias = bias - learning_rate * bias_gradient
    
    if i % 100 == 0 or i == 999:
        print(f"Epoch ({i}/1000) cost: {cost:.6f}, w: {weight[0]:.6f}, b: {bias[0]:.6f}")
## 코드종료 ##
