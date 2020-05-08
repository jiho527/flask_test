from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload')
def load_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save("./uploads/" + secure_filename(f.filename))
      #f.save(secure_filename(f.filename)) // upload.py 디렉토리에 저
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)
