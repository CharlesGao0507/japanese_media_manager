from pathlib import Path

from jmm.utilities.file_information import FileInformation

def test_get_file_paths(file_paths):
    file_informations = list(map(FileInformation, map(Path, file_paths)))

    assert not file_informations[0].has_chinese_subtitle
    assert not file_informations[1].has_chinese_subtitle
    assert file_informations[0].number == 'STAR-325'
    assert file_informations[1].number == 'SSNI-306'

    assert file_informations[0].next is None
    assert file_informations[5].next is not None
    assert file_informations[5].next.next is not None
    assert file_informations[5].next.next.next is None

def test_singleton():
    file_information_1 = FileInformation(Path('./test'))
    file_information_2 = FileInformation(Path('test'))
    file_information_3 = FileInformation(Path('test').absolute())

    assert file_information_1 is file_information_2
    assert file_information_1 is file_information_3
