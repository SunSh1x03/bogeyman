"""Utility helpers for file encryption and decryption."""

from __future__ import annotations

from pathlib import Path

from cryptography.fernet import Fernet


def ensure_key(key_path: Path, *, create: bool = True) -> bytes:
    """Return the symmetric key stored in ``key_path``.

    When ``create`` is ``True`` and ``key_path`` does not yet exist a new key
    is generated and written to the location before being returned.
    """

    if key_path.exists():
        return key_path.read_bytes().strip()

    if not create:
        raise FileNotFoundError(
            f"Encryption key not found at '{key_path}'. Generate it with encrypt.py first."
        )

    key = Fernet.generate_key()
    key_path.write_bytes(key)
    return key


def encrypt_file(file_path: Path, key: bytes) -> Path:
    """Encrypt ``file_path`` using ``key`` and return the path."""

    data = file_path.read_bytes()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(data)
    file_path.write_bytes(encrypted)
    return file_path


def decrypt_file(file_path: Path, key: bytes) -> Path:
    """Decrypt ``file_path`` using ``key`` and return the path."""

    cipher = Fernet(key)
    decrypted = cipher.decrypt(file_path.read_bytes())
    file_path.write_bytes(decrypted)
    return file_path
