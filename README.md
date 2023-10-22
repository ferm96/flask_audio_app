# Flask Audio App

## Description

This application enables users 
to compare two audio recordings, meant for musicians looking to assess 
their practice sessions against a target. The app offer audio matching functionality 
to locate a practice segment within a reference recording and 
provides a visualization of the matched region. The app lets the user playback and loop
over the match, and includes a switching functionality to easily switch back and fourth between the
target match and the practice segment. This is a demo project connected to a master thesis.

<img src="demo.PNG" alt="Demo" width="600" height="400">

## Installation

To set up a virtual enviroment, install dependencies and run the Flask app:

1. Clone the repository: `git clone https://github.com/ferm96/flask_audio_app.git`
2. Change directory to the cloned repository: `cd flask_audio_app`
3. Create a virtual environment and activate it.
Windows example;
create: `python -m venv venv`,
activate: `.\venv\Scripts\activate`.
MacOS;
create: `python3 -m venv venv`,
activate: `source venv/bin/activate`.
4. Install dependencies: `pip install -r requirements.txt`
5. Set the Flask app variable:
On Windows: `set FLASK_APP=__init__.py`
On macOS: `export FLASK_APP=__init__.py`
6. Start the app: `flask run`
7. Access the app at `[http://127.0.0.1:5000](http://localhost:500)`

## Functionalities

1. Playback Controls: Play, pause, stop, and switch between audio recordings. Both are running when pressing play, the switch buttom toggles mute.
2. Matching Functionality: Click "Match" to compute and visualize the matching region between the recordings.
3. Zoom on target recording, loop option (checkbox) on region, and manually adjust matching region if needed.

## Credits

- Developed by [Oliwer Ferm](https://github.com/ferm96/) and [Mikael Kvist](https://github.com/mikaelkvist/).

## License

Copyright 2023 KTH Royal Institute of Technology
