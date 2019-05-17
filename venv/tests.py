from unittest.mock import patch
from wiki import *

c = requests.Session()
print(type(c))

@patch('wiki.requests.sessions.Session')
def test(MockClass):
    MockClass = requests.Session()
    assert MockClass is requests.sessions.Session()
    assert MockClass.called

test()