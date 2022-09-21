from listStack import *

def parenBalance(s) -> bool:
  operation = { '{':'}', '[':']', '(':')' }
  stack = []
  for ch in s:
    if ch in operation:
      stack.append(ch)
    elif ch in operation.values():
      if stack and operation[stack[-1]] == ch:
        stack.pop()
      else:
        return False
  return False



        
