import sys
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.feature_extraction.text import HashingVectorizer
transformer=HashingVectorizer(stop_words='english')

transformer=HashingVectorizer(stop_words='english')

X_train = []
y_train = []

f = open('apple-computers.txt')

try:
	while (True):
		s = f.readline()
		if not s:
            break
		s = s.rstrip()
		if len(s) < 100:
            continue
		X_train.append(s)
		y_train.append(1)
except EOFError:
	pass

f.close()

f = open('apple-fruit.txt')

try:
	while (True):
		s = f.readline()
		if not s:
            break
		s = s.rstrip()
		if len(s) < 100:
            continue
		X_train.append(s)
		y_train.append(2)
except EOFError:
	pass

f.close()

train_X = transformer.fit_transform(X_train)

model = BernoulliNB(alpha=0.06)
model.fit(train_X, y_train)

#get prediction values
preds = []
for i in range(int(input)):
    s = input().rstrip()
    preds.append(s)

preds_X = transformer.transform(preds)
results = model.predict(preds_X)
for res in results:
    print(res)