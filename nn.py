from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils.generic_utils import get_custom_objects
import numpy


numpy.random.seed(70)  # set seed for reproducibility

train_x = []

for i in range(100000):
    # append lists of two random numbers to the values for train_x
    train_x.append(numpy.random.randint(-20, 20, size=2))

train_y = []

for i in train_x:
    train_y.append(i[0] + i[1])  # append sums to train_y

train_y = numpy.array(train_y)
train_x = numpy.array(train_x)

model = Sequential()
model.add(Dense(4, input_dim=2))  # input and first hidden layer
# linear activation because "infinite" range of answers
model.add(Activation('linear'))
model.add(Dense(1))  # output layer with one answer neuron
#model.add(Activation('linear'))
model.compile(optimizer='adam', loss='mse')  # optimizer and loss
model.fit(train_x, train_y, validation_split=0.01, epochs=20)  # train the model


correct = 0
tests=10000
for i in range(tests):
    test = numpy.array([numpy.random.randint(-100000, 100000, size=2)])
    numbers = test[0][0]
    print("Test Case: ", str(test[0][0])+"+"+str(test[0][1]))
    prediction = round(model.predict(test)[0][0])
    print("Result: ", prediction)
    if test[0][0]+test[0][1] == prediction:
        correct += 1
        print("Correct")
    else:
        print("Wrong")
    print("\n")

print("\n\n\n\n")
print("Accuracy: "+ str(int(correct*100/tests))+"%")