#!/bin/bash
# sequential single-core job chain
cd /home/user/work/agent3
while pgrep -f "verify 17167680177565" >/dev/null; do sleep 10; done
( cd a072872 && nice -n 10 timeout 1500 ./c 1000000 0 > c1e6.out 2>&1 )
( cd a126762 && nice -n 10 timeout 900 ./c 1000000 > c1e6.out 2>&1 )
( cd a346154 && nice -n 10 timeout 900 ./cov2 1000 30000000 80 300 > cov.out 2> cov.err )
( cd a114782 && nice -n 10 timeout 1800 gp -q big.gp < /dev/null > big.out 2>&1 )
( cd a051924 && nice -n 10 timeout 1200 ./c 150000 > c150k.out 2>&1 )
echo ALLDONE > chain.done
