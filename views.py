from flask import Blueprint, render_template, request,redirect
from models import Complaint
from init import db


views = Blueprint('views', __name__)

@views.route("/")
def firstapi():
    return render_template("show.html", complaints=Complaint.query.all())

@views.route("/show.html", methods = ['GET', 'POST'])
def about():
    if request.method == 'POST':
        'add entry to DB'
        id = request.form.get('id')
        name = request.form.get('name')
        complaint = request.form.get('complaint')

        entry = Complaint(id=id, name =name, complaint= complaint)
        db.session.add(entry)
        db.session.commit()
    return render_template("show.html", complaints=Complaint.query.all())


@views.route("/remove/<id>", methods=['GET', 'POST'])
def delete(id):
    Complaint.query.filter_by(id=id).delete()
    db.session.commit()
    # flash("Product has been removed successfully", category='success')
    return render_template('show.html', complaints=Complaint.query.all())

@views.route("/update/<id>", methods=['GET', 'POST'])
def update(id):
    if request.method=='POST':
        complaint = request.form.get('complaint')
        comp = Complaint.query.filter_by(id=id).first()
        print(comp.name)
        comp.complaint = complaint
        db.session.add(comp)
        db.session.commit()
        return redirect("/show.html")
    comp = Complaint.query.filter_by(id=id).first()
    return render_template('update.html', complaints=comp)



