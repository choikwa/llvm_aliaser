
import sys

aliases = {}
with open(sys.argv[1]) as f_in:
  for chunk in f_in:
    key = chunk[:chunk.find('=')-1]
    value = chunk[chunk.find('{')+1:chunk.rfind('}')]
    value = value.replace(',', '').split()
    value = [x for x in value if len(x)>0 and x[0] == '!']
    if len(key)>0 and key[0] == '!':
      aliases[key] = value


# This method retrieves all nodes that key may touch in mydict.
# Assumes mydict to be simple Directed Graph. Detects cycles and stops.
reaching_aliases = {}
visited = set()
def reachingNodes(mydict, key):
  nodes = set(mydict[key])
  if key in visited:
    return nodes
  visited.add(key)

  if key in reaching_aliases:
    return reaching_aliases[key]

  for v in mydict[key]:
    if v in mydict:
      nodes = nodes | reachingNodes(mydict, v)

  reaching_aliases[key] = nodes
  return nodes

for k in aliases:
  reachingNodes(aliases, k)

with open('reachingAliases.out', 'w') as f_out:
  for k,v in sorted(reaching_aliases.iteritems()):
    f_out.write(k + ": " + str(v) + '\n')
