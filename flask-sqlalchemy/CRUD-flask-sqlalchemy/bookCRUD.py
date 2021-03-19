import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy


project_dir = os.path.dirname(os.path.abspath(__file__))        #To get current path of project folder
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db")) 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Book(db.Model):
    book_Id=db.Column(db.String(23), unique=True, nullable=False, primary_key=True)
    title = db.Column(db.String(80),nullable=False)

#return title as string
    def __repr__(self):
        return "<Id: {}>".format(self.book_Id),"<Title: {}>".format(self.title)


@app.route("/", methods=["GET", "POST"])
def home():
    books = None
    if request.form:
        try:
            book = Book(book_Id=request.form.get("book_Id") ,title=request.form.get("title"))
            db.session.add(book)
            db.session.commit()
        except Exception as e:
            print("Failed to add book")
            print(e)
    books = Book.query.all()
    return render_template("home.html", books=books)


@app.route("/update", methods=["POST"])
def update():
    try:
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        book = Book.query.filter_by(title=oldtitle).first()
        book.title = newtitle
        db.session.commit()
    except Exception as e:
        print("Couldn't update book title")
        print(e)
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    id=request.form.get("book_Id")
    title = request.form.get("title")
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', port=8087)
