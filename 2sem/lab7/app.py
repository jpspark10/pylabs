from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/')
def mission():
    return render_template('mission.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/promotion')
def promotion():
    lines = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]
    return render_template('promotion.html', lines=lines)


@app.route('/image_mars')
def image_mars():
    return render_template('image_mars.html')


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    if request.method == 'POST':
        data = request.form
        return redirect(url_for('results', nickname=data.get('nickname', ''), level=1, rating=0.0))
    professions = [
        'инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
        'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
        'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог',
        'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов'
    ]
    return render_template('astronaut_selection.html', professions=professions)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return render_template('results.html', nickname=nickname, level=level, rating=rating)


@app.route('/photo/<nickname>', methods=['GET', 'POST'])
def photo(nickname):
    photo_url = None
    if request.method == 'POST':
        file = request.files.get('photo')
        if file:
            filename = secure_filename(f"{nickname}_{file.filename}")
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
    files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if f.startswith(nickname + '_')]
    if files:
        latest = sorted(files)[-1]
        photo_url = url_for('static', filename=f"uploads/{latest}")
    return render_template('photo.html', nickname=nickname, photo_url=photo_url)


@app.route('/carousel')
def carousel():
    images = ['mars1.jpg', 'mars2.jpg', 'mars3.jpg']
    return render_template('carousel.html', images=images)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
