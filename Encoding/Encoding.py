import sys

print(sys.stout.encoding)
print u"Stöcker".encode(sys.stdout.encoding, errors='replace')
print u"Стоескер".encode(sys.stdout.encoding, errors='replace') 