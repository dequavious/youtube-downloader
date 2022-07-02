from io import BytesIO

from dotenv import dotenv_values
from flask import Flask, render_template, request, url_for, redirect, send_file, session, flash
from flask_api import status
from pytube import YouTube

config = dotenv_values(".env")

app = Flask(__name__)
app.config['SECRET_KEY'] = config.get('SECRET_KEY')


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        session['link'] = request.form.get('url')
        try:
            vid = YouTube(session['link'])
            vid.check_availability()
        except:
            flash("Invalid URL.")
            return redirect(url_for('home'))
        return redirect(url_for('downloads'))
    return render_template('home.html')


@app.route("/downloads", methods=["GET"])
def downloads():
    try:
        vid = YouTube(session['link'])
        return render_template('download.html', vid=vid, video=vid.streams.filter(progressive=True),
                               audio=vid.streams.filter(mime_type="audio/mp4"), title=vid.title.replace("\"", "'"))
    except:
        flash("An error occurred while fetching streams. Please try again later.")
        return redirect(url_for('home'))


@app.route("/download/<int:itag>", methods=["GET"])
def download(itag):
    try:
        vid = YouTube(session['link'])
        if request.method == "GET":
            buffer = BytesIO()
            stream = vid.streams.get_by_itag(itag)
            stream.stream_to_buffer(buffer)
            buffer.seek(0)
            if stream.type == "video":
                return send_file(buffer, as_attachment=True, download_name=f'{vid.title}.mp4', mimetype="video/mp4")
            else:
                return send_file(buffer, as_attachment=True, download_name=f'{vid.title}.mp3', mimetype="audio/mp3")
    except:
        return "An error occurred while downloading stream.", status.HTTP_500_INTERNAL_SERVER_ERROR
