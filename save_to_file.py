import csv
from typing import Generator

from variables import COLUMN_NAMES


def save_message_to_file(message: Generator, filename: str) -> None:
	"""
	Функция принимает сообщение, имя файла и записывает данные в файл csv.
	:param message: Текст сообщения.
	:param filename: Путь до файла.
	:return: None
	"""
	with open(filename, 'w', errors='ignore', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(COLUMN_NAMES)
		for value in message:
			writer.writerow(value)
