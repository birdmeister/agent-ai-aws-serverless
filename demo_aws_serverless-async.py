import asyncio
import json

async def multiply(a, b):
  return a * b
  
async def lambda_handler(event, context):
    try:
        if not event.get('body'):
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": "Missing request body"})
            }

        data = json.loads(event['body'])
        a = data["context"]["value_a"]
        b = data["context"]["value_b"]
        
        answer = await multiply(a, b)

        if not answer:
            await asyncio.sleep(3)

        return {
            "statusCode": 200,
            "body": answer
        }
    
    except (KeyError, ValueError, TypeError) as e:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "error": "Invalid input. Please provide numbers for 'a' and 'b'",
                "details": str(e)
            })
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "error": "Internal server error",
                "details": str(e)
            })
        }
    
def execute(event, context):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    return loop.run_until_complete(lambda_handler(event, context))
