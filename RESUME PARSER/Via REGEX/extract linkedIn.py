import PyPDF2
import re
# Open The File in the Command
file = open("C://Users//hp\Desktop//RESUME PARSER//Via REGEX//test.pdf", 'rb')
readPDF = PyPDF2.PdfFileReader(file)
def find_url(string):
   #Find all the String that matches with the pattern
   regex = r"(/^(http(s)?:\/\/)?([\w]+\.)?linkedin\.com\/(pub|in|profile)/gm)"
   url = re.findall(regex,string)
   for url in url:
      return url
# Iterating over all the pages of File
for page_no in range(readPDF.numPages):
   page=readPDF.getPage(page_no)
   text = page.extractText()
   print(find_url(text))
file.close()