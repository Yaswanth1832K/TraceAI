class LogFormatter:
    def format_event(self, data):
        """
        Extracts nested metadata details and formats them into a flat structure.
        """
        # This function attempts to parse metadata deeply.
        user = data.get('user', 'anonymous')
        event_type = data.get('event')
        
        # Deep inspection of metadata. If metadata key is totally missing,
        # it will throw a KeyError or TypeError when we try to do .get() on None, etc.
        # But data.get('metadata') returns None if 'metadata' is not a key.
        # We try to access keys directly on the metadata dictionary without checking if it exists.
        
        metadata_dict = data['metadata'] # Potential KeyError: 'metadata'
        
        ip_addr = metadata_dict.get('ip', 'Unknown IP')
        details = metadata_dict.get('item', 'No item specified')
        
        return {
            'username': user,
            'event': event_type,
            'ip': ip_addr,
            'details': details
        }
