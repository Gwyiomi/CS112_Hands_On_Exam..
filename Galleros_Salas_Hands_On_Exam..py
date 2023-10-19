print("***********************************************************************")
print("Press 1 for Decimal to Binary converter"
      "\nPress 2 for Decimal to Octal number converter"
      "\nPress 3 for Decimal to Hexadecimal converter")
print("***********************************************************************")
choices = int(input("Input here:"))
print("***********************************************************************")
if choices == 1:
    deci_number = int(input("Enter a Decimal number:"))
    print("Binary Number:" + format(deci_number, "b"))
elif choices == 2:
    deci_number = int(input("Enter a Decimal number:"))
    print("Octal Number:" + format(deci_number, "o"))
elif choices == 3:
    deci_number = int(input("Enter a Decimal number:"))
    print("Hexadecimal Number:" + format(deci_number, "x"))
else:
    print("Invalid Input. Please try again")
