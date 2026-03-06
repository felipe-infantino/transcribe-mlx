from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import click

from app.inference import DEFAULT_MODEL, transcribe


@click.command()
@click.argument("audio", type=click.Path(exists=True, dir_okay=False))
@click.argument("output", type=click.Path(dir_okay=False))
@click.option(
    "--model",
    "-m",
    default=DEFAULT_MODEL,
    show_default=True,
    help="HuggingFace repo or local path to the Whisper MLX model.",
)
def main(audio: str, output: str, model: str) -> None:
    """Transcribe AUDIO to OUTPUT (JSON) using MLX Whisper."""
    audio_path = Path(audio)
    output_path = Path(output)

    click.echo(f"Model: {model}")
    click.echo("Note: the model will be downloaded from HuggingFace on the first run (~1–3 GB).")
    click.echo(f"Transcribing  {audio_path.name} …")
    t0 = time.perf_counter()

    result = transcribe(str(audio_path), model=model)

    elapsed = time.perf_counter() - t0

    output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2))

    duration: float = result.get("segments", [{}])[-1].get("end", 0) if result.get("segments") else 0
    rtf = elapsed / duration if duration else 0

    click.echo(
        f"Done  {output_path}  "
        f"[{elapsed:.1f}s elapsed"
        + (f", RTF {rtf:.2f}" if duration else "")
        + "]"
    )
