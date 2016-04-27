import serial,time

def Sending(message,sender):
    ser=serial.Serial("COM12",9600)
    start_cmd='AT+CMGF=1\r'
    start_byte=start_cmd.encode('utf-8')

    num_cmd='AT+CMGS="'+sender+'"\r\n'
    num_byte=num_cmd.encode('utf-8')

    msg_cmd=message+"\x1A"
    msg_byte=msg_cmd.encode('utf-8')

    
    ser.write(start_byte)
    time.sleep(1)
    #ser.write('AT+CMGS="'+sender+'"\r\n')
    ser.write(num_byte)

    time.sleep(1)
    
    #ser.write(message+"x1A")
    ser.write(msg_byte)
    time.sleep(1)
    print("Message Sent")


x=input("Type the Number:\n")
y=input("Type the Message:\n")

Sending(y,x)
