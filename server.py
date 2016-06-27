import os
import zmq

RESTART = 'max_id.txt'


def serve(port=5555, restart_file=RESTART):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://*:%s' % port)

    if not os.path.exists(restart_file):
        with open(restart_file, 'w') as fout:
            fout.write('0')

    with open(restart_file) as fin:
        curr_id = int(fin.read())

    while True:
        ids_req = socket.recv_json()
        ids_rep = {'begin': curr_id}
        curr_id += ids_req['count']
        ids_rep['end'] = curr_id
        with open(restart_file, 'w') as fout:
            fout.write(str(curr_id))
        socket.send_json(ids_rep)


if __name__ == '__main__':
    serve()
