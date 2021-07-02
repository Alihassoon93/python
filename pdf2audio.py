import pyttsx3
import PyPDF2

with open("RL2-.pdf", "rb") as book:
	reader = PyPDF2.PdfFileReader(book)

	audio_reader = pyttsx3.init()
	audio_reader.setProperty("rate", 150)
	first_page = reader.getPage(0)
	content = first_page.extractText()


	audio_reader.say(content)
	audio_reader.runAndWait()

	

