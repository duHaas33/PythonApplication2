import sys
import logging
from PySide6.QtCore import QCoreApplication
from PySide6.QtBluetooth import QBluetoothDeviceDiscoveryAgent, QBluetoothDeviceInfo
from src.bluetooth.r10_device import R10Device

TARGET_DEVICE_ADDRESS = "F7:B2:2A:CA:AB:67"  # Replace with your actual device address

logging.basicConfig(
            format="%(asctime)s,%(msecs)-3d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
            datefmt="%Y-%m-%d:%H:%M:%S",
            level=logging.DEBUG,
            filename=r'c:\temp\bluetoothLog.txt',
            encoding='utf-8',
            force=True
        )

def device_discovered(device: QBluetoothDeviceInfo, r10_device: R10Device):
    if device.address().toString() == TARGET_DEVICE_ADDRESS:
        logging.info(f"Found target device: {device.name()}")
        r10_device._ble_device = device
        r10_device.connect_device()
        agent.stop()

def discovery_finished():
    logging.info("Device discovery finished.")

def main():
    app = QCoreApplication(sys.argv)
    global agent

    # Create the Bluetooth device instance
    r10_device = R10Device(None)

    # Set up the device discovery agent
    agent = QBluetoothDeviceDiscoveryAgent()
    agent.deviceDiscovered.connect(lambda device: device_discovered(device, r10_device))
    agent.finished.connect(discovery_finished)
    agent.start()

    # Start the event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
