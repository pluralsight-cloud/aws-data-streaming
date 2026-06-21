# Sending Records with Boto3 

```python
import json
import boto3

STREAM_NAME = "YOUR_STREAM_NAME"

kinesis = boto3.client("kinesis")

purchases = [
    {"product": "coffee_mug", "qty": 1},
    {"product": "notebook", "qty": 2},
    {"product": "pen", "qty": 3},
]

for purchase in purchases:
    response = kinesis.put_record(
        StreamName=STREAM_NAME,
        PartitionKey="product_purchases",
        Data=json.dumps(purchase)
    )

print(
    response["ShardId"],
    response["SequenceNumber"]
)

```