import sys

n = int(input())
q = []

for i in range(n):
  order = sys.stdin.readline().rstrip()
  if "push_front" in order:
    q.insert(0, int(order[11:]))
  elif "push_back" in order:
    q.append(int(order[10:]))
  elif "pop_f" in order:
    if len(q) > 0:
      print(q.pop(0))
    else:
      print(-1)
  elif "pop_b" in order:
    if len(q) > 0:
      print(q.pop())
    else:
      print(-1)
  elif order == 'size':
    print(len(q))
  elif order == 'empty':
    print(0 if len(q) > 0 else 1)
  elif order == 'front':
    if len(q) > 0:
      print(q[0])
    else:
      print(-1)
  else:
    if len(q) > 0:
      print(q[-1])
    else:
      print(-1)
