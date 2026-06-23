# Previously Picked Single Key

```py
import json
import boto3

kinesis = boto3.client("kinesis")

purchase = {
    "customer_id": "cust-123",
    "product": "coffee_mug",
    "qty": 1
}

kinesis.put_record(
    StreamName=stream_name,
    PartitionKey="product_purchases",
    Data=json.dumps(purchase)
)
```


# Swap to a Partition Key with Multiple Values

```py
import json
import boto3

kinesis = boto3.client("kinesis")

purchase = {
    "customer_id": "cust-123",
    "product": "coffee_mug",
    "qty": 1
}

kinesis.put_record(
    StreamName=stream_name,
    PartitionKey=purchase["customer_id"],
    Data=json.dumps(purchase)
)
```

# Avoiding Hot Spotting or Hot Sharding

```py
import random

customer_id = purchase["customer_id"]

partition_key = (
    f"{customer_id}-{random.randint(0, 9)}"
)
```
