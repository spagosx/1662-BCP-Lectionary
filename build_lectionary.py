import json
import datetime
import pandas as pd
import pdfkit
import PyPDF2
import os
import shutil

def build_lectionary():
    merger = PyPDF2.PdfFileMerger()
    for m in range(12):
        month = m+1
        if not os.path.exists('tmp'):
            os.mkdir('tmp')
        write_to = open(f"tmp/lectionary_{month}.csv", "a")
        string = ",Morning,,Evening\nDay,1st lesson, 2nd lesson, 1st lesson, 2nd lesson\n"
        string += month_lessons(month)
        write_to.write(string)
        write_to.close()
        generatePDF(month)
        merger.append(f'tmp/lectionary_pdf_{month}.pdf')
    merger.write(f"{os.path.expanduser('~')}/Desktop/Lectionary_YEAR.pdf")
    merger.close()
    shutil.rmtree('tmp')


def month_lessons(month):
    string = ""
    filename = f'months/{month}.json'
    with open(filename) as json_file:
        dict = json.load(json_file)
        for index, day in enumerate(dict):
            string += day_lessons(day, index)
    return string
            

def day_lessons(day, index):
    morning = day['morning']
    evening = day['evening']

    return f"{index+1},{morning['first']},{morning['second']},{evening['first']},{evening['second']}\n"
    
def generatePDF(month):
    CSV = pd.read_csv(f'tmp/lectionary_{month}.csv')
    CSV.to_html(f'tmp/lectionary_html_{month}.html')
    pdfkit.from_file(f'tmp/lectionary_html_{month}.html', f'tmp/lectionary_pdf_{month}.pdf')

build_lectionary()