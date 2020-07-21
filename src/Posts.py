import os
stream = os.popen('echo "Hello" > ./Posts.tsv')
output = stream.read()
output
