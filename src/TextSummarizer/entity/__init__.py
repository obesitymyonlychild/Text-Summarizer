from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_dir: Path
    unzip_dir: Path

@dataclass(frozen=True) #unchanged instances
class DataValidationConfig:
    root_dir: Path
    status_file: str
    all_required_files: list