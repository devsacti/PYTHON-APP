from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import sqlite3

import pandas as pd

def index(request):
    res="Hello,i am index function of views.py of ui app of django_prj"

    # db access with sqlite3
    con = sqlite3.connect("db.sqlite3")

    cur=con.cursor()

    cur.execute("select * from ui_t1")

    rows=cur.fetchall()

    for row in rows:
        print(row) # row는 tuple
        res+= ', and after is comes from sqlite3'+' '.join(map(str,row))

    con.close()

    # db access with pandas
    # connect = sqlite3.connect('db.sqlite3')
    # df = pd.read_sql_query('select * from  scraping_naverstock WHERE per <> \'N/A\' ', connect)
    # connect.close()

    return HttpResponse(res)

def templatesAPI1(request):

    return render(request,'product-result.html')