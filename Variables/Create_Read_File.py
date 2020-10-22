from pptx import Presentation

def create_new_file(file_name, content):
	file = open(file_name, "w+")
	file.write(content)
	file = open(file_name, "r")
	file_Content = file.read()
	return file_Content
	
def open_and_read_file(file_name):
	print("hey")
	file = open(file_name, "r")
	print("hey.....Hi...")
	prs = Presentation(file_name)
	print("hey.....Hi...I m Good....")
	fileDataList = []
	print(fileDataList)
	for slide in prs.slides:
		print("First For Loop")
		for shape in slide.shapes:
			print("First For Loop")
			print(shape.text)
			fileDataList.append(shape.text)
				
	