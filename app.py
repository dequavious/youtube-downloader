import os
from io import BytesIO

from flask import Flask, render_template, request, url_for, redirect, send_file, flash
from flask_api import status
from pytube import YouTube

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        link = request.form.get('url')
        try:
            vid = YouTube(link)
            vid.check_availability()
        except:
            flash("Invalid URL.")
            return redirect(url_for('home'))
        try:
            return render_template('download.html', link=link, vid=vid, video=vid.streams.filter(progressive=True),
                                   audio=vid.streams.filter(mime_type="audio/mp4"), title=vid.title.replace("\"", "'"))
        except:
            flash("An error occurred while fetching streams. Please try again later.")
            return redirect(url_for('home'))
    return render_template('home.html')


@app.route("/download/<int:itag>", methods=["GET"])
def download(itag):
    try:
        if not request.args.get('l'):
            return "No link provided.", status.HTTP_400_BAD_REQUEST
        link = request.args.get('l')
        try:
            vid = YouTube(link)
        except:
            return "Invalid link.", status.HTTP_400_BAD_REQUEST
        buffer = BytesIO()
        stream = vid.streams.get_by_itag(itag)

        if stream is None:
            return "Stream not found.", status.HTTP_400_BAD_REQUEST

        stream.stream_to_buffer(buffer)
        buffer.seek(0)
        if stream.type == "video":
            return send_file(buffer, as_attachment=True, download_name=f'{vid.title}.mp4', mimetype="video/mp4")
        else:
            return send_file(buffer, as_attachment=True, download_name=f'{vid.title}.mp3', mimetype="audio/mp3")
    except:
        return "An error occurred while downloading stream.", status.HTTP_500_INTERNAL_SERVER_ERROR
