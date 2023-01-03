def main():
    key1 ,key2 = "",""
    while True:
        new_cmd = input('prompt>')
        if new_cmd == "done":
            break
        elif new_cmd != "":
            promtcomnd = new_cmd.split(' ')
            if promtcomnd[0] == "newkey":
                print("Enter key1:")
                key1 = input('key1>')
                print("Enter key2:")
                key2 = input('key2>')
            elif promtcomnd[0] == "load":
                key1 ,key2 = load_key_file(promtcomnd[1])
            elif promtcomnd[0] == "save":
                save_key_file(promtcomnd[1], key1, key2)
            elif promtcomnd[0] == "info":
                printall(promtcomnd[0], key1, key2)
            elif promtcomnd[0] == "enc":
                encryption_file(promtcomnd[1], promtcomnd[2], key1, key2)
            elif promtcomnd[0] == "dec":
                decryption_file(promtcomnd[2], promtcomnd[1], key1, key2)
            elif promtcomnd[0] == "key1":
                print(key1)
            elif promtcomnd[0] == "key2":
                print(key2)

def encryption_file(file, encfile, key1, key2):
    f= open(file , 'r')
    lines =f.readlines()
    temp=""
    for x in str(lines):
        if key1.find(x) != -1:
            temp+=key2[key1.find(x)]
        else:
            temp+=x
    print(temp)
    f=open(encfile,'w')
    f.write(temp)

def decryption_file(decfile,encfile, key1, key2):
    f= open(encfile , 'r')
    lines =f.readlines()
    temp=""
    for x in str(lines):
        if key2.find(x) != -1:
            temp += key1[key2.find(x)]
        else:
            temp += x
    print(temp)
    f=open(decfile,'w')
    f.write(temp)

def save_key_file(filename,key1,key2):
    f=open(filename,'w')
    f.write(key1)
    f.write('\n')
    f.write(key2)

def load_key_file(filename):
        f = open(filename, 'r')
        Lines = f.readlines()
        k1=Lines[0]
        k2=Lines[1]
        return k1,k2

def printall(filename,key1,key2):

    print('key:'+filename)
    print('clear:\n' + key1)
    print('key:\n' + key2)

main()