#######################################################
#   Author:     Jingbo Yue
#   email:      yue53@purdue.edu
#   ID:         ee364b28
#   Date:       2/10/26
#######################################################

# Write your sequence of statements here.
#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: ./getProjectsUsingSmallestCircuit.sh <outputFile>"
    exit 1
fi
out=$1
smallfile=$(stat -c '%s %n' ./circuits/circuit_*.dat 2>/dev/null | sort -n | head -1 | awk '{print $2}')

if [ -z "$smallfile" ]; then
  > "$out"
  exit 0
fi

smallid=$(basename "$smallfile" | sed 's/^circuit_//; s/\.dat$//')

tail -n +3 ./maps/projects.dat \
  | awk -v cid="$smallid" '$1==cid {print $2}' \
  | sort -u > "$out"

exit 







