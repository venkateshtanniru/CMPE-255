# Yelp Review Classifier

I devloped a classifier for yelp reviews using scikit learn libraries with logistic regression by finding the polarities of the reviews. we first preprocess the data and train the data on logistic regression model. the polarities of the reviews is found by using the set of poitive and negetive words. I obtained the accuracy as 70%.
 

## Getting Started

we first install the scikit learn library and tabulate library. using commands,
```
pip install scikit-learning
pip install tabulate
```

## Pre-Processing

Pre-Processing of the reviews consists of:

* Remove punctuations from all the reviews
* Change all the characters in reviews to lower case letters
* Break the sentences into tokens 
* Remove the neutral words without polarity such as "is, the, a, an" etc

After the preprocessing, the tokens are then compared with a set of positive and negative words to assign scores. If token is present in Positive words a score of '1' is assigned, for negative a score of '-1' is assigned and if token is not present in both sets, then a score of '0' is assigned. Based on these token scores, the mean score for each review is calculated. The value of mean score helps us to label each review as "Positive", "Negative" or "Neutral"

## Building the Model

To build the Logistic Regression model, we use:
1. Countvectorizer
2. Tfidftransformer
3. Logistic Regression Algorithm

## Training and Testing

45,000 Reviews were taken from the dataset to train and test the model. These were randomly split in the ratio of 80-20 as training and test data respectively. we first train the model and that model is used to test the test data. we first apply cross validation and calculate the accuracy based on the results of the data.

## Results

```

 |   Predicted |   Actual | Business_id            | Result   |
|-------------+----------+------------------------+----------|
|     3.31151 |  3.63095 | RESDUcs7fIiihp38-d6_6g | correct  |
|     3.46875 |  4.11667 | 4JNXUYY8wbaaDmk3BPzlWw | correct  |
|     3.369   |  3.71616 | K7lWdNUhCbcnEvI0NhGewg | correct  |
|     3.13636 |  3.9798  | cYwJA2A6I12KNkm2rtXd5g | wrong    |
|     2.97135 |  4.27083 | DkYS3arLOhA8si5uUEmHOw | wrong    |
|     3.01453 |  3.90116 | f4x1YBxkLrZg652xt2KR5g | wrong    |
|     2.73052 |  3.9026  | 5LNZ67Yw9RD6nf4_UhXOjw | wrong    |
|     3.02632 |  3.40132 | SMPbvZLSMMb7KU76YNYMGg | correct  |
|     3.21812 |  3.44295 | ujHiaprwCQ5ewziu0Vi9rw | correct  |
|     3.12847 |  3.61806 | 2weQS-RnoOBhb1KsHKyoSQ | correct  |

```
