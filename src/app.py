# some commnet about your app

# imports
from flask import Flask, render_template
from datetime import date
import socket 
import redis
import os

# step 2: define our connection information for Redis
# Replaces with your configuration information
redis_host = os.environ['REDIS_HOST']
redis_port = os.environ['REDIS_PORT']
redis_password = os.environ['REDIS_PASSWORD']

app = Flask(__name__)

@app.route('/')
def hello_world():

  today = date.today()
  hostname = socket.gethostname()
  ## hostname = socket.getfqdn()
  address = socket.gethostbyname(socket.gethostname())
  redismsg = "test"

# create the Redis Connection object
  try:
   
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
   
        # step 4: Set the hello message in Redis
        r.set("msg:hello", "Hello Redis!!!")

        # step 5: Retrieve the hello message from Redis
        redismsg = r.get("msg:hello")
            
  except Exception as e:
        redismsg = e

  return render_template("index.html", today=today, address=address, hostname=hostname, redismsg=redismsg )
    
## Return: IP


## Return: hostname

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
