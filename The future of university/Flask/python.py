import numpy as np
from flask import Flask, request, jsonify, fender_template
import pickle
app = Flask(_name_)
#import necessary libraries
form tensorflow.keras.modesls import load_model

#model = pickle.load(open('university.pk1', 'rb'))
#load model trrained model
# load your trained model
model = load_mode('model.h5')


@app.rout('/')
def home():
     return render_template('Demo2222.html')

@app.rout('//y_predict', methods=['POST'])
def y_pridict():

#min max scaling
min1=[290., 92.0, 1.0, 1.0, 1.0, 6.8, 0.0]
max1=[340.0, 120.0, 5.0, 5.0, 5.0, 9.92, 1.0]
p = []
for i in range(7):
    l=(k[i]-mini[i])/(max[i]-mini[i])
    p.append(1)
    print(pridiction)
    output=pridiction[0]
    if(output==False):
        return rnder_template('noChance.html', pediction_test=' you  dont have a chance of getting admission ')
    else:
        return render_template('chance.html', prediction_test=' you have a chance of getting admissions' )
if_name_=="_main_":
app.run(debug=Flase)
