class FileManager:
    def __enter__(self):
        print("Entering the context")
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
with FileManager():
    print("Working within the context")