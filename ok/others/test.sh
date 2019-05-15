#!/bin/bash

# Copyright 2019 © Ramon Romero   @RamonRomeroQro

# This program is free software.
# under the terms of the GNU General Public License

# Test and evaluation

echo 'Deleting previous test ./outputs'
rm -rf ./outputs
mkdir ./outputs


for filename in ./tests/*.tsv; do
    echo 'Running test '$filename' ...'
    python3 program.py $filename > "./outputs/$(basename "$filename")"
    diff "./outputs/$(basename "$filename")" expected_outputs/$(basename "$filename")
    if [ $? -eq 0 ]
        then
        echo -e "\t -> Success."
    fi
done



