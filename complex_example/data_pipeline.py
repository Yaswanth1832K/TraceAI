import uuid
from log_formatter import LogFormatter
from store_manager import StoreManager

class DataPipeline:
    def __init__(self):
        self.formatter = LogFormatter()
        self.store_manager = StoreManager()
    
    def process_event(self, event_data):
        print(f"[{event_data.get('event')}] Processing event id: {event_data.get('id')}")
        
        # Format the event for logging
        formatted_log = self.formatter.format_event(event_data)
        
        # Save the event to our mock database
        self.store_manager.save_record(formatted_log)
        
        print(f"[{event_data.get('event')}] Successfully stored.")
