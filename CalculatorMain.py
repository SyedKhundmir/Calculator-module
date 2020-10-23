from ArithmaticPackage import operations

l = []
def demo(data):
   operand = ''
   for val in data:
       if val not in ['+','-','*','/','//','%']:
           operand += val
       else:
           l.append(operand)
           l.append(val)
           operand = ''
   else:
       l.append(operand)
       arithmetic(l)

def arithmetic(l):
    cal = int(l[0])
    operator = ''
    for i in l[1:]:
        if i in ['+','-','*','/','//','%']:
            operator = i
            continue
        if i not in ['+','-','*','/','//','%'] and operator == '+':
            res = operation.add(cal, int(i))
            cal = res
        elif i not in ['+','-','*','/','//','%'] and operator == '-':
            res = operation.sub(cal, int(i))
            cal = res
        elif i not in ['+','-','*','/','//','%'] and operator == '*':
            res = operation.mul(cal, int(i))
            cal = res
        elif i not in ['+', '-', '*', '/', '//', '%'] and operator == '/':
            res = operation.div(cal, int(i))
            cal = res
        elif i not in ['+', '-', '*', '/', '//', '%'] and operator == '%':
            res = operation.mod(cal, int(i))
            cal = res
    print("result:\t",cal)

data = list(input("Note: If there exist *,/,% then place it in the start of expression\nEnter your Calculation :\t"))
res = demo(data)
