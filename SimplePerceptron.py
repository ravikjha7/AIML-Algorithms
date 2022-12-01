import numpy as np

def activation_function(x):
    if x >= 0:
        return 1
    else :
        return 0

def run_perceptron(gate,desired_output):
    bias = 0.4 # the bias is always one
    learning_constant = 0.2
    weights = [0.3,-0.2]

    for _ in range(50) : 
        estimated_output = []
        for i in range(len(gate)) : 
            x = gate[i] 
            product = np.dot(x,weights) + bias 
            # print("i = ",i)
            # print("product = ",product)
            estimated_output.append(activation_function(product))
            error = desired_output[i]-estimated_output[i]
            # print("error = ",error)
            if(error != 0) : 
                # print(x,weights)
                for j in range(len(weights)) : 
                    weights[j] = weights[j] + learning_constant*error*x[j]
                break
            if i == len(gate)-1 : 
                print("estimated_output : " , estimated_output)
                print("desired_output : " , desired_output)
                print("final weights",weights)
                return 

nor_gate = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
nor_gate_output = [1, 0, 0, 0 ]

run_perceptron(nor_gate,nor_gate_output)