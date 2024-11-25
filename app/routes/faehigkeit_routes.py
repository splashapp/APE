from flask import Blueprint, request, redirect, url_for, render_template
from ..models import db, Faehigkeit

faehigkeit_bp = Blueprint('faehigkeit_bp', __name__)

@faehigkeit_bp.route('/create', methods=['GET', 'POST'])
def create_faehigkeit():
    if request.method == 'POST':
        data = request.form
        new_faehigkeit = Faehigkeit(name=data['name'], beschreibung=data.get('beschreibung'))
        db.session.add(new_faehigkeit)
        db.session.commit()
        return redirect(url_for('faehigkeit_bp.get_all_faehigkeiten'))
    return render_template('faehigkeit/create.html')

@faehigkeit_bp.route('/', methods=['GET'])
def get_all_faehigkeiten():
    faehigkeiten = Faehigkeit.query.all()
    return render_template('faehigkeit/read.html', faehigkeiten=faehigkeiten)

@faehigkeit_bp.route('/<int:id>/update', methods=['GET', 'POST'])
def update_faehigkeit(id):
    faehigkeit = Faehigkeit.query.get_or_404(id)
    if request.method == 'POST':
        data = request.form
        faehigkeit.name = data['name']
        faehigkeit.beschreibung = data.get('beschreibung')
        db.session.commit()
        return redirect(url_for('faehigkeit_bp.get_all_faehigkeiten'))
    return render_template('faehigkeit/update.html', faehigkeit=faehigkeit)

@faehigkeit_bp.route('/<int:id>/delete', methods=['POST'])
def delete_faehigkeit(id):
    faehigkeit = Faehigkeit.query.get_or_404(id)
    db.session.delete(faehigkeit)
    db.session.commit()
    return redirect(url_for('faehigkeit_bp.get_all_faehigkeiten'))