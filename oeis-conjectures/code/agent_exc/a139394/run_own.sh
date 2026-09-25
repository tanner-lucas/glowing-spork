#!/bin/bash
nice -n 10 timeout 1200 ./race_own 0 50000000000 0 0 3 100000000000 200000000000 > own_chunk1.txt 2>&1
read A B LP <<< $(grep ^END own_chunk1.txt | sed -E 's/.* A=([0-9]+) B=([0-9]+) lastp=([0-9]+).*/\1 \2 \3/')
nice -n 10 timeout 1200 ./race_own 50000000000 101666666667 $A $B $LP 608981813017 608981813018 608981813123 608981813124 608981813029 608981813030 610000000000 > own_chunk2.txt 2>&1
