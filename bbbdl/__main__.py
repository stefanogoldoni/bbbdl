import ffmpeg
import click
from .resources import Meeting
from .composer import compose_lesson


@click.command()
@click.option("-i", "--input-url", type=str, prompt=True,
              help="The URL of the meeting to download.")
@click.option("-o", "--output-file", type=str, prompt=True,
              help="The file the video should be written to.")
def download(input_url, output_file):
    meeting = Meeting.from_url(input_url)
    streams = compose_lesson(meeting)
    output = ffmpeg.output(*streams, output_file)
    output.run()


if __name__ == "__main__":
    download()
