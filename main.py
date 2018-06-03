from sklearn import tree

# [height, weight, shoe size]
X = [[180, 80,40],[176, 76,38],[185, 85,42],[190, 90,44],[195, 95,47],[170, 70,35],[160, 60,30],[150, 50,25],[165, 65,33],[182, 82,41],[177, 77, 38]]

y = ['male','male','male','male','male','female','female','female','female','male','male']

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(X,y)

predict = classifier.predict([[200,100,50]])
print(predict) 

# Prints ['male']