import os

def reboot():
	#working
	print "rebooting tiles..."
	os.system("ssh pi@192.168.1.103 sudo reboot & ssh pi@192.168.1.104 sudo reboot & ssh pi@192.168.1.105 sudo reboot & ssh pi@192.168.1.106 sudo reboot")
	return;

def udpstream(name):
	f=open('path.tmp','w')
	f.write(name)
	f.close()
	os.system("ssh pi@192.168.1.103 pwomxplayer --tile-code=41 udp://239.0.1.23:1234?buffer_size=1200000B & ssh pi@192.168.1.104 pwomxplayer --tile-code=42 udp://239.0.1.23:1234?buffer_size=1200000B & ssh pi@192.168.1.105 pwomxplayer --tile-code=43 udp://239.0.1.23:1234?buffer_size=1200000B & ssh pi@192.168.1.106 pwomxplayer --tile-code=44 udp://239.0.1.23:1234?buffer_size=1200000B & ./stream.sh")
 	return;

def switchoff():
	os.system("ssh pi@192.168.1.102 sudo shutdown -h now & ssh pi@192.168.1.103 sudo shutdown -h now & ssh pi@192.168.1.104 sudo shutdown -h now & ssh pi@192.168.1.105 sudo shutdown -h now & ssh pi@192.168.1.106 sudo shutdown -h now")
  

#updstream();

#reboot();





