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
* Change all the characters in reviews to lower case letters
* Break the sentences into tokens 
* Remove the neutral words without polarity such as "is, the, a, an" etc

After the preprocessing, the tokens are then compared with a set of positive and negative words to assign scores. If token is present in Positive words a score of '1' is assigned, for negative a score of '-1' is assigned and if token is not present in both sets, then a score of '0' is assigned. Based on these token scores, the mean score for each review is calculated. The value of mean score helps us to label each review as "Positive", "Negative" or "Neutral"

# Building the Model

To build the Logistic Regression model, we use:
1. Countvectorizer
2. Tfidftransformer
3. Logistic Regression Algorithm
