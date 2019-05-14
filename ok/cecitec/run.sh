#!/bin/bash

# Copyright 2019 © Ramon Romero   @RamonRomeroQro

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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



