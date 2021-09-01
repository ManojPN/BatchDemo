import boto3

session = boto3.session.Session(region_name= 'us-east-1')

db_client = session.client('dynamodb')

items_count = 100

for i in range(items_count):
    response = db_client.put_item(
        TableName='DemoTable',
        Item={
            'PrimKey': i,
            'SortKey': "Welcome "+ i
        })
