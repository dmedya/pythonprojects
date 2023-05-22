import pyttsx3
import PyPDF4


hikaye= open('kitapokuyucu.pdf','rb')
pdfOkuyucu = PyPDF4.PdfFileReader(hikaye)


engine = pyttsx3.init()
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

for sayfa_numarasi in range (0,pdfOkuyucu.numPages):
    sayfa = pdfOkuyucu.getPage(sayfa_numarasi)
    yazi=sayfa.extractText()
    engine.say(yazi)
    engine.runAndWait()

