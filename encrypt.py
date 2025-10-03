"""CLI script that encrypts a file in-place using ``cryptography.Fernet``."""

from __future__ import annotations

import argparse
from pathlib import Path

from crypto_utils import ensure_key, encrypt_file


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Encrypt a file using a Fernet key.")
    parser.add_argument(
        "file",
        type=Path,
        help="Path to the file that should be encrypted.",
    )
    parser.add_argument(
        "--key",
        type=Path,
        default=Path("bogeyman.key"),
        help="Path to the key file. The key is created automatically if it does not exist.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    file_path = args.file
    key_path = args.key

    if not file_path.exists():
        raise FileNotFoundError(f"File '{file_path}' does not exist.")

    key = ensure_key(key_path)
    encrypt_file(file_path, key)


if __name__ == "__main__":
    main()
