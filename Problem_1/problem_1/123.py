import os
from pathlib import Path

print(os.path.isfile('/etc/boot.log'))

os.remove("/etc/boot.log")

print(os.path.isfile('/etc/boot.log'))


