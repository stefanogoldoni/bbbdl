# bbbdl

A tool for downloading BigBlueButton meetings

## Requirements

- [`Python 3.8+`](https://www.python.org/)
- [`ffmpeg`](https://ffmpeg.org/download.html)
- [`pipx`](https://pipxproject.github.io/pipx/installation/)

## Installing

Run the following command:
```
pipx install bbbdl
```

## Usage

### Download a single BigBlueButton meeting

```
bbbdl download -i {MEETING_URL} -o {OUTPUT_FILE_NAME}
```

### Download all meetings from a list

```
bbbdl sync -j {LIST_FILE}
```

### Download all meetings from a remote list

```
bbbdl sync -r {LIST_FILE_URL}
```

## Meeting list format

A JSON file containing an object with filename/url pairs:

```json
{
  "a.mp4": "https://example.org/playback/presentation/2.0/playback.html?meetingId=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-1111111111111",
  "b.mp4": "https://example.org/playback/presentation/2.0/playback.html?meetingId=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb-2222222222222"
}
```

### Development

1. Clone the git repository
2. Install the dependencies with poetry:
   ```bash
   poetry install
   ```
