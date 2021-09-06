"""To get all the matching results of the requested query."""

def results(data,name,query,type):
  result_list = [f'{str(n + 1)}.   {data[n][name]}' for n in range(0,len(data))]
  pre_message = f'`{len(data)}` {type} found matching `{query}`!'
  post_message = 'Please type the number corresponding to your selection, or type `c` now to cancel.'

  message = '\n '.join(result_list)
  output = f'{pre_message}\n \n```md\n {message}\n```\n {post_message}'
  return output

