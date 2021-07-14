import problem_1.copy_maker as cm
import os
from unittest import mock


def test_parser_xml():
    result = next(cm.parser_xml('tests/config.xml'))
    assert isinstance(result, dict)
    assert len(result) == 3
    assert {'source_path': '/var/log/', 'destination_path': '/etc', 'file_name': 'boot.log'} == result


def test_validation():
    assert cm.validation('/var/log/', 'boot.log', '/etc') is True
    assert cm.validation('/var/xlogx/', 'boot.log', '/etc') == os.path.exists('/var/xlogx/')
    assert cm.validation('/var/log/', 'boot.log', '/1etc1') == os.path.exists('/1etc1')
    source = '/var/log/'
    file_name = 'boot.log123'
    assert cm.validation(source, file_name, '/etc') == os.path.isfile(source+file_name)


def test_main(preparing_and_cleaning):
    assert os.path.isfile('/etc/boot.log') is False
    with mock.patch("sys.argv", return_value=[None, 'tests/config.xml']):
        cm.main()
