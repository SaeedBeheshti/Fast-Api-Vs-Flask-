#!/bin/bash

URLS=("http://localhost:5000" "http://localhost:5001")
METHODS=("GET" "POST" "PUT" "DELETE" "PATCH")

for METHOD in "${METHODS[@]}"; do
    echo "=== Method: $METHOD ==="
    RESP1=$(curl -s -i -X $METHOD ${URLS[0]})
    RESP2=$(curl -s -i -X $METHOD ${URLS[1]})

    echo "FastAPI (5000):"
    echo "$RESP1"
    echo
    echo "Flask (5001):"
    echo "$RESP2"
    echo

    if [ "$RESP1" == "$RESP2" ]; then
        echo "[✅ Identical]"
    else
        echo "[⚠️ Different]"
    fi
    echo "-------------------------------"
done
