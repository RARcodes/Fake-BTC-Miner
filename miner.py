from colorama import Fore, Style, init
import secrets
from random import randint
import threading

init()

btcval = 14404.41

print(Fore.YELLOW + "Mining in progress...")

num_btc = 0
total_btc = 0
wallet_address = ""

def mine():
    global num_btc, total_btc
    while True:
        ranInt = randint(0, 2500)
        if ranInt <= 1:
            randomBTC = randint(1, 100) / 100
            print(Fore.WHITE + "> 0x" + secrets.token_hex(20) + Fore.GREEN + " >: " + str(randomBTC) + " BTC (" + Style.BRIGHT + "$" + str(
                "{:,}".format(round(btcval * randomBTC, 2))) + ")" + Style.RESET_ALL)
            num_btc += 1
            total_btc += randomBTC
        else:
            print(Fore.WHITE + "> 0x" + secrets.token_hex(20) + Fore.RED + " > 0.00 BTC (" + Style.BRIGHT + "$0.00" + Style.RESET_ALL + ")")

        if num_btc >= 100:
            break

t1 = threading.Thread(target=mine)
t1.start()

while True:
    if num_btc >= 100:
        t1.join()
        wallet_address = input("Enter your wallet address to deposit the mined cryptocurrency: ")
        break

print(Fore.GREEN + f"\nMining complete! You have mined a total of {total_btc:.2f} BTC ({Style.BRIGHT}${'{:,.2f}'.format(round(btcval*total_btc, 2))})\n")
print(Fore.YELLOW + f"Depositing {total_btc:.2f} BTC to wallet address {wallet_address}...")
