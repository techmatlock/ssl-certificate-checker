from flask import Flask, render_template, send_file
import json

app = Flask(__name__)

@app.route('/download')
def download_csv():
    filename = "output.csv"
    return send_file(filename, as_attachment=True)
    
@app.route('/')
def display_data():
    """Loads both json files that were generated from preprocess_data.py"""
    with open('domain_list.json', 'r') as json_file:
        results = json.load(json_file)
    with open('exception_list.json', 'r') as json_file2:
        exceptions = json.load(json_file2)
    return render_template("index.html", results=results, exceptions=exceptions)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, threaded=True)