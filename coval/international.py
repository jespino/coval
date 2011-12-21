import string
import re

def isbn(isbn, strict=True):
    '''Validation of an ISBN (international Standard Book Number)'''

    if not strict:
        isbn = isbn.upper()
        if isbn[0:4] == 'ISBN':
            isbn = isbn[4:]
        isbn = isbn.strip().replace("-", "").replace("/", "")

    if len(isbn) == 10:
        return isbn10(isbn)
    elif len(isbn) == 13:
        return isbn13(isbn)
    else:
        return False

# Extracted from Wikipedia's http://en.wikipedia.org/wiki/Isbn page
def isbn10(isbn, strict=True):
    '''Validation of an ISBN (international Standard Book Number) in ISBN-10 format'''

    if not strict:
        isbn = isbn.upper()
        if isbn[0:4] == 'ISBN':
            isbn = isbn[4:]
        isbn = isbn.strip().replace("-", "").replace("/", "")

    if not re.match('^\d{10}$', isbn):
        return False

    total = sum([int(num)*weight for num, weight in
                     zip(isbn, reversed(range(1, 11)))])
    return total%11==0

# Extracted from Wikipedia's http://en.wikipedia.org/wiki/Isbn page
def isbn13(isbn, strict=True):
    '''Validation of an ISBN (international Standard Book Number) in ISBN-13 format'''

    if not strict:
        isbn = isbn.upper()
        if isbn[0:4] == 'ISBN':
            isbn = isbn[4:]
        isbn = isbn.strip().replace("-", "").replace("/", "")

    if not re.match('^\d{13}$', isbn):
        return False

    total = sum([int(num)*weight for num, weight in zip(isbn, (1,3)*6)])
    ck = 10-(total%10)
    return ck == int(isbn[-1])

def iban(iban, strict=True):
    '''Validation of an IBAN (international bankaccount number)'''
    country_code_length = {
        'AD': 24, 'AE': 23, 'AL': 28, 'AT': 20, 'BA': 20, 'BE': 16, 'BG': 22,
        'CH': 21, 'CY': 28, 'CZ': 24, 'DE': 22, 'DK': 18, 'EE': 20, 'ES': 24,
        'FR': 27, 'FI': 18, 'GB': 22, 'GE': 22, 'GI': 23, 'GR': 27, 'HR': 21,
        'HU': 28, 'IE': 22, 'IL': 23, 'IS': 26, 'IT': 27, 'KW': 30, 'LB': 28,
        'LI': 21, 'LT': 20, 'LU': 20, 'LV': 21, 'MC': 27, 'ME': 22, 'MK': 19,
        'MR': 27, 'MT': 31, 'MU': 30, 'NL': 18, 'NO': 15, 'PL': 28, 'PT': 25,
        'RO': 24, 'RS': 22, 'SA': 24, 'SE': 24, 'SI': 19, 'SK': 24, 'SM': 27,
        'TN': 24, 'TR': 26,
    }
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if not strict:
        iban = iban.strip().replace("-", "").replace("/", "")

    iban = iban.upper()

    if len(iban)<2 or not iban[0:2] in country_code_length.keys():
        return False

    if len(iban) != country_code_length[iban[0:2]]:
        return False

    iban = iban[4:]+iban[0:4]

    iban_translated = ''
    for char in iban:
        if char in letters:
            iban_translated += str(letters.index(char)+10)
        elif char in '0123456789':
            iban_translated += char
        else:
            return False
    return (int(iban_translated) % 97) == 1
            

def banknote_euro(banknote, strict=True):
    '''Validation of a Euro banknote id'''
    euro_country_codes = 'JKLMNPRSTUVWXYZ'

    if not strict:
        banknote = banknote.strip().replace("-", "").replace("/", "")
    
    if len(banknote) != 12:
        return False

    if not banknote[0] in euro_country_codes:
        return False

    # Convert charater to ascii code
    banknote = int(str(ord(banknote[0]))+banknote[1:])
    return (int(banknote) % 9) == 0
