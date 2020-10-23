from pptx import Presentation
import win32com.client

def create_new_file(file_name, content):
	file = open(file_name, "w+")
	file.write(content)
	file = open(file_name, "r")
	file_Content = file.read()
	return file_Content
	
def open_and_read_file(file_name):
	PptApp = win32com.client.Dispatch("Powerpoint.Application")
    PptApp.Visible = True
    PPtPresentation = PptApp.Presentations.Open(file_name, "r")
    PPtPresentation.SaveAs(file_name+"x", 24)
    PPtPresentation.close()
    PptApp.Quit()
	print("hey")
	file = open(file_name, "r")
	print("hey.....Hi...")
	prs = Presentation(file)
	print("hey.....Hi...I m Good....")
	fileDataList = []
	print(fileDataList)
	for slide in prs.slides:
		print("First For Loop")
		for shape in slide.shapes:
			print("First For Loop")
			print(shape.text)
			fileDataList.append(shape.text)
	return fileDataList			