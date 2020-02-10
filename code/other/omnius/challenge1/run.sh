#!/bin/bash
# 2020 Ramon Romero @RamonRomeroQro


if [[ -d ./outputs ]]; then
    echo 'Deleting previous test ./outputs'
    rm -rf ./outputs
fi

mkdir ./outputs

for filename in ./inputs/*.json; do
    echo 'Running test '$filename' ...'
    python3 program.py $filename >"./outputs/$(basename "$filename" .json).txt"
done
