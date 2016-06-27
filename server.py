import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

curr_id, max_id = 0, 2**64-1
while True:
    ids_req = socket.recv_json()
    ids_rep = {'begin': curr_id}
    curr_id += ids_req['count']
    ids_rep['end'] = curr_id
    socket.send_json(ids_rep)
