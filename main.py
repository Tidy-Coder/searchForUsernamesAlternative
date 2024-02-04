# This is Python code...
while True:
  tidyInput = input("Please enter a username, or enter \"exit\" to exit...")
  if tidyInput.upper().replace(" ", "") == "EXIT":
    break
  tidyOrganizedInput = []
  theAlphabet = "abcdefghijklmnopqrstuvwxyz"
  for i in tidyInput:
    if i in theAlphabet.upper():
      tidyOrganizedInput += [i]
    else:
      if tidyOrganizedInput == []:
        tidyOrganizedInput = [i]
      elif len(tidyOrganizedInput) == 1:
        tidyOrganizedInput[1] += [i]
      tidyOrganizedInput[-1] += [i]
  print("-".join(tidyOrganizedInput))
  print("~".join(tidyOrganizedInput))
  print("the" + tidyInput[0].upper() + tidyInput[1])
  print(tidyInput + "Account")
