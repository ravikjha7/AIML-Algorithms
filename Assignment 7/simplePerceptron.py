import numpy as np

Dataset = [
[0,0,1],
[0,1,0],
[1,0,0],
[1,1,0]
]
wt1=0.3
wt2=-0.2
alpha = 0.2
def unitval(x):
	if x>=0:
		return 1
	else:
		return 0

def perceptron(x,w,b,val,alpha):
	sum = np.dot(w,x)+b
	ans = unitval(sum)
	err = val-ans
	for j in range(len(x)):
		w[j]=w[j]+alpha * err *x[j]
	return err

w = [wt1,wt2]
b = 0.4
err = 1
epochs=0
print("Training.....")

while(err):
	err = 0
	for i in range(len(Dataset)):
		x = Dataset[i][:-1]
		val = Dataset[i][-1]
		ans = perceptron(x,w,b,val,alpha)
		err = err or ans
	epochs+=1
	
print("Testing...")
print(" BELOW ARE THE WEIGHTS AFTER TRAINING: ")
print(w)
print("No of Iterations: ",epochs-1)