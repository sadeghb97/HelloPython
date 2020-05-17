def printExceptionMessage(exception) :
    print("Ex Type:", type(exception))
    if hasattr(exception, 'message'):
        print("Ex Message: " + exception.message)
    else: print("Ex Message:", exception)

try :
    op1 = input("Enter Op1: ")
    op2 = input("Enter Op2: ")
    intOp1 = int(op1)
    intOp2 = int(op2)
    result = intOp1 / intOp2
    print("Result: " + str(result))
except (ZeroDivisionError, FloatingPointError) as ex :
    print("Zero Division Or Floating Point Error")
    printExceptionMessage(ex)
except Exception as ex :
    print("Exception occured!")
    printExceptionMessage(ex)
else:
    print("No Exception")
finally:
    print("Try block finished!")