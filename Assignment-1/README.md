# Yelp Review Classifier

I devloped a classifier for yelp reviews using scikit learn libraries with logistic regression by finding the polarities of the reviews. we first preprocess the data and train the data on logistic regression model. the polarities of the reviews is found by using the set of poitive and negetive words. I obtained the accuracy as 70%.
 

# Getting Started

we first install the scikit learn library and tabulate library. using commands,
```
pip install scikit-learning
pip install tabulate
```

# Pre-Processing

* Remove punctuations from all the reviews
* Change all the charecters in reviews to lower case letters
* Break the scentences into tokens 
* Rmove the neutral words without polarity such as "is, the, a, an" etc
