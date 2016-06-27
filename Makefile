all: server client

clean:
	rm -f server client
	rm -f ids_pb2.py
	rm -f *.pyc

proto: ids.proto
	protoc --python_out=. ids.proto

server: server.py proto
	@echo '#!/bin/sh' > server
	@echo 'python server.py "$$@"' >> server
	@chmod +x server

client: client.py proto
	@echo '#!/bin/sh' > client
	@echo 'python client.py "$$@"' >> client
	@chmod +x client
