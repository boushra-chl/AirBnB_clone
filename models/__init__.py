#!/usr/bin/python3
"""creates a unique FileStorage instance of the application"""


from .file_storage import FileStorage
storage = FileStorage()
storage.reload()
