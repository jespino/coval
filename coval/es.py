import string
import re

def cif(cif, strict=True):
    '''Validate Spanish CIF number
    
    In Spain, all Spanish companies are issued with a CIF code.'''
    cif = cif.upper()

    if not strict:
        cif = cif.strip().replace("-", "")
    
    letters = 'ABCDEFGHJKLMNPRQSUVW'
    letters2 = 'ABCDEFGHIJ'
    
    if not re.match("^[%s]\d{7}[\d[%s]$" % (letters, letters2), cif):
        return False
    
    letter = cif[0]
    
    provinceCode = cif[1:3]
    
    number = cif[3:8];
    controlCode = cif[8]
    
    if letter in "CKLMNPQRSW" and controlCode in range(0,10):
        return False
    
    if letter in "ABDEFGHJUV" and controlCode in string.letters:
        return False
    
    a = int(provinceCode[1])+int(number[1])+int(number[3])
    
    b = 0;
    oddNumbers = [int(provinceCode[0]), int(number[0]), int(number[2]), int(number[4])]
    for number in oddNumbers:
        x = number*2
        if x >= 10:
            x = (x % 10) + 1
        b += x
    
    c = a + b
    
    e = c % 10
    
    if e != 0:
        d = 10 - e
    else:
        d = 0
    
    if controlCode != str(d) and letters2[d-1] != controlCode:
        return False
    
    return True

def ccc(ccc, strict=True):
    '''Validate Spanish Account Client Code number
    
    In Spain, all Spanish banking accounts are issued with a CCC code.'''

    if not strict:
        ccc = ccc.strip().replace("-", "").replace(" ", "")

    if not re.match("^\d{20}$", ccc):
        return False
    
    weight = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
    
    entity = ccc[0:4]
    office = ccc[4:8]
    
    controlCode = ccc[8:10]
    account = ccc[10:]
    
    firstCode  = "00"+entity+office
    secondCode = account;
    
    firstCodeResult = 0;
    for x in range(0,10):
        firstCodeResult += int(firstCode[x]) * weight[x]
    
    firstCodeMod = firstCodeResult % 11;
    firstCodeResult = 11 - firstCodeMod;
    
    if firstCodeResult == 10:
        firstCodeResult = 1
    
    if firstCodeResult == 11:
        firstCodeResult = 0
    
    secondCodeResult = 0;
    for x in range(0,10):
        secondCodeResult += int(secondCode[x]) * weight[x]
    
    secondCodeMod    = secondCodeResult % 11
    secondCodeResult = 11 - secondCodeMod
    
    if secondCodeResult == 10:
        secondCodeResult = 1
    
    if secondCodeResult == 11:
        secondCodeResult = 0
    
    if firstCodeResult == int(controlCode[0]) and secondCodeResult == int(controlCode[1]):
        return True
    
    return False


def ssn(ssn, strict=True):
    '''Validate Spanish Social Security number
    
    In Spain, all Spanish have a social security number.'''

    if not strict:
        ssn = ssn.strip().replace("-", "").replace("/", "")

    if not re.match("^\d{12}$", ssn):
        return False
    
    a = ssn[0:2]
    b = ssn[2:10]
    
    code = ssn[10:12]
    
    snn = "%012d" % int(ssn)
    
    if not re.match("^\d{12}$", ssn):
        return False;
    
    if (int(b) < 10000000):
        d = int(b) + (int(a) * 10000000)
    else:
        d = a + b.replace("0*$", "")
    
    c = int(d) % 97
    
    return (c == int(code))


def postcode(postcode, strict=True):
    '''Validate Spanish Postal Code number'''
    if not strict:
        postcode = postcode.strip()

    if not re.match("^\d{5}$", postcode):
        return False
    
    provinceCode = postcode[0:2]
    if (int(provinceCode) > 52) or (int(provinceCode) < 1):
        return False
    
    return True
