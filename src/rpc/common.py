from pathlib import Path


def get_config_path(file_name: str) -> Path:
    current_dir = Path(__file__).absolute().parent
    return current_dir / "config" / file_name
