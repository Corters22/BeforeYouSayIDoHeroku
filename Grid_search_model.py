import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

#//////////////////////////////////////////
# Read in csv
#//////////////////////////////////////////

df = pd.read_csv('divorce_data.csv', delimiter=';')
df.head()

#///////////////////////////////////////////
# Pull Important feature questions from random forest model
#///////////////////////////////////////////
df = df[['Q40', 'Q38', 'Q12', 'Q19', 'Q16', 'Q18', 'Q20', 'Q15', 'Q9', 'Q36', 'Divorce']]
df.head()

#///////////////////////////////////////////
# designate X and y for model
#///////////////////////////////////////////
X = df.drop('Divorce', axis=1)
y = df['Divorce']

#////////////////////////////////////////////
# Split data into training and testing
#///////////////////////////////////////////
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

#////////////////////////////////////////////
# Create the SVC Model
#////////////////////////////////////////////
from sklearn.svm import SVC 
model = SVC(kernel='linear')

#/////////////////////////////////////////////
# Create the GridSearch estimator along with a parameter object containing the values to adjust
#/////////////////////////////////////////////
from sklearn.model_selection import GridSearchCV
param_grid = {'C': [1, 5, 10, 50],
              'gamma': [0.0001, 0.0005, 0.001, 0.005]}
grid = GridSearchCV(model, param_grid, verbose=3)

#///////////////////////////////////////////////
# Fit the model using the grid search estimator. 
# This will take the SVC model and try each combination of parameters
#//////////////////////////////////////////////
grid.fit(X_train, y_train)

# List the best parameters for this dataset
print(grid.best_params_)

# List the best score
print(grid.best_score_)

#///////////////////////////////////////////////
# Make predictions with the hypertuned model
#//////////////////////////////////////////////
predictions = grid.predict(X_test)

#///////////////////////////////////////////////
# Calculate classification report
#//////////////////////////////////////////////
from sklearn.metrics import classification_report
print(classification_report(y_test, predictions, 
                           target_names=['Divorced', 'Happily Married']))


#//////////////////////////////////////////////
# Testing model on new data
#/////////////////////////////////////////////
def make_prediction(answers):
    # my_answers = [1, 0, 4, 4, 3, 4, 4, 3, 3, 0]
    pred_columns = X.columns

    #Transposing list of answers to dataframe to match model shape
    pred_df = pd.DataFrame(answers).transpose()
    pred_df.columns = pred_columns

    # making prediction on new data
    prediction = grid.predict(pred_df)

    return prediction

#///////////////////////////////////////////////
# Saving model to use later
#//////////////////////////////////////////////

# save your model by updating "your_name" with your name
# and "your_model" with your model variable
# be sure to turn this in to BCS
# if joblib fails to import, try running the command to install in terminal/git-bash
import joblib
filename = 'grid_search.sav'
joblib.dump(grid, filename)





