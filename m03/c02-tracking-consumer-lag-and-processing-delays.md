# Start by Creating a New Stream

```bash
STREAM_NAME="product-sales"

aws kinesis create-stream \
  --stream-name $STREAM_NAME \
  --shard-count 1


aws kinesis describe-stream-summary \
--stream-name $STREAM_NAME
```

# Run the Demo Producer and Consumer

## Terminal 1:

- Run `python3`
- Paste in `producer.py`

## Terminal 2:

- Run `python3`
- Paste in `consumer.py`

# You should see something like this:

Producer:
[PRODUCER] product=coffee_mug      category=home
[PRODUCER] product=notebook        category=office
[PRODUCER] product=laptop          category=electronics
[PRODUCER] product=pen             category=office

Consumer:
[CONSUMER] Processing product=coffee_mug
[CONSUMER] Processing product=notebook
[CONSUMER] Processing product=laptop
[CONSUMER] Inventory verification required for laptop
