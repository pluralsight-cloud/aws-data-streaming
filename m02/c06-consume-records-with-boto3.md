# Get the Kinesis Shard ID

```py
import boto3

STREAM_NAME = "YOUR_STREAM_NAME"

kinesis = boto3.client("kinesis")

response = kinesis.list_shards(
    StreamName=STREAM_NAME
)

shard_id = response["Shards"][0]["ShardId"]

print(shard_id)
```

# Get the Shard Iterator

```py
iterator_response = kinesis.get_shard_iterator(
    StreamName=STREAM_NAME,
    ShardId=shard_id,
    ShardIteratorType="TRIM_HORIZON"
)

shard_iterator = iterator_response["ShardIterator"]
```

# Get Records from the Shard: 

```py
records_response = kinesis.get_records(
    ShardIterator=shard_iterator,
    Limit=100
)

for record in records_response["Records"]:
    print(record["Data"])
```
