# RPN-calculator-python
RPN calculator using python

import operator

ops = { '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv
}

def eval_expression(tokens, stack):
  
    for token in tokens:
        if set(token).issubset(set("0123456789.")):
            stack.append(float(token))
        elif token in ops:
            if len(stack) < 2:
                raise ValueError('Must have at least two parameters to perform op')
            a = stack.pop()
            b = stack.pop()
            op = ops[token]
            if(op == operator.floordiv and a == 0):
              print("Division not possible")
              raise ZeroDivisionError("Zero cannot divide a number")
           
            stack.append(op(b,a))
        else:
            raise ValueError("WTF? %s" % token)
    return stack

if __name__ == '__main__':
    stack = []
    while True:
        expression = input('> ')
        if expression in ['quit','q','exit']:
            exit()
        elif expression in ['clear','empty']:
            stack = []
            continue
        elif len(expression)==0:
            continue
        stack = eval_expression(expression.split(), stack)
        print(stack)
