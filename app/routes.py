from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from models import Ingredient

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
        
    return render_template('login.html', title='Sign In', form=form)    
    

@app.route('/create_ingredient', methods=['POST'])
def create_ingredient():
    request_data = json.loads(request.data)
    name = request_data['name']
    description = request_data['description']
    origin = request_data['origin']

    new_ingredient = Ingredient(
        name = name,
        description = description,
        origin = origin  
    )
    

    db.session.add(new_ingredient)
    db.session.commit()

    response = app.response_class(
        response=json.dumps({'result_info': "Запись ингредиента создана"}),
        mimetype='application/json'
    )
    return response


@app.route('/ingredient')
def ingredient_id():
    return Ingredient.query.get(ingredient_id)

