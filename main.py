import pyttsx3
import PyPDF2

book = open('testpdf.pdf','rb')
#Change the testbook.pdf with your own book make sure it is in the same directory as main.

pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
speaker = pyttsx3.init()

#You can initialize the starting and ending page by changing 7 and pages respectively.

for num in range(10,pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()