# id-service

Simple zeroMQ based service to get unique ranges of IDs

To set up on Ubuntu:
- install the following packages: python-zmq, python-protobuf, protobuf-compiler
- run 'make'
- run 'server' and 'client' scripts. The client requires passing desired number of IDs as a command line argument.

The server logic is very simple: it generates unique IDs incrementally starting from 0 (uint64). I thought about some mechanism for releasing IDs so they could be reused later on but decided not to implement it. Even with extremely high load, for instance 1,000,000 clients each requesting 10,000 IDs per second, the maximum possible value would be reached in ~60 years so it isn't worth it.

The resulting message contains a range of globally unique IDs in a form of [begin, end). This allows the server to process any client in constant time and reply with a short fixed-length message.
I limited the maximum IDs count per request to 10,000. Certainly, a client can obtain more by sending more than one request.
