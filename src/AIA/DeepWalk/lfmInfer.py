with open('./lastfm_target.txt') as tfile:
    Lines = tfile.readlines()
    target=[]
    for line in Lines:
        arr=line.strip().split(',')
        target.append(int(arr[1]))

print(len(target))

with open('./lastfm_64.emd') as embfile:
    LEmb=embfile.readlines()
    emb={}
    keys=[]
    for line in LEmb:
        arr=line.strip().split()
        keys.append(int(arr[0]))
        emb[int(arr[0])]=arr[1:]


print(len(emb))
X=[]
y=[]
for i in keys:
    emb[i]= map(float,emb[i])
    X.append(emb[i])
    y.append(target[i])

print(len(X))
print(len(y))


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)


# ######################################################################

from sklearn import metrics
from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(solver='adam', alpha=1e-4, hidden_layer_sizes=(64,32,16,18), random_state=1,max_iter=200)

mlp.fit(X_train, y_train)

print("Training set score: %f" % mlp.score(X_train, y_train))
print("Test set score: %f" % mlp.score(X_test, y_test))

y_score = mlp.predict(X_test)
print(metrics.f1_score(y_test, y_score, average='micro'))
print(metrics.classification_report(y_test, y_score, labels=range(18)))

# ######################################################################

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(max_depth=150, random_state=0)
rf.fit(X_train, y_train)

print("Training set score: %f" % rf.score(X_train, y_train))
print("Test set score: %f" % rf.score(X_test, y_test))

y_score = rf.predict(X_test)
print(metrics.f1_score(y_test, y_score, average='micro'))
print(metrics.classification_report(y_test, y_score, labels=range(18)))

# ######################################################################

from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC


svm = OneVsRestClassifier(SVC(kernel='rbf'))
svm.fit(X_train, y_train)

print("Training set score: %f" % svm.score(X_train, y_train))
print("Test set score: %f" % svm.score(X_test, y_test))

y_score = svm.predict(X_test)
print(metrics.f1_score(y_test, y_score, average='micro'))
print(metrics.classification_report(y_test, y_score, labels=range(18)))
