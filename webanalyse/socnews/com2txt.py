import os
cmd_path = os.path.dirname(__file__)+'/python'
print(cmd_path)
cmd = [cmd_path, 'test.py','> msg.txt']
os.execv(cmd_path,cmd)