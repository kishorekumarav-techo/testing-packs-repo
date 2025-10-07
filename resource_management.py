import os

class TraceFileHandler:
    def write_data(self, file_path, data):
        f = open(file_path, 'w') 
        f.write(data)

class CacheManager:
    def __init__(self):
        self.cache_data = bytearray(1024*1024*50)

    def clear_large_resource(self):
        pass
