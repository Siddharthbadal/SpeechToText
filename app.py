from flask import Flask, render_template, request, redirect
import speech_recognition as sr
from collections import Counter

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    count = ''
    transcript = ''
    commonWord=''
    if request.method == 'POST':

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files['file']
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
            count = len(transcript.split())
            commonWord = commonWords(transcript)
            
            


    return render_template('index.html', transcript=transcript,count=count, commonWord=commonWord)


def commonWords(txt):
    splitTxt = txt.split()
    counter = Counter(splitTxt)
    commonWord = counter.most_common(1)
    return commonWord




if __name__ == "__main__":
    app.run(debug=True, threaded=True)