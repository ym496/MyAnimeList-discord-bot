"""To get the URL-encoded name of the requested query."""

def getname(name):
  list_name = list(name.split(' '))
  output = '%20'.join(list_name)
  return output


