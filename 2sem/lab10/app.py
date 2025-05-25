import os
import json
import random
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from wtforms import StringField, SelectField, TextAreaField, BooleanField, FileField, RadioField, EmailField, \
    SubmitField
from wtforms.fields import IntegerField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from sqlalchemy import create_engine, select, or_
from sqlalchemy.orm import sessionmaker

from models import Base, User, Job, Department

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')


def load_members():
    path = os.path.join(app.root_path, 'members', 'members.json')
    with open(path, encoding='utf-8') as f:
        return json.load(f)


members = load_members()

engine = create_engine('sqlite:///mars_explorer.db', echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db_session = Session()

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return db_session.get(User, int(user_id))


# Forms
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


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
    ], validators=[DataRequired()])
    gender = RadioField('Пол', choices=[('male', 'Мужской'), ('female', 'Женский')], validators=[DataRequired()])
    motivation = TextAreaField('Мотивация', validators=[DataRequired()])
    stay = BooleanField('Готовы ли остаться на Марсе?')
    photo = FileField('Фото', validators=[DataRequired()])
    submit = SubmitField('Отправить')


class RegisterForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    position = StringField('Должность', validators=[DataRequired()])
    speciality = StringField('Профессия', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')


class JobForm(FlaskForm):
    team_leader = SelectField('Team Leader', coerce=int, validators=[DataRequired()])
    job = StringField('Описание работы', validators=[DataRequired()])
    work_size = IntegerField('Объём работ (часы)', validators=[DataRequired()])
    collaborators = StringField('Участники (IDs через запятую)')
    is_finished = BooleanField('Завершена?')
    submit = SubmitField('Сохранить')


class DepartmentForm(FlaskForm):
    title = StringField('Название департамента', validators=[DataRequired()])
    chief = SelectField('Руководитель (ID)', coerce=int, validators=[DataRequired()])
    members = StringField('Участники (IDs через запятую)')
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Сохранить')


# Routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db_session.execute(select(User).filter_by(email=form.email.data)).scalar_one_or_none()
        if user and check_password_hash(user.hashed_password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        flash('Неверные учетные данные', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data,
            hashed_password=generate_password_hash(form.password.data)
        )
        db_session.add(user)
        db_session.commit()
        flash('Регистрация успешна', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/')
@login_required
def index():
    jobs = db_session.execute(select(Job)).scalars().all()
    return render_template('index.html', jobs=jobs)


@app.route('/job/add', methods=['GET', 'POST'])
@login_required
def add_job():
    form = JobForm()
    users = db_session.execute(select(User)).scalars().all()
    form.team_leader.choices = [(u.id, f"{u.surname} {u.name}") for u in users]
    if form.validate_on_submit():
        job = Job(
            team_leader=form.team_leader.data,
            job=form.job.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data
        )
        db_session.add(job)
        db_session.commit()
        flash('Работа добавлена', 'success')
        return redirect(url_for('index'))
    return render_template('add_job.html', form=form)


@app.route('/job/<int:job_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_job(job_id):
    job = db_session.get(Job, job_id)
    if not job or (job.team_leader != current_user.id and current_user.id != 1):
        abort(403)
    form = JobForm(obj=job)
    users = db_session.execute(select(User)).scalars().all()
    form.team_leader.choices = [(u.id, f"{u.surname} {u.name}") for u in users]
    if form.validate_on_submit():
        form.populate_obj(job)
        db_session.commit()
        flash('Работа обновлена', 'success')
        return redirect(url_for('index'))
    return render_template('add_job.html', form=form)


@app.route('/job/<int:job_id>/delete')
@login_required
def delete_job(job_id):
    job = db_session.get(Job, job_id)
    if not job or (job.team_leader != current_user.id and current_user.id != 1):
        abort(403)
    db_session.delete(job)
    db_session.commit()
    flash('Работа удалена', 'success')
    return redirect(url_for('index'))


@app.route('/departments')
@login_required
def list_departments():
    depts = db_session.execute(select(Department)).scalars().all()
    return render_template('departments.html', depts=depts)


@app.route('/department/add', methods=['GET', 'POST'])
@login_required
def add_department():
    form = DepartmentForm()
    users = db_session.execute(select(User)).scalars().all()
    form.chief.choices = [(u.id, f"{u.surname} {u.name}") for u in users]
    if form.validate_on_submit():
        dept = Department(
            title=form.title.data,
            chief=form.chief.data,
            members=form.members.data,
            email=form.email.data
        )
        db_session.add(dept)
        db_session.commit()
        flash('Департамент добавлен', 'success')
        return redirect(url_for('list_departments'))
    return render_template('add_department.html', form=form)


@app.route('/department/<int:dept_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_department(dept_id):
    dept = db_session.get(Department, dept_id)
    if not dept:
        abort(404)
    form = DepartmentForm(obj=dept)
    users = db_session.execute(select(User)).scalars().all()
    form.chief.choices = [(u.id, f"{u.surname} {u.name}") for u in users]
    if form.validate_on_submit():
        form.populate_obj(dept)
        db_session.commit()
        flash('Департамент обновлен', 'success')
        return redirect(url_for('list_departments'))
    return render_template('add_department.html', form=form)


@app.route('/department/<int:dept_id>/delete')
@login_required
def delete_department(dept_id):
    dept = db_session.get(Department, dept_id)
    if not dept:
        abort(404)
    db_session.delete(dept)
    db_session.commit()
    flash('Департамент удален', 'success')
    return redirect(url_for('list_departments'))


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    form = SelectionForm()
    if form.validate_on_submit():
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        photo.save(path)
        msg = EmailMessage()
        msg['Subject'] = 'Новая заявка волонтёра'
        msg['From'] = 'sender@example.com'
        msg['To'] = form.email.data
        body = (
            f"Фамилия: {form.surname.data}\n"
            f"Имя: {form.name.data}\n"
            f"Образование: {form.education.data}\n"
            f"Профессия: {form.profession.data}\n"
            f"Пол: {form.gender.data}\n"
            f"Мотивация: {form.motivation.data}\n"
            f"Готовы остаться на Марсе: {form.stay.data}"
        )
        msg.set_content(body)
        with open(path, 'rb') as f:
            msg.add_attachment(f.read(), maintype='image', subtype='jpeg', filename=filename)
        with smtplib.SMTP('localhost') as server:
            server.send_message(msg)
        flash('Заявка отправлена', 'success')
        return redirect(url_for('index'))
    return render_template('astronaut_selection.html', title='Запись добровольцем', form=form)


@app.route('/galery', methods=['GET', 'POST'])
@login_required
def galery():
    gallery_folder = os.path.join(app.root_path, 'static', 'gallery')
    os.makedirs(gallery_folder, exist_ok=True)
    if request.method == 'POST':
        img = request.files.get('photo')
        if img:
            fn = secure_filename(img.filename)
            img.save(os.path.join(gallery_folder, fn))
            flash('Изображение загружено', 'success')
    images = sorted(os.listdir(gallery_folder))
    return render_template('galery.html', title='Галерея', images=images)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
