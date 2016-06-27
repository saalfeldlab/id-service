import zmq
import ids_pb2

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

curr_id, max_id = 0, 2**64-1
max_count = 10000
while True:
    msg = socket.recv()
    ids_req = ids_pb2.IdsRequest()
    ids_req.ParseFromString(msg)

    ids_rep = ids_pb2.IdsReply()
    ids_rep.begin = curr_id
    curr_id = min(max_id, curr_id + min(ids_req.count, max_count))
    ids_rep.end = curr_id

    socket.send(ids_rep.SerializeToString())
