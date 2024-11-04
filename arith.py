def arith_op(_x, _y):
  x = int(_x)
  y = int(_y)
  print(f'{x} + {y} = {x + y}')
  print(f'{x} - {y} = {x - y}')
  print(f'{x} * {y} = {x * y}')
  print(f'{x} / {y} = {x / y}')
  
def error_handler():
  pass
  
  
#error_handler()

def read_input():
  intake = ['','']
  val = input("Enter two integers separated by space\n")
  temp = ''
  x = 0
  ln = 0
  lst = len(val) - 1
  
  while True:
     if ln == len(val):
       break
     
     if val[ln] == ' ':
       intake[x] = temp
       x += 1
       ln += 1
       temp = ''
     else:
       if ln == lst:
         temp += val[lst]
         intake[x] = temp
       temp += val[ln]
       ln += 1
       
  
  arith_op(intake[0], intake[1])
  
read_input()


