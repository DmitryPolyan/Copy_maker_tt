import pytest
import platform
import os


@pytest.fixture(autouse=True, scope='session')
def preparing_and_cleaning():
    if platform.system() == "Linux":
        if os.path.isfile('/etc/boot.log'):
            os.remove("/etc/boot.log")
    else:
        if os.path.isfile(r'C:\Program files\kernel32.dll'):
            os.remove(r"C:\Program files\kernel32.dll")
    yield
    if platform.system() == "Linux":
        if os.path.isfile('/etc/boot.log'):
            os.remove("/etc/boot.log")
    else:
        if os.path.isfile(r'C:\Program files\kernel32.dll'):
            os.remove(r"C:\Program files\kernel32.dll")
