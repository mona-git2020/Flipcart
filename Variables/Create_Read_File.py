def create_new_file(file_name, content):
	file = open(file_name, "w+")
	file.write(content)
	file = open(file_name, "r")
	file_Content = file.read()
	return file_Content