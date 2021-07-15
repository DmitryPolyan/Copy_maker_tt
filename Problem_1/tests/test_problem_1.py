import problem_1.copy_maker as cm
import os
from unittest import mock
import platform


def test_parser_xml():
    result = next(cm.parser_xml('tests/config.xml'))
    assert isinstance(result, dict)
    assert len(result) == 3
    assert {'source_path': '/var/log', 'destination_path': '/etc', 'file_name': 'boot.log'} == result


def test_validation():
    if platform.system() == "Linux":
        assert cm.validation('/var/log', 'boot.log', '/etc') is True
        assert cm.validation('/var/xlogx', 'boot.log', '/etc') == os.path.exists('/var/xlogx/')
        assert cm.validation('/var/log', 'boot.log', '/1etc1') == os.path.exists('/1etc1')
        assert cm.validation('/var/log', 'boot.log123', '/etc') == os.path.isfile('/var/log' + 'boot.log123')

    elif platform.system() == "Windows":
        assert cm.validation(r"C:\Windows\system32", "kernel32.dll", r"C:\Program files") is True
        assert cm.validation(r"C:\Windows\system42", "kernel32.dll", r"C:\Program files") == os.path.exists(
            r"C:\Windows\system42")
        assert cm.validation(r"C:\Windows\system32", "kernel32.dll", r"C:\Program1 files") == os.path.exists(
            r"C:\Program1 files")
        assert cm.validation(r"C:\Windows\system32", "kernel52.dll", r"C:\Program files") == os.path.isfile(
            r"C:\Windows\system32" + "kernel52.dll")


def test_main(preparing_and_cleaning):
    all_work = [i for i in cm.parser_xml('tests/test_config.xml')]
    for i in all_work:
        assert os.path.isfile(i['destination_path'] + "/" + i['file_name']) is False
    with mock.patch("problem_1.copy_maker.get_config_file", return_value='tests/test_config.xml'):
        cm.main()
    for i in all_work:
        assert os.path.isfile(i['destination_path'] + "/" + i['file_name']) is True
