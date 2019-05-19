import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.linear_model import SGDClassifier, LogisticRegression, PassiveAggressiveClassifier
from sklearn.model_selection import train_test_split

# Getting training data
train_dir = 'trainingdata.txt'
f = open(train_dir, "r")
data = []
for x in f:
    data.append(x.replace('\n',' '))
doclen = data[0]
del data[0]

train_X = []
train_y = []
for x in data:
    yv = int(x[0])
    train_y.append(yv)

    newX = x
    train_X.append(newX)

# Get Pred Data
temp=[]
sample_input = input()
try:
    while (sample_input != ''):
        temp.append(sample_input)
        sample_input = input()
except:
    pass

pred_data_raw = temp
dblen = pred_data_raw[0]
del pred_data_raw[0]

pred_data = []
for x in pred_data_raw:
    pred_data.append(x)

# Naive Bayesian Classifier
# Vectorize Text Information
text_clf = Pipeline([('vect', CountVectorizer(lowercase=False, analyzer='char_wb')), ('tfidf', TfidfTransformer()), ('clf', SGDClassifier(loss='hinge', penalty='l2', warm_start=True, alpha=1e-27, n_iter=2000, random_state=42, fit_intercept=False, n_jobs=-1, learning_rate='optimal', epsilon=0.001, shuffle=False))])

X_train, X_test, y_train, y_test = train_test_split(train_X, train_y, test_size=0.3, shuffle=False)

text_clf = text_clf.fit(X_train, y_train)

results = text_clf.predict(pred_data_raw)
for x in results:
    print(x)
