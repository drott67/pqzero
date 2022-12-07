from termcolor import cprint, colored

def factors(x):
  #Gets all factors of a given number
  captured = []
  for i in range(1, x + 1):
    if x % i == 0:
      captured.append(i)
      captured.append((i*-1))
  return captured

def arrays(masterP,masterQ):
  #Returns arrays of all factors of p,q
  return factors(masterP), factors(masterQ)

def divide(p,q):
  #Finds all p/q numbers
  pq = set()
  for i in p:
    for j in q:
      pq.add(i/j)
  return pq

def mathematize(eq,x):
  #Takes equation and a number, checks if it is a solution for the equation
  elist = eq.split()
  total = 0
  
  for bit in elist:
    sign = bit[0]
    num = ''
    index = 1
    for char in bit[1:]:
      try:
        test = float(char)
        num += char
        index += 1
      except:
        break
        
    try:
      signedX = x**int(bit[index+1])
      if sign == "+": total += float(num)*signedX
      elif sign == "-": total -= float(num)*signedX
    except:
      if sign == "+": total += float(num)
      elif sign == "-": total -= float(num)
      
  total = round(total,5)
  
  if total == 0:
    return True, total
  return False, total

def instructions():
  cprint("+==============================================+",end="\n|                                              |\n", color='red')
  print("| P's and Q's                                  |")
  print("|                                              |")
  print("| P is the last Int in the equation.           |")
  print("| Q is the first Int in the equation.          |",end="\n|                                              |\n")
  print("| Enter polynomials as:                        |")
  print("|   Sign, Integer, Variable, Power             |")
  print("|                                              |")
  print("| Example:                                     |")
  print("|   -1x4                                       |")
  print("|   *All parts must include +/-                |")
  print("|   *Parts with an Int of 1 must include it    |", end = "\n|                                              |\n")
  print("| Sample:                                      |")
  print("|   P: 3                                       |")
  print("|   Q: 2                                       |")
  print("|   E: -2x2 +4x1 +3                            |",end="\n|                                              |\n")
  cprint("+==============================================+", end = "\n\n",color='red')
  


if __name__ == "__main__":
  instructions()

  cprint("+=== P's and Q's ===-",'red')

  p1 = int(input('| Unfactored P: '))
  q1 = int(input('| Unfactored Q: '))
  eq = input("| Equation: ")
  #p1 = 6
  #q1 = 6
  #eq = "+6x3 +19x2 +1x1 -6"
  p,q = arrays(p1,q1)
  pq = divide(p,q)
  solutions = []
  for i in pq:
    print("CHECKING: ", i)
    check = mathematize(eq,i)
    if check[0]:
      solutions.append(i)
  print("SOL: ",solutions)
