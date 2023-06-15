from flask import render_template, request, redirect
from app import app, db
from app.models import Movie

confirmar = "confirmado"

@app.route('/')

@app.route('/index')
def index():
    # movies = [
    #     {
    #         'id':1,
    #         'name':'Tarzan',
    #         'year':'1999',
    #         'gender':'animada'
    #     },
    #     {
    #         'id':2,
    #         'name':'Bolt',
    #         'year':'2008',
    #         'gender':'animada'
    #     }
    # ]
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        name= form.get('name')
        year= form.get('year')
        gender= form.get('gender')
        if name and year and gender:
            movie = Movie(name=name,year=year,gender=gender)
            db.session.add(movie)
            db.session.commit()
        return redirect('/')

    return "confirmado"

@app.route('/update/<int:id>')
def updateRoute(id):
    if not id or id != 0:
        movie = Movie.query.get(id)
        if movie:
            return render_template('update.html', movie=movie)

    return "confirmado"

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if not id or id != 0:
        movie = Movie.query.get(id)
        if movie:
            form = request.form
            name = form.get('name')
            year = form.get('year')
            gender = form.get('gender')
            movie.name = name
            movie.year = year
            movie.gender = gender
            db.session.commit()
        return redirect('/')

    return "confirmado"

@app.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        movie = Movie.query.get(id)
        if movie:
            db.session.delete(movie)
            db.session.commit()
        return redirect('/')

    return "confirmado"

@app.route('/turn/<int:id>')
def turn(id):
    if not id or id != 0:
        movie = Movie.query.get(id)
        if movie:
            # Perform the desired action with the movie status
            db.session.commit()
        return redirect('/')

    return "confirmado"