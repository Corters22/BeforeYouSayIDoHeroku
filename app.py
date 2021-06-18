# Dependencies
from flask import Flask, jsonify, render_template, request
from project import Divorce_Data
import pandas as pd
import numpy as np
import joblib
# import Grid_search_model 

#################################################
# Database Setup
#################################################   
data = Divorce_Data()
# grid_search = Grid_search_model
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

################################################
# adding model for predictions
################################################
model = joblib.load('grid_search.sav')


#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/api_options')
def api_list():   
    """List available api routes."""
    return (
        f"<h4>Available Routes:</h4>"       
        f'<a href="/api/divorcedata">Divorce Data</a><br/>' 
        f'<a href="/"><h4>Back</h4></a><br/>' 
        f'<a href="/prediction/<answers>'
    )    

@app.route("/api/divorcedata")
def demo():
    return jsonify(data.questions())

@app.route("/prediction", methods=['GET', 'POST'])
def prediction_gif():
    if request.method == 'POST':
        answers = [request.get_json()]
        df = pd.DataFrame(answers)
        predictions = model.predict(df)
        print(predictions)
        if predictions ==1:
            gif_url = 'static/images/avocado_love.gif'
        else:
            gif_url = 'static/images/broken_heart.gif'
      
    else:
        gif_url = 'error'
    
    return jsonify(gif_url)
    



@app.route('/visualizations')
def visualizations():
    return render_template('viz.html')


if __name__ == '__main__':
    app.run(debug=True)