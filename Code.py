n = input("Enter the first list of words separated by commas: ").split(',')
m = input("Enter the second list of words separated by commas: ").split(',')
queue=[]
queue.append(m)
queue.extend(n)
for line in list(m):
  if len(queue) < 5:
      queue.append(line)
      print(queue)
      print('\n')
  elif len(queue) == 5:
      queue.pop(0)
      queue.append(line)
      for i in queue:
        print(i)
      print('\n')