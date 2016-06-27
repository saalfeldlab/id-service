import zmq
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("count", type=int, help="wanted IDs count")


def request(count):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    ids_req = {'count': count}
    print("Requesting %d ids.." % ids_req['count'])
    socket.send_json(ids_req)

    ids_rep = socket.recv_json()
    return ids_rep['begin'], ids_rep['end']


if __name__ == '__main__':
    args = parser.parse_args()
    start, end = request(args.count)
    print('got ids %s to %s.' % (start, end))
