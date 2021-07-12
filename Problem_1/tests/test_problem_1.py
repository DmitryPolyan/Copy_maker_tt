import problem_1.copy_maker as cm


def test_parser_xml():
    result = cm.parser_xml('tests/config.xml')
    assert isinstance(result, dict)
