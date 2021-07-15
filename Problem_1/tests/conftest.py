import xml.etree.ElementTree as ET
import pytest
import os
import random
import shutil


def generation_xml(test_folders: list) -> None:
    """
    Generation of configuration file for testing.
    Create temp XML config file in folder "tests"
    :param test_folders: list of temp folders
    """
    top = ET.Element('config')
    work_dir = os.path.abspath(os.curdir)+'/'
    for i in range(int(len(test_folders)/2)):
        child = ET.SubElement(top, 'file')
        child.attrib = {'source_path': work_dir + test_folders[i],
                        "destination_path": work_dir + test_folders[i+3],
                        "file_name": f"{i}.txt"}
    my_data = ET.tostring(top)
    with open('tests/test_config.xml', "wb") as f:
        f.write(my_data)


@pytest.fixture
def preparing_and_cleaning():
    folder_numbers = list(range(100))
    random.shuffle(folder_numbers)
    # Create folders for testing
    temp_folder = f"tests/place_for_testing{folder_numbers[-1]}/"
    os.mkdir(temp_folder)
    test_folders = [temp_folder + str(folder_numbers[i]) for i in range(6)]
    for folder in test_folders:
        os.mkdir(folder)
    # Create files for testing
    for i in range(int(len(test_folders)/2)):
        with open(f"{test_folders[i]}/{i}.txt", "wb") as f:
            f.write(os.urandom(random.randint(5000, 2000000)))
    generation_xml(test_folders)
    yield
    os.remove('tests/test_config.xml')
    shutil.rmtree(temp_folder)
