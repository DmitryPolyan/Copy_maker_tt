import xml.etree.ElementTree as ET
import shutil
import os
import typing
import logging
from sys import argv


def parser_xml(conf_name: str) -> typing.List[typing.Dict[str, str]]:
    """
    Parsing of configuration XML file
    :param conf_name: name of configuration XML file
    :return: list with params of copies
    """
    logging.info("Start of parsing")
    all_configs = []
    tree = ET.parse(conf_name)
    root = tree.getroot()
    for child in root:
        all_configs.append(child.attrib)
    return all_configs


def copy_maker(source: str, file_name: str, destination: str) -> None:
    """
    Copy file from source to destination
    :param source: source path
    :param file_name: file for copy
    :param destination: destination copy
    :return:
    """
    shutil.copy2(source+file_name, destination)
    logging.info(f"{file_name} copied ")


def validation(source: str, file_name: str, destination: str) -> bool:
    """
    Checking for the existence of a source, file, and destination
    :param source: source path
    :param file_name: file for copy
    :param destination: destination copy
    :return:
    """
    if not os.path.exists(source):
        logging.error("Source does not exist")
        return False
    if not os.path.isfile(source+file_name):
        logging.error("File does not exist")
        return False
    if not os.path.exists(destination):
        logging.error("Destination does not exist")
        return False
    return True


def main():
    logging.basicConfig(filename="logs/logs.log", level=logging.INFO)
    conf_name = argv[1]
    for conf in parser_xml(conf_name):
        if validation(conf['source_path'], conf['file_name'], conf['destination_path']):
            copy_maker(conf['source_path'], conf['file_name'], conf['destination_path'])
        else:
            break
    logging.info("Copy completed ")


if '__name__' != '__main__':
    main()

