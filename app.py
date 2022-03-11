# importing Flask and other modules
import os

from flask import Flask, request, render_template
from Topsis_Shikhar_101917064 import topsis
from werkzeug.utils import secure_filename
import pandas as pd

# Flask constructor
app = Flask(__name__)

ALLOWED_EXTENSIONS = {'csv'}
UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		if 'InputFile' not in request.files:
			return render_template("f1.html",error="No file")
			
		file = request.files['InputFile']

		if file.filename == '':
			return render_template("f1.html",error="No file selected")

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	
		# file_name = request.form.get("InputFile")
		impacts = request.form.get('InputImpact')
		weights = request.form.get('InputWeight')

		loc = UPLOAD_FOLDER+'/'+file.filename
		df = pd.read_csv(loc)
		try:
			output_df = topsis(df, weights, impacts)
			headings = tuple(output_df.columns.values)
			arr = output_df.values.tolist()
			data = tuple(map(tuple, arr))
			return render_template("f1.html", headings=headings, data=data, filename=filename, impacts=impacts, weights=weights, output=True)
		except Exception as e:
			return render_template("f1.html", error=True, message = e)
	return render_template("f1.html", output = False)

if __name__ == '__main__':
    app.run()
