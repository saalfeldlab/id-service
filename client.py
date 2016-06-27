import zmq
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("count", type=int, help="wanted IDs count")
args = parser.parse_args()
if args.count < 0:
    print("the count can't be negative")
    sys.exit()

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

ids_req = {'count': args.count}
print("Requesting %d ids.." % ids_req.count)
socket.send_json(ids_req)

ids_rep = socket.recv_json()
print("My ids are %s to %s" % (ids_rep['begin'], ids_rep['end']))
