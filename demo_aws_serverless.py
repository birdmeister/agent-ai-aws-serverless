import json

def multiply(a, b):
  return a * b
  
def execute(event, context):
    if not event or 'body' not in event:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing request body"})
        }
    
    try:
        data = json.loads(event['body'])
        a = data["context"]["value_a"]
        b = data["context"]["value_b"]
        
        answer = multiply(a, b)
        
        body = {
            "result": answer,
            "input": {"a": a, "b": b}
        }
        
        return {
            "statusCode": 200,
            "body": answer
        }
        
    except (KeyError, ValueError, TypeError):
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid input. Please provide numbers for 'a' and 'b'"})
        }
