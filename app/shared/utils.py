from bson import ObjectId
import json
from datetime import datetime

class JSONEncoder(json.JSONEncoder):
    """
    Custom JSON encoder to handle MongoDB ObjectId and other non-serializable types.
    """
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

def serialize_mongo_doc(doc):
    """
    Convert MongoDB document to JSON-serializable object.
    
    Args:
        doc: MongoDB document or list of documents
        
    Returns:
        JSON-serializable object
    """
    if doc is None:
        return None
    
    if isinstance(doc, list):
        return [serialize_mongo_doc(item) for item in doc]
    
    if isinstance(doc, dict):
        result = {}
        for key, value in doc.items():
            if isinstance(value, ObjectId):
                result[key] = str(value)
            elif isinstance(value, datetime):
                result[key] = value.isoformat()
            elif isinstance(value, (list, dict)):
                result[key] = serialize_mongo_doc(value)
            else:
                result[key] = value
        return result
    
    return doc
