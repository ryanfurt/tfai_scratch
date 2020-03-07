from django.shortcuts import render
import sqlalchemy, sqlalchemy.orm
from myapp.models import Base, Language

engine = sqlalchemy.create_engine('sqlite:///demo.sqlite')
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

def is_empty():
    return len(session.query(Language).all()) <= 0

def populate():
    new_langs = [Language('Python','py'),Language('Ruby', 'rb'),
                 Language('Common Lisp', 'lisp'),Language('Objective-C', 'm')]
    session.add_all(new_langs)
    session.commit()

def index(request):
    if is_empty():
        populate()
    langs = session.query(Language).all()
    return render(request,'index.html',{'langs':langs})