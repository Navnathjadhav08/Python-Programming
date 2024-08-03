""" Machine Learning Assignment : 15

    There is one data set of wine which classify the wines according to its contents into three 
classes. 
Consider below Wine Dataset as

PlayPredictor.csv

These data are the results of a chemical analysis of wines grown in the same region in Italy 
but derived from three different cultivars. The analysis determined the quantities of 13 
constituents found in each of the three types of wines. 
Wine data set contains 13 features as 
    1) Alcohol 
    2) Malic acid 
    3) Ash 
    4) Alcalinity of ash 
    5) Magnesium 
    6) Total phenols 
    7) Flavanoids 
    8) Nonflavanoid phenols 
    9) Proanthocyanins 
    10)Color intensity 
    11)Hue 
    12)OD280/OD315 of diluted wines 
    13)Proline 
According to the above features wine can be classified as 
• Class 1 
• Class 2 
• Class 3

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


from sklearn import metrics
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


def WinePredictor():
    # load Dataset
    
    wine = datasets.load_wine()
    
    #print the names of the features
    print(wine.feature_names)
    
    #print the label species(class_0,class_1,class_2)
    print(wine.target_names)
    
    #print the wine data (top 5   records)
    print(wine.data[0:5])
    
    # print the wine labels (0:class_0,1:class_1,2:class_2)
    print(wine.target)
    
    #SPLITTING dataset into training set and test set
    X_train,X_test,Y_train,Y_test = train_test_split(wine.data,wine.target,test_size=0.3)#70% training and 30% test
    
    # create KNN classifier
    knn = KNeighborsClassifier(n_neighbors=3)
     
    #Train the model using the training sets
    knn.fit(X_train,Y_train)
    
    #predict the response for test dataset
    y_pred = knn.predict(X_test)
    
    #Model Accuracy , how often is the classifier correct?
    print("Accuracy : ",metrics.accuracy_score(Y_test,y_pred))
    
     


def main():
    print("Machine Learning Application")
    
   
    print("Wine predictor application using k Nearest knighbor algorithm")
    
    WinePredictor()


if __name__ == "__main__":
    main()




