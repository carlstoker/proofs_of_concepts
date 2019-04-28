#!/usr/bin/env python3
"""Grabs frame from a video file"""

import argparse
import json
import os
import random
import subprocess

def extract_single_frame(filename, frame_directory, frame_filename, capture_time):
    """Extract individual frames for processing.

    Arguments:
    filename -- file from which to extract frame
    frame_directory -- directory to store frame
    frame_filename -- filename for frame
    capture_time -- start time for capturing frame
    scale -- scaling to use (default: None)
    """

    command = [
        'ffmpeg',
        '-ss', str(capture_time),
        '-i', filename,
        '-vf', 'format=yuvj444p',
        '-vframes', '1',
        '-y',
        '-loglevel', 'fatal',
        os.path.join(frame_directory, frame_filename)
    ]
    subprocess.call(command)

    return None


def get_metadata(filename, keys):
    """Return metadata for filename

    Arguments:
    filename -- filename to retrieve metadata from
    keys -- keys to look for and save
    """
    command = [
        'ffprobe',
        '-show_entries', 'stream={0}:format={0}'.format(','.join(keys)),
        '-of', 'json',
        '-v', 'error',
        filename
    ]
    j = json.loads(subprocess.check_output(command))

    metadata = {}
    for key in keys:
        for stream in j['streams']:
            if key in stream:
                metadata[key] = stream[key]
                break
        if key not in metadata and key in j['format']:
            metadata[key] = j['format'][key]

    if 'duration' in metadata:
        metadata['duration'] = float(metadata['duration'])

    return metadata


def random_timecode(filename, min=5, max=95):
    """Extract individual frames for processing.

    Arguments:
    filename -- file from which to determine timecode
    min -- minimum timecode (percent) to select (default: 5)
    max -- maximum timecode (percent) to select (default: 95)
    """

    duration = get_metadata(filename, ['duration'])['duration']
    min = int(duration * float(min) / 100)
    max = int(duration * float(max) / 100)

    return random.randrange(min, max)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(
        description='Grab frame from FILE(s)'
    )
    PARSER.add_argument(
        'FILE',
        nargs='+'
    )
    PARSER.add_argument(
        '--output',
        help='output directory (default: %(default)s)',
        default='~/Pictures',
        metavar='FRAME_DIR'
    )
    PARSER.add_argument(
        '--framename',
        help='frame filename (default: %(default)s)',
        default='framegrab.jpg',
        metavar='FRAME_FILENAME'
    )
    PARSER.add_argument(
        '--timecode',
        help='frame timecode (default: %(default)s)',
        default='random',
        metavar='CAPTURE_TIME'
    )

    SETTINGS = PARSER.parse_args().__dict__
    SETTINGS['output'] = os.path.expanduser(SETTINGS['output'])

    for file in SETTINGS['FILE']:
        if SETTINGS['timecode'] == 'random':
            SETTINGS['timecode'] = random_timecode(file)

        extract_single_frame(
            file,
            SETTINGS['output'],
            SETTINGS['framename'],
            SETTINGS['timecode']
        )
