# Update the number of shards to 2:

```bash
aws kinesis update-shard-count \
  --stream-name YOUR-STREAM-NAME \
  --target-shard-count 2 \
  --scaling-type UNIFORM_SCALING
```

# Show the current status of a stream or scaling operation:

```bash
aws kinesis describe-stream-summary \
  --stream-name YOUR-STREAM-NAME \
  --query 'StreamDescriptionSummary.{Status:StreamStatus,Shards:OpenShardCount}'
```

# Merge the number of shards back to 1:

```bash
aws kinesis update-shard-count \
  --stream-name YOUR-STREAM-NAME \
  --target-shard-count 1 \
  --scaling-type UNIFORM_SCALING
```
