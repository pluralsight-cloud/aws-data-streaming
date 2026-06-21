# How to Consume Records from Kinesis with the AWS CLI

## Get the Shard ID for the Stream:

```bash
STREAM_NAME="YOUR_STREAM_NAME"

aws kinesis list-shards \
  --stream-name "$STREAM_NAME" \
  --query 'Shards[*].ShardId' \
  --output text
```

## Set the Shard ID as a variable

```bash
SHARD_ID="YOUR_SHARD_ID"
```

## Verify the Shard ID:

```bash
aws kinesis list-shards \
  --stream-name "$STREAM_NAME"
```

## Get Shard Iterators

Get a shard iterator from the start of the data in the shard:

```bash
aws kinesis get-shard-iterator \
  --stream-name "$STREAM_NAME" \
  --shard-id "$SHARD_ID" \
  --shard-iterator-type TRIM_HORIZON
```

Use the Shard iterator to get records:

```bash
aws kinesis get-records \
  --shard-iterator "SHARD_ITERATOR"
```

If there is another `NextShardIterator` in the returned data:

```bash
aws kinesis get-records \
  --shard-iterator "NEXT_SHARD_ITERATOR"
```

You may also need to decode the data if it is in base64:

```bash
aws kinesis get-records \
  --shard-iterator "SHARD_ITERATOR" \
  --query 'Records[*  ].Data' \
  --output text | base64 --decode
```
