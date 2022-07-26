from time import time, sleep
import pigpio

pi = pigpio.pi()


HANDLE = pi.spi_open(0, 40000)
SS = 8  # Pin du SS sur la Pi

# Disable Slave Select
pi.write(SS, 1)


def transfer_and_wait(what):
    global HANDLE

    a = str(what).encode()
    print("envoi", a, type(a))

    n, b = pi.spi_xfer(HANDLE, a)
    print("reçu:", b)

    sleep(0.002)  # (0.000002)  # 20 microsecond
    return b

def main():
    """
    byte a, b, c, d

    """
    global HANDLE
    global SS

    # enable Slave Select
    pi.write(SS, 0)

    ################################ Test de addition
    print("\n\nTest d'addition:")
    # Envoi de la commande 'add'
    transfer_and_wait('a')

    # Envoi de la valeur 10
    transfer_and_wait(10)

    a = transfer_and_wait(17)
    b = transfer_and_wait(33)
    c = transfer_and_wait(42)
    d = transfer_and_wait(0)

    # disable Slave Select
    pi.write(SS, 1)

    print("Résultats des additions:");
    for item in [a, b, c, d]:
        print("item", item, "type:", type(item))

    # enable Slave Select
    pi.write(SS, 0)

    ################################ Test de soustraction
    print("\n\nTest de soustraction:")
    # Envoi de la commande 'add'
    transfer_and_wait('s')

    # Envoi de la valeur 10
    transfer_and_wait(10)

    a = transfer_and_wait(17)
    b = transfer_and_wait(33)
    c = transfer_and_wait(42)
    d = transfer_and_wait(0)

    # disable Slave Select
    pi.write(SS, 1)

    print("Résultats des soustractions:");
    for item in [a, b, c, d]:
        print("item", item, "type:", type(item))

    sleep(1)


main()

pi.spi_close(HANDLE)
pi.stop()
