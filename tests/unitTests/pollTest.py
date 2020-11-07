from xmlrpc.client import ServerProxy

s = ServerProxy('http://localhost:9000')

s.getResponsesPoll("Toulouse", "VEGA-6000")

s.getResponsesPoll("Paris","Challenger-6000")