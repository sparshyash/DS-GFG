import random,os,time
print('\033[?25l',end="")
for i in range(1,101):
    print(i)
time.sleep(0.2)
os.system("clear")
print("\033[?25h",end="")