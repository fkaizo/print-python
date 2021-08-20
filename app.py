from graphql_client import GraphQLClient
from ecspos import printer

query = """
  subscription {
    printAdded {
      title
    }
  }
"""
p = printer.File()
def callback(_id, data):
  text = data['payload']['data']['printAdded']['title']
  p.text(text[0:500])
  p.text('\n')
  p.text('--------------------------------\n\n')
  print(f"> {text}")

try:
  while True:
    with GraphQLClient('wss://print.labgamma.com.br/graphql') as client:
        sub_id = client.subscribe(query, callback=callback)
except KeyboardInterrupt:
  print("bye...")
  quit()
except Exception:
  print("caiu")
    # finally:
    #   client.stop_subscribe(sub_id)

  # do other stuff
  # ...
  # later stop the subscription