import os
import zmq

RESTART = 'max_id.txt'


def serve(port=5555):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://*:%s' % port)

    if not os.path.exists(RESTART):
        with open(RESTART, 'w') as fout:
            fout.write('0')

    with open(RESTART) as fin:
        curr_id = int(fin.read())

    while True:
        ids_req = socket.recv_json()
        ids_rep = {'begin': curr_id}
        curr_id += ids_req['count']
        ids_rep['end'] = curr_id
        with open(RESTART, 'w') as fout:
            fout.write(str(curr_id))
        socket.send_json(ids_rep)


if __name__ == '__main__':
    serve()
