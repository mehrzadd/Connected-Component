import sys
import os
import pdb
import timeit

try:
  first_arg = sys.argv[1]
  start1 = timeit.default_timer()

  d = {}
  def main_program (data=first_arg):
    status={}
    node=[]
    with open(data, 'r') as f:
      for line in f:
         (key, val) = line.strip().split('\t')
         if key not in d:
             d[key] = [val]     
         #if key in d and val not in d[key]:
         else:
             d[key].append(val)
         if val not in d:
             d[val]=[key]
         #if val in d and key not in d[val]:
         else:
             d[val].append(key)
         node=d.keys()
    count, component, time =bfs(d, node)
    print("\n\n*******************************")
    print("number of componnets is {}".format(count))
    print("*******************************\n")
    for key, value in component.items():
      component[key]=sorted(value)
    #pdb.set_trace()

    for key, value in component.items(): 
      for key2, value2 in component.items():
        if (component[key2][0]<component[key][0] and key < key2):
          temp=component[key]
          component[key]=component[key2]
          component[key2]=temp

    #print(component)
    for key, value in component.items():
      print("component: {0}".format('\t'.join(map(str, value))))
    print ("running time of this algorithm is "+ time)

  def bfs(graph,node):
  	#pdb.set_trace()
  	comps={}
  	component=0
  	while node:
  	  start=node[0]
  	  component+=1
  	  q=[start]
  	  path=[int(start)]
  	  while q:
  		  v=q.pop(0)
  		  node.remove(v)
  		  for u in graph[v]:
  		    if int(u) not in path:
  		      path.append(int(u))
  		      q.append(u)
  		    graph[u].remove(v)
  	  comps[component]=path
  	stop1 = timeit.default_timer()
  	runtime= float(stop1) - float(start1)
  	return component, comps, str(runtime)

  if __name__ == '__main__':
  	main_program()

except Exception as e:
  print ("please give an input as edgelist")
  sys.stdout.flush()
