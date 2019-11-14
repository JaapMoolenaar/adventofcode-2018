import time

from . import cache
from . import app

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/test')
def test():
    count = get_hit_count()
    return 'Hello World! I have been seen {} timess.\n'.format(count)