import sys
import os
# sys.path.append()
from MediaToVideo import MediaToVideo


def test1():
    path = os.path.join(os.path.dirname(__file__), "media")
    m2v = MediaToVideo(src_path=path)
    m2v.render()
