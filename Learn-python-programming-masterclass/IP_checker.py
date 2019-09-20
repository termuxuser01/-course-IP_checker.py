class LetterException(Exception):
  def __str__(self):
    s = 'there cannot be a letter in an ip address'

class StopatBeggining(Exception):
  def __str__(self):
    s = 'Ip address cannot start with a period'

ip_addr = input("Enter an ip address to validate: \n")

def IPcheck(addr):
  i = 0
  b = 0
  c = 0
  for a in addr:
    i += 1
    if a == '.' and i == 1:
      raise StopatBegging
      break
    elif a.isalpha():
      raise LetterException
      break
    elif len(addr) < 7:
      print('address invalid (not enough digits)')
      break
    elif a == '.':
      b += 1
      c = 0
      if b > 4:
        print("too many sections, must have format:")
        print("")
        print("XXX.XXX.XXX.XXX")
        break
    elif a.isdigit(): 
      c += 1
      if c > 3:
        print('segment too long!')
        break
    else:
      print('{} is a valid ip addres'.format(addr))

try:
  IPcheck(ip_addr)
except LetterException:
  print('IPv4 address cannot contain letters!')
except StopatBeggining:
  print('There is a stop at beggining, check typing and try again!')
else:
  print('{} is a valid ip addres'.format(ip_addr))
