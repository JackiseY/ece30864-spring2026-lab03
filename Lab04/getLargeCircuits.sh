#######################################################
#   Author:     Jingbo Yue
#   email:      yue53@purdue.edu
#   ID:         ee364b28
#   Date:       2/10/26
#######################################################

# Write your sequence of statements here.

#!/bin/bash

for f in circuits/circuit_*.dat; do
  sz=$(stat -c%s "$f")
  if [ "$sz" -ge 200 ]; then
    basename "$f" | sed 's/^circuit_//' | sed 's/\.dat$//'
  fi
done | sort -r | uniq

exit 0
