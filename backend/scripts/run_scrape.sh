#!/bin/bash

HTTP_CODE=$(curl -X PATCH -H "Accept: application/json" -H "Content-Type: application/json" --write-out "%{http_code}\n" "127.0.0.1:80/scrape" --silent)
echo $HTTP_CODE