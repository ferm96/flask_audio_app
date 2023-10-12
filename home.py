from flask import Blueprint, render_template, send_from_directory, current_app, request, jsonify
import librosa
import os
import numpy as np

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/', methods=["GET", "POST"])
def index():
	return render_template('home/song.html')

@bp.route('/music/<path:filename>', methods=['GET'])
def download(filename):
    path = current_app.config['UPLOAD_FOLDER']
    return send_from_directory(
		path,
        filename,
        as_attachment=True,
        mimetype='audio/mp3'
    )

@bp.route('/align', methods=['POST'])
def align_audio():
    audio_file1_path = os.path.join(current_app.static_folder, 'audio\Kissinetude.wav')
    audio_file2_path = os.path.join(current_app.static_folder, 'audio\Seg.wav')

    if not audio_file1_path or not audio_file2_path:
        return jsonify({'error': 'Invalid audio file paths'})

    # Perform alignment using librosa.dtw with chroma_cens features
    audio1, sr = librosa.load(audio_file1_path)
    audio2, sr = librosa.load(audio_file2_path)
    X = librosa.feature.chroma_cens(y=audio1, sr=sr, hop_length = 512)
    Y = librosa.feature.chroma_cens(y=audio2, sr=sr, hop_length = 512)
    D, wp = librosa.sequence.dtw(X, Y, subseq=True)


    hop_length = 512
    wp = np.flip(wp)
    start = wp[0][1] * hop_length / sr
    end = wp[-1][1] * hop_length / sr
    
    # Convert the alignment path to a list
    alignment_path = wp.tolist() 

    # Return the alignment path as JSON
    return jsonify({'start_time': start, 'end_time': end})
