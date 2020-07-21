import os
stream = os.popen('echo "Hello" > ./Posts-test.tsv')
output = stream.read()
output
