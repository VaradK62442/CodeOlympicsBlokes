# open library API
# QR tag API

# given a book's ISBN, create a QR code for 
# a link to that book's page on open library

from pyperclip import copy

ISBN = input("Enter ISBN of book: ")
link = 'https://openlibrary.org/isbn/' + ISBN

QR_code = 'https://qrtag.net/api/qr.png?url=' + link

copy(QR_code)
print("Done! The link to the QR code has been copied to your clipboard.")