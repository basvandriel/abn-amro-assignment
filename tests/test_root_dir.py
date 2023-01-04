from pathlib import Path
from abn_assignment import constants


def test_root_dir():
    path = constants.ROOT_DIR
    assert isinstance(path, Path)


def test_data_dir():
    path = constants.DATA_DIR
    assert isinstance(path, Path)
