from typing import *
import ffmpeg
from .resources import Meeting


def compose_screensharing(meeting: Meeting, width: int, height: int) -> Tuple[ffmpeg.Stream, ffmpeg.Stream]:
    """Overlay the deskshare and the webcam."""

    webcams = meeting.webcams.stream_all().filter("scale", width, height)
    deskshare = meeting.deskshare.stream_all().filter("scale", width, height)

    return webcams.overlay(deskshare)


def compose_lesson(meeting: Meeting, width: int, height: int) -> Tuple[ffmpeg.Stream, ffmpeg.Stream]:
    """Keep slides, deskshare video and webcam audio, while discarding the rest."""

    stream = compose_screensharing(meeting, width, height)

    for shape in meeting.shapes:
        for enable in shape.enables:
            scaled_stream = shape.resource.stream_all().filter("scale", width, height)
            stream = stream.overlay(scaled_stream, enable=f"between(t, {enable[0]}, {enable[1]})")

    return stream
