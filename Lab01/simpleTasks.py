# ######################################################
# Author : Jingbo Yue
# email  : yue53@purdue.edu
# ID     : ee364b28
# Date   : 2026 01 16
# ######################################################

import os
import sys

# ######################################################
# No Module-Level Variables or Statements!
# ONLY FUNCTIONS BEYOND THIS POINT!
# ######################################################

def writePyramids(filePath: str, baseSize: int, count: int, char: str) -> None:
    
    height = (baseSize + 1) // 2
    lines = []

    for row in range(height):
        num_chars = 2 * row + 1                      
        left_spaces = (baseSize - num_chars) // 2    
        pyramid_line = (" " * left_spaces) + (char * num_chars) + (" " * left_spaces)

        row_line = " ".join([pyramid_line] * count)
        lines.append(row_line)

    with open(filePath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def getStreaks(sequence: str, letters: str) -> list[str]:
    allowed = set(letters)
    streaks = []

    current = ""          
    current_char = None   

    for ch in sequence:
        if ch in allowed:
            if current == "" or ch != current_char:
                if current != "":
                    streaks.append(current)
                current = ch
                current_char = ch
            else:
                current += ch
        else:
            if current != "":
                streaks.append(current)
                current = ""
                current_char = None

    if current != "":
        streaks.append(current)

    return streaks


# ######################################################
# This block is optional and can be used for testing.
# We will NOT look into its content.
# ######################################################
if __name__ == "__main__":
    # --- Test writePyramids ---
    writePyramids("pyramid13_test.txt", 13, 6, "X")
    writePyramids("pyramid15_test.txt", 15, 5, "*")

    # --- Test getStreaks ---
    seq = "AAASSSSSSAPPPSSPPBBCCCSSS"
    print(getStreaks(seq, "SAQT"))  # expect: ['AAA', 'SSSSSS', 'A', 'SS', 'SSS']
    print(getStreaks(seq, "PAZ"))   # expect: ['AAA', 'A', 'PPP', 'PP']
