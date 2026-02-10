from collections import namedtuple

Book = namedtuple ('Book', ['name', 'ISBN', 'quantity'])
Book1 = Book( 'Hands on Data Structures', '9781788995573', '50')

print('Using index ISBN: ' + Book1[1])

print('Using key ISBN: ' + Book1.ISBN)
print(Book1.name)