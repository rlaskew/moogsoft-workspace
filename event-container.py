
import json

## from https://api.docs.moogsoft.com/reference/events-api-object
class Event:
    def __init__(self,
                    description, 
                    severity, 
                    source, 
                    check, 
                    service, 
                    deduplication_key, 
                    alias, 
                    time, 
                    namespace,
                    manager, 
                    manager_id, 
                    location, 
                    event_class, 
                    tags, 
                    utc_offset):

      self.description = description
      self.severity = severity
      self.source = source
      self.check = check
      self.service = service
      self.deduplication_key = deduplication_key
      self.alias = alias
      self.time = time
      self.namespace = namespace
      self.manager = manager
      self.manager_id
      self.location = location
      self.event_class = event_class
      self.tags = tags
      self.utc_offset = utc_offset

a = Event("hello world")
