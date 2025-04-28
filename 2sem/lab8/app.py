from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField, FileField, RadioField, EmailField, \
    SubmitField
from wtforms.validators import DataRequired, Email
from werkzeug.utils import secure_filename
import json, os, smtplib
from email.message import EmailMessage
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')


# Загрузка списка членов экипажа из JSON
def load_members():
    path = os.path.join(app.root_path, 'members', 'members.json')
    with open(path, encoding='utf-8') as f:
        return json.load(f)


members = load_members()


# WTForms форма для /astronaut_selection
class SelectionForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    education = StringField('Образование', validators=[DataRequired()])
    profession = SelectField('Основная профессия', choices=[
        ('engineer_researcher', 'Инженер-исследователь'), ('pilot', 'Пилот'),
        ('builder', 'Строитель'), ('exobiologist', 'Экзобиолог'), ('doctor', 'Врач'),
        ('terraform_engineer', 'Инженер по терраформированию'), ('climatologist', 'Климатолог'),
        ('radiation_specialist', 'Специалист по радиационной защите'), ('astrogeologist', 'Астрогеолог'),
        ('glaciologist', 'Гляциолог'), ('life_support_engineer', 'Инженер жизнеобеспечения'),
        ('meteorologist', 'Метеоролог'), ('rover_operator', 'Оператор марсохода'),
        ('cyber_engineer', 'Киберинженер'), ('navigator', 'Штурман'), ('drone_pilot', 'Пилот дронов')
    ])
    gender = RadioField('Пол', choices=[('male', 'Мужской'), ('female', 'Женский')], validators=[DataRequired()])
    motivation = TextAreaField('Мотивация', validators=[DataRequired()])
    stay = BooleanField('Готовы ли остаться на Марсе?')
    photo = FileField('Фото', validators=[DataRequired()])
    submit = SubmitField('Отправить')


@app.route('/')
@app.route('/index')
def index():
    links = [
        ('Главная', url_for('index')),
        ('Список профессий (ul)', url_for('list_prof', list='ul')),
        ('Размещение', url_for('distribution')),
        ('Член экипажа #1', url_for('member_number', number=1)),
        ('Член экипажа случайно', url_for('member_random')),
        ('Оформление каюты', url_for('room', sex='male', age=20)),
        ('Запись добровольцем', url_for('astronaut_selection')),
        ('Галерея', url_for('galery'))
    ]
    return render_template('index.html', title='Добро пожаловать!', links=links)


@app.route('/list_prof/<list>')
def list_prof(list):
    professions = [
        'Командир', 'Пилот', 'Инженер', 'Медик', 'Биолог', 'Геолог', 'Климатолог',
        'Радиационный специалист', 'Экзобиолог', 'Дизайнер интерьера'
    ]
    if list not in ['ul', 'ol']:
        return f"Неверный параметр '{list}'. Используйте 'ul' или 'ol'."
    return render_template('list_prof.html', title='Список профессий',
                           professions=professions, list_type=list)


@app.route('/distribution')
def distribution():
    return render_template('distribution.html', title='Размещение', crew=members)


@app.route('/member/<int:number>')
def member_number(number):
    if 1 <= number <= len(members):
        member = members[number - 1]
    else:
        return f"Член экипажа под номером {number} не найден."
    return render_template('member.html', title='Член экипажа', member=member)


@app.route('/member/random')
def member_random():
    return render_template('member.html', title='Член экипажа', member=random.choice(members))


@app.route('/room/<sex>/<int:age>')
def room(sex, age):
    return render_template('room.html', title='Оформление каюты', sex=sex, age=age)


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    form = SelectionForm()
    if form.validate_on_submit():
        # Сохранение файла
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        photo.save(path)
        # Отправка письма
        msg = EmailMessage()
        msg['Subject'] = 'Новая заявка волонтёра'
        msg['From'] = 'sender@example.com'
        msg['To'] = form.email.data
        body = f"Фамилия: {form.surname.data}\nИмя: {form.name.data}\n..."
        msg.set_content(body)
        with open(path, 'rb') as f:
            msg.add_attachment(f.read(), maintype='image', subtype='jpeg', filename=filename)
        with smtplib.SMTP('localhost') as server:
            server.send_message(msg)
        flash('Заявка отправлена')
        return redirect(url_for('astronaut_selection'))
    return render_template('astronaut_selection.html', title='Запись добровольцем', form=form)


@app.route('/galery', methods=['GET', 'POST'])
def galery():
    gallery_folder = os.path.join('static', 'gallery')
    os.makedirs(gallery_folder, exist_ok=True)
    if request.method == 'POST':
        img = request.files['photo']
        fn = secure_filename(img.filename)
        img.save(os.path.join(app.root_path, gallery_folder, fn))
    images = os.listdir(os.path.join(app.root_path, gallery_folder))
    return render_template('galery.html', title='Галерея', images=images)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
