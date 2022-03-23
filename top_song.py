from abc import ABC, abstractmethod
from pathlib import Path

import logger


class TopSong(ABC):
    def __init__(self, n: int,
                 data_path: Path,
                 output_path: Path,
                 input_file):
        self.n = n
        self.data_path = data_path
        self.output_path = output_path
        self.input_file = input_file
        self.count_storage = {}
        self.result = []

    @abstractmethod
    def count_frequency(self, file):
        pass

    @abstractmethod
    def filter(self):
        pass

    @abstractmethod
    def get_output_file_prefix(self):
        pass

    def get_filename(self) -> str:
        log_file_date = self.input_file[7:17]
        return f"{self.get_output_file_prefix()}{log_file_date}.txt"

    def discover(self):
        try:
            with open(self.data_path / 'input' / self.input_file) as f:
                self.count_frequency(f)
                self.filter()
                self.save()
        except FileNotFoundError as e:
            logger.error(e)

    def save(self) -> None:
        with open(self.output_path / self.get_filename(), "w") as result_file:
            result_file.writelines(self.result)
