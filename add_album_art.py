#!/usr/bin/env python3
# Adds album art (cover.jpg) to mp3s and flacs, using ffmpeg
import os, shutil, subprocess, sys, tempfile

path = sys.argv[1]

def main():
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and os.path.splitext(f)[1].lower() in ['.mp3', '.flac']]

    cover_path = os.path.abspath(os.path.join(path, 'cover.jpg'))
    if not os.path.isfile(cover_path):
        print('cover.jpg not found in {}!  Exiting.'.format(path))
        sys.exit(1)

    for audio_filename in files:
        add_art(audio_filename, cover_path)

def add_art(audio_filename, cover_path):
    audio_path = os.path.abspath(os.path.join(path, audio_filename))
    print('Adding cover.jpg to {}'.format(audio_path))

    with tempfile.TemporaryDirectory() as temp_directory:
        command = [
            'ffmpeg',
            '-i', audio_path,
            '-i', cover_path,
            '-c', 'copy',
            '-map', '0:0',
            '-map', '1:0',
            '-id3v2_version', '3',
            '-metadata:s:v', 'title="Album cover"',
            '-metadata:s:v', 'comment="Cover (front)"',
            '-v', "error",
            '{}/{}'.format(temp_directory, audio_filename)
        ]
        subprocess.call(command)
        shutil.move('{}/{}'.format(temp_directory, audio_filename), audio_path)
        return None

main()
