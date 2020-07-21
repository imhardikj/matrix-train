import os
stream = os.popen('echo "Hello" > ./data/matrix-train.p')
output1 = stream.read()
stream = os.popen('echo "Hello" > ./data/matrix-test.p')
output2 = stream.read()
stream = os.popen('echo "Hello" > ./data/model.p')
output3 = stream.read()
output1
output2
output3
