from xmlrpc.client import ServerProxy
s1 = ServerProxy('http://localhost:8888')
s1.sendStates("Paris", "SOUL-9000")


