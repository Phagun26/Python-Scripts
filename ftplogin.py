import ftplib

def func(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        print("gg")
    except:
        print("chi")

func('90.130.70.73')