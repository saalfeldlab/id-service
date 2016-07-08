import os
import zmq

def serve(port=9001):
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.bind('tcp://*:%s' % port)

    while True:
        ids_req = socket.recv_json()
        print(ids_req)

if __name__ == '__main__':
    serve()
