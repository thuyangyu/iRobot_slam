#import subprocess
#subprocess.run(['python', 'listener.py'], shell=True)

import os
os.system('cd /home/nvidia/SSD/ssd; python3 demo.py --cpu --images ./data/demo/trash.jpg --thresh .5')

print ('Hi there, Turtlebot is here!')
