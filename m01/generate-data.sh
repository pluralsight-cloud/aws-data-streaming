#!/usr/bin/env bash

STREAM_NAME="YOUR-STREAM-NAME"
PARTITION_KEY="test-key"

counter=1

while true; do
    payload=$(jq -nc \
        --arg count "$counter" \
        --arg ts "$(date -u +"%Y-%m-%dT%H:%M:%SZ")" \
        '{counter: ($count|tonumber), timestamp: $ts}')

    aws kinesis put-record \
        --stream-name "$STREAM_NAME" \
        --partition-key "$PARTITION_KEY-$counter" \
        --data "$(echo -n "$payload" | base64)"

    echo "Sent record $counter"
    counter=$((counter + 1))

    sleep 1
done
