# Flask Audio App

## Description

The Flask Audio App is an application that enables users 
to compare two audio recordings simultaneously, meant for musicians looking to assess 
their practice sessions against a target. The app offer audio matching functionality 
to locate a practice segment within a reference recording and 
provides a visualization of the matched region.

![demo](demo.PNG)

## Installation

To set up the Flask Audio App:

1. Clone the repository: `git clone https://github.com/ferm96/flaskaudioapp.git`
2. Create a virtual environment: `python -m venv venv` and activate it.
3. Install dependencies: `pip install -r requirements.txt`
4. Start the app: `flask run`
5. Access the app at `http://127.0.0.1:5000`

## Usage

1. Playback Controls: Play, pause, stop, and switch between audio recordings. Both are running when pressing play, the switch buttom toggles mute.
2. Matching Functionality: Click "Match" to identify matching regions between the recordings.
3. Zoom and Loop: Zoom in, loop selected region, and manually adjust alignments if needed.

## Credits

- Developed by Oliwer Ferm (oliwerferm@gmail.com) and Mikael Kvist.
- Built using Flask, Librosa, and WaveSurfer.js.

## License

This project is not currently licensed.
