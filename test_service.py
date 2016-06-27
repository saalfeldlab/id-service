from server import serve
import tempfile
from client import request
import pytest
import threading
import random


@pytest.fixture
def temporary_file():
    tf = tempfile.NamedTemporaryFile('w', delete=False)
    tf.close()
    return tf.name


def test_service(temporary_file):
    with open(temporary_file, 'w') as fout:
        restart = random.randint(1000, 2000)
        fout.write(str(restart))
    thread = threading.Thread(target=serve, daemon=True,
                              kwargs=dict(restart_file=temporary_file))
    thread.start()
    count = random.randint(1000, 2000)
    start, end = request(count)
    assert end - start == count
    assert start == restart
    with open(temporary_file, 'r') as fin:
        assert int(fin.read()) == end
    thread.join(timeout=0.025)
