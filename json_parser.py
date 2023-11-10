import json
from typing import Generator

from bs4 import BeautifulSoup as Bs

from variables import DATE, FROM, USER, NAME, BODY, CONTENT, DIV


def get_message(file: str) -> Generator:
	"""
	Функция принимает путь до файла, парсит необходимые данные и возвращает
	генератор кортежа из сообщения и имени файла.
	:param file: Путь до файла.
	:return: Генератор кортежа из сообщения и имени файла.
	"""
	with open(file, encoding='utf-8-sig') as f:
		data = json.load(f)
		for i in data:
			try:
				date: str = i[DATE].split('T')[0]
				user: str = i[FROM][USER][NAME].replace('\n', '')
				parsed_text: str = i[BODY][CONTENT]
				soup: Bs = Bs(parsed_text, 'html.parser')
				text: str = soup.get_text(DIV).replace(DIV, '').replace('\n', '')
				message: list = [date, user, text]
				yield message
			except AttributeError:
				pass
			except TypeError:
				pass
