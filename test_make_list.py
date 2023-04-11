import os
import pytest

from make_link import create_symlink


@pytest.fixture
def config_files():
    """Return a dictionary of test config files"""
    return {
        'test_config_1': 'test_link_1',
        'test_config_2': 'test_link_2',
    }


@pytest.fixture(autouse=True)
def cleanup(config_files):
    """Cleanup any created test links after each test"""
    yield
    for link_file in config_files.values():
        if os.path.exists(link_file):
            os.remove(link_file)


def test_create_symlink_success(config_files):
    """Test that create_symlink creates a symlink successfully"""
    config_file = 'test_config_1'
    link_file = config_files[config_file]
    create_symlink(config_file, link_file)
    assert os.path.islink(link_file)


def test_create_symlink_failure(config_files):
    """Test that create_symlink returns False when symlink creation fails"""
    # Create a dummy file to occupy the link file path
    open('test_link_1', 'w').close()
    config_file = 'test_config_1'
    link_file = config_files[config_file]
    with pytest.raises(OSError):
        create_symlink(config_file, link_file)
    assert not os.path.islink(link_file)
