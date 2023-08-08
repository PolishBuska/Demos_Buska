


class FileException(Exception):
    def __int__(self,extension,message = "invalid format"):
        self.extension = extension
        self.message = message
        super().__init__(self.message)
