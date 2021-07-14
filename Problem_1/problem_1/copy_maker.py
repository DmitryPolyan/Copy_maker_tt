import xml.etree.ElementTree as ET
import shutil
import os
import typing
import logging
import sys
import argparse


def get_config_file() -> str:
    """
    Getting the name of the configuration file from the command line.
    :return: file name
    """
    def check_file(file_name: str) -> str:
        """Checking a file for availability and support """
        if not os.path.isfile(file_name):
            raise argparse.ArgumentTypeError("File does not exist")
        elif file_name[-4:] != ".xml":
            raise argparse.ArgumentTypeError("Unsupported file format ")
        return file_name

    parser = argparse.ArgumentParser(
        description="The utility copies files according to the provided configuration file.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("configuration", type=check_file, help="configuration file (XML)")
    args = parser.parse_args()
    return args.configuration


def parser_xml(conf_name: str) -> typing.List[typing.Dict[str, str]]:
    """
    Parsing of configuration XML file
    :param conf_name: name of configuration XML file
    :return: list with params of copies
    """
    # logging.info("Start of parsing")
    tree = ET.parse(conf_name)
    root = tree.getroot()
    for child in root:
        yield child.attrib


def copy_maker(source: str, file_name: str, destination: str) -> None:
    """
    Copy file from source to destination
    :param source: source path
    :param file_name: file for copy
    :param destination: destination copy
    :return: None
    """
    shutil.copy2(source+file_name, destination)
    logging.info(f"{file_name} copied")


def validation(source: str, file_name: str, destination: str) -> bool:
    """
    Checking for the existence of a source, file, and destination
    :param source: source path
    :param file_name: file for copy
    :param destination: destination copy
    :return: bool
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
    logging.basicConfig(filename="logs/logs.log", format='%(asctime)s - %(message)s', level=logging.INFO)
    for conf in parser_xml(get_config_file()):
        if validation(conf['source_path'], conf['file_name'], conf['destination_path']):
            copy_maker(conf['source_path'], conf['file_name'], conf['destination_path'])
    logging.info("End of work")


if __name__ == '__main__':
    main()

