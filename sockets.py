from socket import *
def conScan(ho,po):
    try:
        con= socket(AF_INET,SOCK_STREAM)
        con.connect((ho,po))
        print("done")
        con.close()
    except:
        print("nah")

conScan('31.13.79.35',22)