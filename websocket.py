
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

        
        
        
        
        
        
import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        try:
            await websocket.send(now)
        except websockets.exceptions.ConnectionClosed:
            print("Client disconnected.  Do cleanup")
            break             
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
