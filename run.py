import sys,serial
import serial.tools.list_ports
from time import sleep

MySerial = "COM5"             # Открытый последовательный порт
MyBPS = 4800
Mytimeout = 1

def  open_port(port, bps, timex):
    try:
        ser = serial.Serial()
        ser.baudrate = bps
        ser.port = port
        ser._timeout = timex
        ser.open()

        if ser.is_open:
            print("--- последовательный порт открыт ---")
            return ser

    except Exception as e:
        print("--- Открытие порта: исключение ---:", e)
        return 0

def send_to_port(ser, text):
    try:
        ser.write(b"\r\n") 
        read_from_port(ser)

        text = text + "\r\n"
        result = ser.write(text.encode())       
        if result == len(text):
            print(f"==> {text}")
            return result
        else:
            print("--- Ошибка отправки ---:", "data len:", len(text), "send len:", result)
            return 0
    except Exception as e:
        print("--- Отправка данных: неуспешно ---:", e)

def  read_from_port(ser):
    answer = ser.readlines()  #Read from Serial Port
    result = ""
    for s in answer:
        result = result + s.decode()
    return result    


def  close_port(ser):
    if ser.is_open:
        try:
            ser.close()
            print("--- Последовательный порт закрыт ---")
            return 0
        except Exception as e:
            print("--- Закрытие порта исключение ---:", e)
            return -1
    else:
        print("--- Ошибка ---: последовательный порт закрыт!")
        return -1

if __name__ == "__main__":
    ser = open_port(MySerial, MyBPS, Mytimeout)
    if ser is None:
        print("--- Ошибка открытия последовательного порта---")
        sys.exit()

    # line_time_old = None
    # with open('cambrils.txt', 'r') as f:
    #     for line in f:
    #         # line = line.split("]")
    #         line_time = 60*60*1000*int(line[1:3]) + 60*1000*int(line[4:6]) + 1000*int(line[7:9]) + int(line[10:13]) #часы
    #         if line_time_old is None:
    #             line_time_old = line_time
    #         cmd = line.split("]")[1].replace("\n", "").replace("\r", "")
    #         # sleep((line_time - line_time_old)/1000)

    #         send_to_port(ser, cmd) 
    #         answer = read_from_port(ser)
    #         print(answer)

    #         line_time_old = line_time

  
    # send_to_port(ser, "$GNRMC,165456.517,A,4103.7095,N,00101.5054,E,2.08,0.00,250621,,,A*77") 
    # answer = read_from_port(ser)
    # print(answer)

    send_to_port(ser, "AT$LED=1") 
    answer = read_from_port(ser)
    print(answer)

    send_to_port(ser, "AT$TIM=0") 
    answer = read_from_port(ser)
    print(answer)

    send_to_port(ser, "AT$SB=1") 
    answer = read_from_port(ser)
    print(answer)

    close_port(ser)
    



