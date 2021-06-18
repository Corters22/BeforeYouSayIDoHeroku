
from sklearn import tree
import pandas as pd
import os


df = pd.read_csv(os.path.join('..','divorce_data.csv'),sep=";")
# Drop the null columns where all values are null
df = df.dropna(axis='columns', how='all')
# Drop the null rows
df = df.dropna()
df.head()


target = df["Divorce"]
data = df.drop("Divorce", axis=1)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=42)


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
clf.score(X_test, y_test)


from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=200)
rf = rf.fit(X_train, y_train)
rf.score(X_test, y_test)


#/////////////////////////////////////////////////////////
#Pulling out important features and the full questions for app
#/////////////////////////////////////////////////////////

question_data = pd.read_csv('../reference.tsv', delimiter='|')
question_data


feature = df.columns

imp_features = sorted(zip(rf.feature_importances_, feature), reverse=True)
imp_features = pd.DataFrame(imp_features)


imp_features = imp_features.rename(columns = { 0: 'importance_score', 1: 'atribute_id'})
imp_features['atribute_id'] = imp_features['atribute_id'].str.replace('Q', '').astype('int64')
imp_features.head(10)


merged_df = pd.merge(imp_features, question_data, on="atribute_id")
merged_df.head(10)


feature_questions = []
i=0
for i in range(len(merged_df)):
    question = merged_df.iloc[i, 2]
    feature_questions.append(question)

feature_questions





