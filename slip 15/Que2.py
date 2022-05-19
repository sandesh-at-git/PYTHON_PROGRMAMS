import os
count = 0
for path in os.listdir():

    if os.path.isfile(os.path.join( path)):
        count += 1
print('File count:', count)