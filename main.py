# This is Python code...
import time
tidyLocation = 0
tidyHello = "hello!!!"
for ib in tidyHello:
  if tidyLocation == 0:
    print(tidyHello[0])
  else:
    print(tidyHello[:tidyLocation + 1])
  tidyLocation += 1
  time.sleep(0.15)
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
        tidyOrganizedInput = [[i]]
      elif len(tidyOrganizedInput) == 1:
        tidyOrganizedInput[0] += i
      else:
        tidyOrganizedInput[-1] += i
  print("-".join(tidyOrganizedInput))
  print("_".join(tidyOrganizedInput))
  print("~".join(tidyOrganizedInput))
  print("the" + tidyInput[0].upper() + tidyInput[1])
  print(tidyInput + "Account")
  print(tidyInput + "Professional")
  print(tidyInput + "IsProfessional")
  print("-".join(tidyOrganizedInput + ["Account"]))
  print("_".join(tidyOrganizedInput + ["Account"]))
  print("~".join(tidyOrganizedInput + ["Account"]))
  print("-".join(["Professional"] + tidyOrganizedInput))
  print("_".join(["Professional"] + tidyOrganizedInput))
  print("~".join(["Professional"] + tidyOrganizedInput))
  print("-".join(["Account"] + tidyOrganizedInput))
  print("_".join(["Account"] + tidyOrganizedInput))
  print("~".join(["Account"] + tidyOrganizedInput))
  print("-".join(tidyOrganizedInput + ["Professional"]))
  print("_".join(tidyOrganizedInput + ["Professional"]))
  print("~".join(tidyOrganizedInput + ["Professional"]))
  print("-".join(tidyOrganizedInput + ["isProfessional"]))
  print("_".join(tidyOrganizedInput + ["isProfessional"]))
  print("~".join(tidyOrganizedInput + ["isProfessional"]))
