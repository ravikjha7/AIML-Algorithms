import numpy as np

outputs_desired = 1 
outputs = {1:1,2:1,3:0,4:1}
learning_constant = 0.8
x = {0:1,1:1,2:1,3:0,4:1}
errors = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}

weights =   [
                {}, #0
                {5:0.3,6:0.1}, #1
                {5:-0.2,6:0.4}, #2
                {5:0.2,6:-0.3}, #3
                {5:0.1,6:0.4}, #4
                {7:-0.3}, #5
                {7:0.2}, #6
                {}, #7
            ]

biases = {
    5 : 0.2 ,
    6 : 0.1 ,
    7 : -0.3
}

edges = {
    5 : [1,2,3,4],
    6 : [1,2,3,4],
    7 : [5,6]
}

hidden_layer_nodes = [5,6]
output_layer_nodes = [7]

def error_outputs_layer(k) : 
    return outputs[k]*(1-outputs[k])*(outputs_desired-outputs[k])

def error_hidden_layer(j) : 
    sum = 0 
    for k in output_layer_nodes : 
        sum = sum + errors[k]*weights[j][k] 
    error = outputs[j]*(1-outputs[j])*sum

    return error

def update_weights() : 
    for i in range(len(weights)) : 
        for j in weights[i] : 
            weights[i][j] =  weights[i][j] + learning_constant*errors[j]*outputs[i]

def update_bias() : 
    for j in biases : 
        biases[j] =  biases[j] + learning_constant*errors[j]

def x_sum(node) : 
    sum = biases[node]*x[0] 
    for i in edges[node] : 
        sum = sum + x[i]*weights[i][node]
    return sum

def sigmoid(x):
    return 1./(1.+np.exp(-x))

for __ in range(2) : 
     for i in hidden_layer_nodes : 
        x[i] = x_sum(i)
        outputs[i] = sigmoid(x[i])


     for i in output_layer_nodes : 
        x[i] = x_sum(i)
        outputs[i] = sigmoid(x[i])

    
     for i in output_layer_nodes : 
        errors[i] = error_outputs_layer(i)
    
     for i in hidden_layer_nodes : 
        errors[i] = error_hidden_layer(i)
    

     error_val = outputs_desired - outputs[7]

     update_weights() 
     update_bias()

     print("Error {} - {}".format(i+1,error_val))
     

print("\nFinal weights : ")

for i in range(len(weights)) : 
    for j in weights[i] : 
        print("{} - {} : {}".format(i,j,weights[i][j]))



    


