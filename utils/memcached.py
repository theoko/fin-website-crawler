from pymemcache.client import base


class MemcachedUtils:
    def __init__(self):
        self.client = base.Client(('localhost', 11211))

    def flush(self):
        self.client.flush_all()

    def close(self):
        self.client.close()

    def __del__(self):
        self.client.close()
