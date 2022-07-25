import os
import sys

os.system('git fetch')
os.system('git pull')

with open('lock.txt') as file:
    status = file.read()

if status == 'locked':
    print('server is Locked!')
    sys.exit()

with open('lock.txt', 'w') as file:
    file.write('locked')

os.system('git add .')
os.system('git commit -m "LOCKED"')
os.system('git push')

os.system('java -Xms6G -Xmx6G -jar server.jar nogui')

with open('lock.txt', 'w') as file:
    file.write('unlocked')

os.system('git add .')
os.system('git commit -m "saved"')
os.system('git push')
