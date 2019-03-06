import pandas as pd

data =  pd.read_csv(r'yelp_review.csv',encoding = "utf8",keep_default_na=False,nrows=200000)


from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)
data.to_sql('yelp_reviews',con=engine)

data.head()


data.shape

reviews = data[:45000]["text"]
reviews.head()


import string
from nltk.corpus import stopwords

def tokenize_reviews(review):
    rev = [char for char in review if char not in string.punctuation]
    rev = ''.join(rev)
    
    return [word for word in rev.split() if word.lower() not in stopwords.words('english')]

print(tokenize_reviews(reviews[0]))


rev_tokens = []
dataset = []
for review in reviews:
    if len(review) > 10:
        rev_tokens.append(tokenize_reviews(review))
        dataset.append(review)




print(rev_tokens[44998])




file = open(r'pos_words.txt')
positive  = file.read()
positive = positive.lower()
file = open(r'neg_words.txt')
negative  = file.read()



def assign_score(token):
    score = []
    for word in token:
        if word in positive:
            score.append(1)
        elif word in negative:
            score.append(-1)
        else:
            score.append(0)
    return score


rev_scores = []
for token in rev_tokens:
    rev_scores.append(assign_score(token))

from statistics import mean
labels = []
pos = neg = neut = 0         
for score in rev_scores:
    if score:
        val =  mean(score)
        if val > 0.29:
            labels.append(1)
            pos += 1
        elif 0.212 <= val <= 0.29:
            labels.append(0)
            neut += 1
        else:
            labels.append(-1)
            neg += 1
    else:
        labels.append(0)

print(pos,neg,neut)



from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(dataset,labels,test_size=0.25,random_state=42)



from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsOneClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer,CountVectorizer

nb = Pipeline([('vect', CountVectorizer(analyzer = 'word',lowercase = True,stop_words='english')),
               ('tfidf', TfidfTransformer(smooth_idf=True)),
               ('clf', LogisticRegression(penalty='l2',solver='newton-cg',multi_class='multinomial')),
              ])
nb.fit(x_train, y_train)


from sklearn.model_selection import cross_val_score
scores = cross_val_score(nb, x_train,y_train , cv=5)
print(scores)

y_pred = nb.predict(x_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)



y_pred = []
y_pred = nb.predict(x_test)
from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))



import heapq
counter = []
counter = engine.execute("SELECT COUNT(*) AS count,business_id FROM yelp_reviews GROUP BY business_id").fetchall()
rest = heapq.nlargest(10,counter)



results = []
correct = 0
for count,id in rest:
    data_base = []
    stars = []
    prediction = ""
    data_base = engine.execute("SELECT text from yelp_reviews where business_id = ?",(id)).fetchall()
    stars = engine.execute("SELECT stars as INTEGER from yelp_reviews where business_id = ?",(id)).fetchall()
    new_db = []
    stars_db = []
    for data in data_base:
        new_db.append(str(data))

    for star in stars:
        stars_db.append(star[0])
        
    ypred = nb.predict(new_db)
    y_pred_new = []
    for pred in ypred:
        if pred == 0:
            y_pred_new.append(3.5)
        elif pred == -1:
            y_pred_new.append(1.5)
        else:
            y_pred_new.append(5)
        
#         print(y_pred_new)
    predicted = mean(y_pred_new)
    actual = mean(stars_db)
    if abs(predicted - actual) < 0.7:
        prediction = "correct"
        correct += 1
    else:
        prediction = "wrong"
    results.append([predicted,actual,id,prediction])



from tabulate import tabulate
print(tabulate(results,headers=['Predicted', 'Actual', 'Business_id','Result'], tablefmt='orgtbl'))





