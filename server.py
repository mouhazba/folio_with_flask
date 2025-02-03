from flask import Flask
from flask import render_template, url_for, request, redirect
from markupsafe import escape # eviter les injocntions
import pandas as pd
import os





app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def current_page(page_name):
    return render_template(page_name)

def save_in_csv(data):
    # with pathlib
    # file_path = Path('name_file.csv')
    #df_Frame.to_csv('from_contact_form.csv', mode='a', index=False, header=not file_path.exists()'))

    df_Frame = pd.DataFrame([data])  # Convertir en DataFrame avec une seule ligne
    df_Frame.to_csv('from_contact_form.csv', mode='a', index=False, header=not os.path.exists('from_contact_form.csv'))

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            save_in_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'not save in database'
    else:
        return 'Something is wrong'
        
