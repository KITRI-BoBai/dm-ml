from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser, PDFSyntaxError
import requests
import pandas as pd
import csv

def read_pdf_PDFMINER(pdf_file_path):
    output_string = StringIO()
    with open(pdf_file_path, 'rb') as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    return str(output_string.getvalue())

coinList = open('./onlyWhitePaper.csv', 'r', encoding='utf-8')

coins = csv.reader(coinList)

for coin in coins:
    flag=0
    url = coin[2]
    url = url[2:]
    url = url[:-2]
    
    if '.pdf' in coin[2]:
        try :
            myfile = requests.get(url)
            open('./whitepaper.pdf', 'wb').write(myfile.content)
            path = './whitepaper.pdf'
            result = read_pdf_PDFMINER(path)
        except PDFSyntaxError:
            flag = 1
            print(coin[1])
        except requests.exceptions.SSLError:
            flag = 1
            print(coin[1])
        except requests.exceptions.ConnectionError:
            flag = 1
            print(coin[1])
        except UnicodeDecodeError:
            flag = 1
            print(coin[1])
        except ValueError:
            flag = 1
            print(coin[1])
        except requests.exceptions.ChunkedEncodingError:
            flag = 1
            print(coin[1])


    if '.pdf' in coin[2] and flag == 0:
        f = open("./data/"+coin[1]+".txt", 'w', -1, "utf-8")
        f.write(result)
        f.close()
        print(coin[1])
