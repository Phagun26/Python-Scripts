import zipfile

def third():
    zfile = zipfile.ZipFile('passw.zip')
    passfile = open('passw.txt')
    for line in passfile.readline():
        password = line.strip('\n')
        guess = extract(zfile, password)
        if guess:
            print(password)


def extract(zfile,password):
    try:
        zfile.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        print('wrong pass')
        return
