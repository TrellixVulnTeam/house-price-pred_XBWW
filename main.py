from flask import Flask, render_template,redirect,flash, url_for
from form import Prediction
from joblib import load

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b92d7375507461de5267396ceb708ec0'
@app.route('/', methods=['GET','POST'])
def home():
    form = Prediction()
    if form.validate_on_submit():
        data = [form.bedrooms.data,form.bathrooms.data,form.condition.data,form.floors.data,form.sqft_above.data,form.sqft_living.data,
        form.sqft_lot.data,form.sqft_lot15.data,form.yr_built.data,form.zipcode.data]

        model = load('model.joblib')
        result= model.predict([data])
        result = str(result).strip('[]')
        flash('The price is $' + result)
        return redirect(url_for('home'))
    return render_template('home.html',myform=form)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True) 