# Dependencies
import pandas as pd
import numpy as np

class Divorce_Data():

    def questions(self):
        results = pd.read_csv("divorce_data.csv")
        quest = results.to_dict('results')
        return(quest)