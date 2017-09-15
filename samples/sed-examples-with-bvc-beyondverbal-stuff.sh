#!/bin/bash

OUTPUT_FILENAME='output.json'

python2.7 bvc.py >${OUTPUT_FILENAME} 2>&1

# Remove u's from JSON.
sed -i -e "s/u'/'/g" ${OUTPUT_FILENAME}

# If there are any double quotes, eliminate them.
sed -i -e "s/\"//g" ${OUTPUT_FILENAME}

# Turn single into double quotes.
sed -i -e "s/'/\"/g" ${OUTPUT_FILENAME}


echo "Printing results: "
cat ${OUTPUT_FILENAME} | jq '.'
