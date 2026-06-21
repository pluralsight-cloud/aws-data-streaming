# Sending Records with Boto3 Aggregation and Collection

```python
import json
import boto3

STREAM_NAME = "YOUR_STREAM_NAME"

kinesis = boto3.client("kinesis")

response = kinesis.put_records(
    StreamName=STREAM_NAME,
    Records=[
        {
            "PartitionKey": "product_purchases",
            "Data": json.dumps({"product": "coffee_mug", "qty": 1}),
        },
        {
            "PartitionKey": "product_purchases",
            "Data": json.dumps({"product": "notebook", "qty": 2}),
        },
        {
            "PartitionKey": "product_purchases",
            "Data": json.dumps({"product": "pen", "qty": 3}),
        },
    ],
)

print(response)
```
