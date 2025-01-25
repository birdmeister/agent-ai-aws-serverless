# Agent.ai AWS Serverless action
Sample code for using an AWS serverless function on Agent.ai

Overall flow:
1. Get user input (type number) with a prompt and save to 'value_a'
2. Get user input (type number) with a prompt and save to 'value_b'
3. Create an Advanced action type Serverless function (see 'demo_aws_serverless.py')
4. Output is a variable named 'answer', which is a string (not a JSON object string)
5. Last step is a Show Output Action to show 'answer' to the user. It is of type Text 
