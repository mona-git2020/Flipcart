file1 = open("pythonFile1.txt", "w+")
file1.write("Hello, My Name Is Monalisha Prajapati.\n" "Today is my birthday.\n" "Thank you so much for your warm wishes.")
file1 = open("pythonFile1.txt", "r")
file1_Content = file1.read()
print(file1_Content)
print("\n")
file2 = open("pythonFile2.txt", "w+")
file2.write(file1_Content)
file2 = open("pythonFile2.txt", "r")
file2_Content = file2.read()
print(file2_Content)
if (file1_Content==file2_Content):
	print("\nContent matched")
else:
	print("\nContent not matched")	