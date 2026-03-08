class StoreManager:
    def __init__(self):
        self._database = []
        
    def save_record(self, record):
        """
        Appends the fully formatted record into our mock memory database.
        """
        self._database.append(record)
        return len(self._database)
    
    def get_all_records(self):
        return self._database
