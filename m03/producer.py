import json
import random
import time
import uuid

import boto3

STREAM_NAME = "product-sales"

kinesis = boto3.client("kinesis")

products = [
    ("coffee_mug", "home"),
    ("notebook", "office"),
    ("pen", "office"),
    ("water_bottle", "home"),
    ("laptop", "electronics"),
    ("gaming_pc", "electronics"),
    ("4k_monitor", "electronics"),
]

weights = [
    40,
    30,
    20,
    15,
    3,
    2,
    2,
]

print("Starting producer...")

while True:
    product, category = random.choices(
        products,
        weights=weights
    )[0]
    event = {
        "order_id": str(uuid.uuid4()),
        "product": product,
        "category": category,
        "qty": random.randint(1, 3),
        "timestamp": time.time(),
    }
    kinesis.put_record(
        StreamName=STREAM_NAME,
        PartitionKey="product_sales",
        Data=json.dumps(event)
    )
    print(
        f"[PRODUCER] "
        f"product={product:<15} "
        f"category={category}"
    )
    time.sleep(0.25)
