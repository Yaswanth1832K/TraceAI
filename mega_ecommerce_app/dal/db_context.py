class DatabaseContext:
    def __init__(self):
        self.connected = True

    def query(self, sql):
        # Mock database response
        return [100] 
