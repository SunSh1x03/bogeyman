"""CLI script that decrypts a file encrypted with ``encrypt.py``."""

from __future__ import annotations

import argparse
from pathlib import Path

from crypto_utils import decrypt_file, ensure_key


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Decrypt a file using a Fernet key.")
    parser.add_argument(
        "file",
        type=Path,
        help="Path to the file that should be decrypted.",
    )
    parser.add_argument(
        "--key",
        type=Path,
        default=Path("bogeyman.key"),
        help="Path to the key file generated during encryption.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    file_path = args.file
    key_path = args.key

    if not file_path.exists():
        raise FileNotFoundError(f"File '{file_path}' does not exist.")

    key = ensure_key(key_path, create=False)
    decrypt_file(file_path, key)


if __name__ == "__main__":
    main()
