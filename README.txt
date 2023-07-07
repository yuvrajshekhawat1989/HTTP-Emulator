To run part1 follow :
1. Open terminal, go to directory 
	cd “/home/p4/tutorials/exercises/basic”

2. Run command make clean
3. Run command make run

4. Now Run below commands on mininet to open the Host terminals:
	xterm h1
	xterm h2
5. Commands to run on h2’s terminal 
	bash h2-arp.sh 
	python server.py 
6. Command to run on  h1’s terminal
	bash h1-arp.sh 
	python client.py 


To run part2:

1. Open VM's terminal, go to 
	cd “/home/p4/tutorials/exercises/basic”
2. Run command make clean
3. Run command make run

4. You are now on the mininet prompt.Run below commands to open the Host terminals:
	xterm h1
	xterm h2
	xterm h3
5. Commands to run on h3’s terminal 
	bash h3-arp.sh 
	python server.py 

6. Commands to run on h2’s terminal 
	bash h2-arp.sh 
	python cache.py 

7. Command to run on  h1’s terminal 
	bash h1-arp.sh 
	python client.py 




