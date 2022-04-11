from time import sleep

f = open("./test1.txt", "a+")
while True:
    f.write("222222\n")
    print("written")
    sleep(2)
