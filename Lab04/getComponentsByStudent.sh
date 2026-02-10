#######################################################
#   Author:     Jingbo Yue
#   email:      yue53@purdue.edu
#   ID:         ee364b28
#   Date:       2/10/26
#######################################################

# Write your sequence of statements here.
#!/bin/bash

if [ $# -ne 1 ]; then
    echo 'Usage: ./getComponentsByStudents.sh “Last, First"'
    exit 1
fi

name="$1"

sid=$(grep -F "$name" maps/students.dat | cut -d'|' -f2 | tr -d ' ')
if [ -z "$sid" ]; then
  exit 0
fi

grep -l -F "$sid" circuits/circuit_*.dat \
| xargs -I {} grep -oE '[A-Z]{3}-[0-9]+' {} \
| sort -u

exit 0


