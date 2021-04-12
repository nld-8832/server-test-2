from flask import Flask, request, send_from_directory, send_file, url_for
import DP_TRANS as KHOI_SUPER_TRANS

#BASE
model_file_path = 'model/deepspeech-0.9.3-models.tflite'
lm_file_path = 'model/deepspeech-0.9.3-models.scorer'

beam_width = 500
lm_alpha = 0.93
lm_beta = 1.18

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload/<path:filename>', methods= ['GET', 'POST'])
def upload_file(filename):
    if request.method == 'POST':
        f = request.files['files']
        #Store wav file
        filepath = 'Upload_File/{}.wav'.format(filename)
        f.save(filepath)
        #Transcribe and store transcript
        transcript = KHOI_SUPER_TRANS.KHOI_TRANSCRIBE(filepath, model_file_path, lm_file_path, lm_alpha, lm_beta, beam_width)
        trans_filepath = 'Transcribe_File/{}.txt'.format(filename)
        with open(trans_filepath, "a") as text_file:
            text_file.write(transcript)
        return '200'
    else:
        return 'Upload ONLY'

@app.route('/download/<path:filename>')
def get_file(filename):
    trans_filepath = '/Transcribe_File/{}.txt'.format(filename)
    return send_file(trans_filepath)

with app.test_request_context(): 
    print(url_for('upload_file', filename = 'samplefilename'))
    print(url_for('get_file', filename = 'samplefilename'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
