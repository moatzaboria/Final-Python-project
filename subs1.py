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
            elif promtcomnd[0] == "key1":
                print(key1)
            elif promtcomnd[0] == "key2":
                print(key2)

