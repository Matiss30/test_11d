
c=int(input("Ievadi kvadrāta malu: "))
def laukums (x):
  global a
  a=x*x
  return a

def maina(d):
  e=d+5
  w=e*e
  return w

print("Pirmais laukums ir ",laukums(c))
print("Otrais laukums ir ",maina(c))

