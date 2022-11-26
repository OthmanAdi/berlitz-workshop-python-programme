from socket import *

IPAdresses = [
    "127.01.20.5",
    "60.1.5.20",
]

print(IPAdresses[0])

target0 = "linkedin.com"
target1 = "6-wochen-startup.de"

print(gethostbyname(
    target0))  # hier wird mithelfe von gethostbyname die IP von die targets die definiert worden ausgedrückt
print("\n")
print(gethostbyname(target1))
print("\n")
print(gethostname())
PLZDONTHACKME = gethostname()
print(gethostbyname(PLZDONTHACKME))
