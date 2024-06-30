""" Machine Learning Assignment : 14 

     There is one data set of wether conditions. 
    That dataset contains information as wether and we have to decides whether to play or 
    not. 
    
Data set contains the target variable as Play which indicates whether to play or not. 
Consider below Play Predictor Dataset as

PlayPredictor.csv

,Whether,Temperature,Play
1,Sunny,Hot,No
2,Sunny,Hot,No
3,Overcast,Hot,Yes
4,Rainy,Mild,Yes
5,Rainy,Cool,Yes
6,Rainy,Cool,No
7,Overcast,Cool,Yes
8,Sunny,Mild,No
9,Sunny,Cool,Yes
10,Rainy,Mild,Yes
11,Sunny,Mild,Yes
12,Overcast,Mild,Yes
13,Overcast,Hot,Yes
14,Rainy,Mild,No
15,Rainy,Mild,Yes
16,Rainy,Cool,Yes
17,Rainy,Cool,No
18,Overcast,Cool,Yes
19,Sunny,Mild,No
20,Sunny,Cool,Yes
21,Rainy,Mild,Yes
22,Sunny,Mild,Yes
23,Sunny,Hot,No
24,Sunny,Hot,No
25,Overcast,Hot,Yes
26,Rainy,Mild,Yes
27,Rainy,Cool,Yes
28,Overcast,Cool,Yes
29,Sunny,Mild,No
30,Sunny,Cool,Yes

Step 1: 
Get Data 
Load data from PlayPredictor.csv file into python application. 
Step 2: 
Clean, Prepare and Manipulate data 
As we want to use the above data into machine learning application we have prepare 
that in the format which is accepted by the algorithms. 
As our dataset contains two features as Wether and Temperature. We have to replace 
each string field into numeric constants by using LabelEncoder from processing module 
of sklearn. 
Step 3: 
Train Data 
Now we want to train our data for that we have to select the Machine learning algorithm. 
For that we select K Nearest Neighbour algorithm. 
use fit method for training purpose. For training use whole dataset. 
Step 4: 
Test Data 
After successful training now we can test our trained data by passing some value of 
wether and temperature. 
As we are using KNN algorithm use value of K as 3. 
After providing the values check the result and display on screen. 
Result may be Yes or No. 
Step 5: 
Calculate Accuracy 
Write one function as CheckAccuracy() which calculate the accuracy of our algorithm. 
For calculating the accuracy divide the dataset into two equal parts as Training data and 
Testing data. 
Calculate Accuracy by changing value of K. 

"""
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def PlayPredictor():
    data = pd.read_csv(r"C:\Users\NAVNATH\OneDrive\Desktop\Py\assignments\Machine Learning Assignments 14-\PlayPredictor.csv")
    # print("original data")
    # print(data)
    # print(data.describe())
    l = LabelEncoder()
    # Correct usage of fit_transform method
    data["Whether"] = l.fit_transform(data["Whether"])
    data["Temperature"] = l.fit_transform(data["Temperature"])

    print("Encoded Data:")
    print(data)
    
    x = data.drop("Play", axis=1)
    y = data["Play"]
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    
    knn = KNeighborsClassifier(n_neighbors=3)
    
    knn.fit(x_train, y_train)
    
    y_pred = knn.predict(x_test)
    
    
    
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

def main():
    print("--------------predict from weather and go for play or not -------------")
    
    PlayPredictor()


if __name__ == "__main__":
    main()






