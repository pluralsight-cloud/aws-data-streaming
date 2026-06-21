# Send Records with the AWS CLI

```bash
STREAM_NAME="YOUR_STREAM_NAME"

aws kinesis put-record \
  --stream-name $STREAM_NAME \
  --partition-key product_purchases \
  --data '{"product":"coffee_mug","qty":1}'

aws kinesis put-record \
  --stream-name $STREAM_NAME \
  --partition-key product_purchases \
  --data '{"product":"notebook","qty":1}'

DATA=$(echo '{"product":"notebook","qty":2}'| base64)
aws kinesis put-record \
  --stream-name $STREAM_NAME \
  --partition-key product_purchases \
  --data $DATA

```
