import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

dfTrain = pd.read_csv("q2_train.csv")
dfTest = pd.read_csv("q2_test.csv")

X = dfTrain.iloc[:, 0:len(dfTrain.columns)-1] 	  
Y = dfTrain['BUY'] 	  





unique_table = []
final_table = []
final_prob_table = []
    

def train_data() : 
    for i in range(len(dfTrain.columns)) : 
        arr = np.array(dfTrain.iloc[:, i:i+1] )
        # print(arr)
        cnt_unique = np.unique(arr)
        unique_table.append(cnt_unique)

    print(unique_table)
        

    for i in range(len(dfTrain.columns)) : 
        arr = np.array(dfTrain.iloc[:, i:i+1],dtype=int)
        ouput = np.array(dfTrain.iloc[:, -1],dtype=int)
        temp1 = [] 
        temp2 = [] 
        # print(i)
        for j in range(len(unique_table[i])) : 
            # print(j)
            temp1.append(0)
            temp2.append(0)

        for j in range(len(arr)) : 
            
            if ouput[j] == 0 :
                temp1[arr[j][0]]  = temp1[arr[j][0]]  + 1 
            else : 
                temp2[arr[j][0]]  = temp2[arr[j][0]]  + 1

        temp = [temp1,temp2]
        final_table.append(temp)

    

    for i in range(len(final_table)) : 
        temp1 = []
        temp2 = []
        for j in range(len(unique_table[i])) : 
            print(final_table[i][0][j]/final_table[-1][0][0])
            val = final_table[i][0][j]/final_table[-1][0][0]
            temp1.append(val)
        for j in range(len(unique_table[i])) : 
            print(final_table[i][1][j]/final_table[-1][0][0])
            val = final_table[i][1][j]/final_table[-1][1][1]
            temp2.append(val)
        
        temp = [] 
        temp.append(temp1)
        temp.append(temp2)

        final_prob_table.append(temp)
    print(final_table)
    print(final_prob_table)

def predict(features) : 
    # print("final = ",final_table)
    yes = final_table[-1][1][1]/len(X)
    no = final_table[-1][0][0]/len(X)
    # print(yes)

    for i in range(len(final_table)-1) : 
        no = no*final_prob_table[i][0][features[i]]
        yes = yes*final_prob_table[i][1][features[i]]
        # print(yes)
    
    # print(yes)
    # print(no)
    if yes > no : 
        return 1
    else : 
        return 0

def test_data() : 
    X = dfTrain.iloc[:, 0:len(dfTrain.columns)-1] 	  
    Y = dfTrain.iloc[:, -1]
    Y_predict = []
    for i in range(len(X)) : 
        features = dfTrain.iloc[i, 0:len(dfTrain.columns)-1]
        # print(type(features.values))
        predicted_val = predict(features.values)
        Y_predict.append(predicted_val)
        print(predicted_val,Y[i])
    

    
    ans = accuracy_score(Y, Y_predict)
    print(ans)

train_data()
test_data()




