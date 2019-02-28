import bluetooth
from threading import *
# import RPi.GPIO as GPIO        #calling for header file which helps in using GPIOs of PI
LED=21
connection = False
script_end = False
sem_send = Semaphore(0)
sem_recv = Semaphore(0)
# GPIO.setmode(GPIO.BCM)     #programming the GPIO by BCM pin numbers. (like PIN40 as GPIO21)
# GPIO.setwarnings(False)
# GPIO.setup(LED,GPIO.OUT)  #initialize GPIO21 (LED) as an output Pin
# GPIO.output(LED,0)
 
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
 
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
 
client_socket,address = server_socket.accept()
connection = True
sem_recv.release()
sem_send.release()
print "Accepted connection from ",address

def recv():
    global script_end
    global connection
    
    sem_recv.acquire()
    while True:
        data = client_socket.recv(1024)
        print "Received: %s" % data
 
        if (data == "q"):
            print ("Quit")
            script_end = True
            break
 
    client_socket.close()
    server_socket.close()

def send():
    global connection
    global script_end
    
    sem_send.acquire()
    
    while(not script_end):
        val = raw_input()
        client_socket.send(str(val))
        

def main():
    global script_end
    send_thread = Thread(target=send)
    recv_thread = Thread(target=recv)
    
    send_thread.daemon = True
    recv_thread.daemon = True
    
    send_thread.start()
    recv_thread.start()
    
    while (not script_end):
        pass
    
if __name__ == "__main__":
    main()