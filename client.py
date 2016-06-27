import zmq
import sys
import argparse
import ids_pb2

parser = argparse.ArgumentParser()
parser.add_argument("count", type=int, help="wanted IDs count")
args = parser.parse_args()
if args.count < 0:
    print("the count can't be negative")
    sys.exit()

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

ids_req = ids_pb2.IdsRequest()
ids_req.count = args.count
print("Requesting %d ids.." % ids_req.count)
socket.send(ids_req.SerializeToString())

msg = socket.recv()
ids_rep = ids_pb2.IdsReply()
ids_rep.ParseFromString(msg)
print("My ids are %s" % range(ids_rep.begin, ids_rep.end))
