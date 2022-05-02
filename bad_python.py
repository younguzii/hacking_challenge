import json
import os

stream = os.popen('id')
output = stream.read()
result = {"result": output}
result = json.dumps(result)

print(result)
