
import os


y = input("hit y to hibernate ")
if y == "y":
    os.system(r'rundll32.exe powrprof.dll,SetSuspendState Hibernate')