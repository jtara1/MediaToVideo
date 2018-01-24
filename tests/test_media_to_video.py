import sys
import os
import shutil
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from media_to_video import MediaToVideo

path = os.path.join(os.path.dirname(__file__), "media")
output_path = os.path.join(path, MediaToVideo.relative_output_directory)


def cleanup_old_tests(func):
    def run():
        shutil.rmtree(output_path)
        func()
    return run


@cleanup_old_tests
def test1():
    m2v = MediaToVideo(src_path=path,
                       interval_duration=3,
                       dont_load_renders_heap=True)
    m2v.render(True)
    assert(m2v.render_queue.qsize() == 1)
    assert(len(os.listdir(output_path)) == 1)


if __name__ == "__main__":
    test1()
