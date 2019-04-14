# This CODE made for stealing FLAGS{32} from EXAMPLE@mailforspam.com and cutting "FLAG{}" part. Vlad made it #
# MA - Main Array; c - counter
# Librarys import
import requests
import re

# Zeroing
c=1
MA=[]

# Getting pages and finding a FLAG{32} / c(%d) is counter [12-13, 24-26 lines] / Making main array MA [17 line]
while c<10:
    get1 = requests.get('https://www.mfsa.info/mail/EXAMPLE/%d' % c)
    data = get1.text
    text = re.findall('FLAG{ ' + '[a-zA-Z0-9]{32}' + ' }', data)
    print(text)
    MA = MA + text
    c = c + 1

print('- '*10 + 'CLAER DATA' + ' -'*10)
c=0

# Filtering array, getting part inside FLAG{__}
while c<9:
    if MA[c] != '':
        print(MA[c][7:39])
    c = c +1

print('- '*12 + 'END' + ' -'*11)
