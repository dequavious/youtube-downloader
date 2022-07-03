from io import BytesIO

from flask import Flask, render_template, request, url_for, redirect, send_file, flash, session
from flask_api import status
from pytube import YouTube

app = Flask(__name__)
app.config['SECRET_KEY'] = "b7da1ed008f16f3b2a92e0f4f86770e91cf687271b5cc2df"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        link = request.form.get('url')
        try:
            vid = YouTube(link)
            vid.check_availability()
            session['link'] = link
        except:
            flash("Invalid URL.")
            return redirect(url_for('home'))
        return redirect(url_for('downloads'))
    return render_template('home.html')


@app.route("/downloads", methods=["GET"])
def downloads():
    try:
        if not session.get('link'):
            return redirect(url_for('home'))

        try:
            vid = YouTube(session['link'])
        except:
            flash("Invalid URL.")
            return redirect(url_for('home'))

        return render_template('download.html', vid=vid, video=vid.streams.filter(progressive=True),
                               audio=vid.streams.filter(mime_type="audio/mp4"), title=vid.title.replace("\"", "'"))
    except:
        flash("An error occurred while fetching streams. Please try again later.")
        return redirect(url_for('home'))


@app.route("/download/<int:itag>", methods=["GET"])
def download(itag):
    try:
        if not session.get('link'):
            return "No session link.", status.HTTP_400_BAD_REQUEST

        try:
            vid = YouTube(session['link'])
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
