# transcribe-mlx

Local audio transcription to JSON using MLX Whisper. Runs on Apple Silicon.

## Install

```bash
pip install transcribe-mlx
```

## Usage

```bash
transcribe-mlx "audio.mp3" "output.json"
transcribe-mlx "audio.mp3" "output.json" --model mlx-community/whisper-large-v3-mlx
```

Output is saved as a JSON file with segments, words, and timestamps.

> **First run:** the model (~1–3 GB) is downloaded automatically from HuggingFace and cached locally. Subsequent runs use the cache.

## Arguments

| Argument | Description |
|---|---|
| `audio` | Path to the input audio file |
| `output` | Path where the output JSON will be saved |

## Options

| Flag | Default | Description |
|---|---|---|
| `--model` / `-m` | `mlx-community/whisper-large-v3-turbo` | HuggingFace repo or local path to the Whisper MLX model |

## Requirements

- Python 3.11+
- Apple Silicon (MLX requires Metal)
- FFmpeg (`brew install ffmpeg`)

## Development

```bash
git clone https://github.com/felipeinfantino/transcribe-mlx
cd transcribe-mlx
poetry install
poetry run transcribe-mlx "inputs/audio.mp3" "outputs/result.json"
```

### Extending with a new package

```bash
poetry add [packagename]

# Check the CLI is still working
poetry run transcribe-mlx "inputs/audio.mp3" "outputs/result.json"

# Verify lockfile is clean
poetry lock

# Bump version
poetry version patch   # or minor / major
```

## License

MIT
