def generate_necklace(num1, num2):
  past = num1
  current = num2
  necklace = [past]
  necklace.append(current)
  tmp = 0

  while True:
    tmp = (past + current) % 10
    necklace.append(tmp) 
    if (num1 == current) and (num2 == tmp):
      break
    past=current
    current=tmp
  return necklace

# Read input from the keyboard
while True:
  num1 = int(input("Enter the first single-digit number (or a negative number to exit): "))
  if num1 < 0:
    print("Exiting the program.")
    break
    
  if num1 > 9:
    print("Invalid input. Please enter a single-digit number.")
    continue
    
  num2 = int(input("Enter the second single-digit number (or a negative number to exit): "))
  if num2 < 0:
    print("Exiting the program.")
    break
    
  if num2 > 9:
    print("Invalid input. Please enter a single-digit number.")
    continue
    
# Generate and print the necklace
  necklace = generate_necklace(num1, num2)
  print("Necklace:", necklace)
  print("Necklace Length:", len(necklace))
  print()
