import pygatt
from binascii import hexlify

adapter = pygatt.GATTToolBackend()

def handle_data(handle, value):
    """
    handle -- integer, characteristic read handle the data was received on
    value -- bytearray, the data returned in the notification
    """
    print("Received data: %s" % hexlify(value))

try:
    adapter.start()
    device = adapter.connect('01:23:45:67:89:ab')

    device.subscribe("a1e8f5b1-696b-4e4c-87c6-69dfe0b0093b",
                     callback=handle_data)
finally:
    adapter.stop()