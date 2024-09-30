#Project_overview
#1. Prompt user to enter "Host name or IP gateway to scan"
#2. Port to be scan 1 - 1025
#3. Open port should be write to a file
#4. Any expection must be handle and write to the file
#5. Record starting date and ending date, write to the file and total time of scanned

#Import built in library/modules i.e socket and datetime
import socket
import datetime

#Create a function name 'verifiedPorts' to check given host and port using socket library
def verifiedPorts(userInput, port):
    scan=socket.socket()
    try:
        scan.connect((userInput, port))
    except:
        return False
    else:
        return True

#Output the status of all scanned ports to a file
writeFile = open("outputFile", "w")

#Prompt user to enter host name, IP Address or default gateway
userInput = input("Please enter host IP Address: ")

#Used 'datetime' libary and method to get current time
startTime = datetime.datetime.now()

#Socket library to confirmed if scanned host IP address is valid
scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Validate if input IP is valid or invalid
try:
    inputHostIP = socket.gethostbyname(userInput)
    print("Hooray, your host IP address is valid to be scanned!")
except:
    print("Opps, Program terminated, please try again with valid Host IP address")
    writeFile.write(f"User entered {userInput} was not valid!")
    exit()

#Verified if host IP address entered is valid to be scanned
try:
    scan.connect((userInput, 4)) #Port 4 is unassigned port
    print("Opps, Host IP entered is unavailable!")

#Handle expection error and print as output
except socket.error as errorIsScanned:
    output = str(errorIsScanned)
scan.close() #close isScan validation

#Checking based on specific error code i.e WinError 10061 - target IP refuse to connect
if(output.startswith("[WinError 10061")):
    print(f"Host is available, scanned begins at {startTime} \n")
    writeFile.write(f"{inputHostIP} is available, scanned begins at {startTime} \n")
else:
    print("Opps, we encounter problem scanning host IP address! aborting scan")
    writeFile.write(f"Host IP address {inputHostIP} unreachable! Aborted scan")
    writeFile.close() #close connection
    exit() #exit or quit

#Use for loop to verify open ports between 1-1025 range
for portRange in range(50, 55):
    if (verifiedPorts(userInput, portRange)):
        print("Port number ", {portRange}, " is open \n")
        writeFile.write(f"Port {portRange} is open \n")

#Informed user if the task is completed
print("Host IP scanned has been completed! ")

#Ending program, record endTime and Total, write to files
endTime = datetime.datetime.now()
print("Host IP scanned ends at: ", endTime)
print("Total scanned time: ", endTime-startTime , "seconds.")
writeFile.write(f"Scanned ends at: {endTime} \n")
writeFile.write((f"Total scanned time: {endTime-startTime}, seconds"))
writeFile.close() #close connection