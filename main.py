from glob import glob
from os.path import isfile

from save_to_file import save_message_to_file
from json_parser import get_message
from variables import FILES, TO_SAVE


if __name__ == '__main__':
	directory: str = FILES
	to_save: str = TO_SAVE

	for file in glob(directory + '/*'):
		if isfile(file):
			generator_data = get_message(file)
			filename = file.replace(directory, to_save).replace('json', 'csv')
			save_message_to_file(generator_data, filename)
