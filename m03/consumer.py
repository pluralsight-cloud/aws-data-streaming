import json
import random
import time

import boto3

STREAM_NAME = "product-sales"

kinesis = boto3.client("kinesis")

print("Discovering shard...")

shard_id = kinesis.list_shards(
    StreamName=STREAM_NAME
)["Shards"][0]["ShardId"]

iterator = kinesis.get_shard_iterator(
    StreamName=STREAM_NAME,
    ShardId=shard_id,
    ShardIteratorType="LATEST"
)["ShardIterator"]

print(f"Using shard {shard_id}")
print("Starting consumer...")

while True:
    response = kinesis.get_records(
        ShardIterator=iterator,
        Limit=1
    )
    iterator = response["NextShardIterator"]
    records = response["Records"]
    if not records:
        time.sleep(1)
        continue
    for record in records:
        event = json.loads(
            record["Data"].decode("utf-8")
        )
        product = event["product"]
        category = event["category"]
        print(
            f"[CONSUMER] "
            f"Processing "
            f"product={product:<15} "
            f"category={category}"
        )
        if (category == "electronics" and random.random() < 0.50):
            print(
                f"[CONSUMER] "
                f"Inventory verification required "
                f"for {product}"
            )
            time.sleep(10)
            print(
                f"[CONSUMER] "
                f"Inventory verification complete "
                f"for {product}"
            )
