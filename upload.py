from flask import Flask, render_template, request
# Flask 모듈 임포트
from werkzeug.utils import secure_filename # 파일이름의 보안 버전 반환

app = Flask(__name__) # Flask 객체를 app에 할당

@app.route('/') # app객체를 이용해 라우팅 경로를 결정
def load_file(): # 해당 라우팅 경로로 요청이 올 때 실행할 함수를 바로 밑에 작성
   return render_template('upload.html')
	
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save("./uploads/" + secure_filename(f.filename)) # uploads 폴더에 사진 저장
      #f.save(secure_filename(f.filename)) // upload.py가 있는 디렉토리에 저장
      return 'file uploaded successfully'

if __name__ == '__main__':
   #app.run(debug = True)
   app.run(host="172.30.1.21", port="8080") # upload.html 파일의 form action도 바꿔줘야 함
