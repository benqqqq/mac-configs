import os


_CONFIG_FILES = {
    './configs/kitty.conf': '~/.config/kitty/kitty.conf',
    './configs/nvimrc': '~/.nvmrc',
    './configs/zshrc': '~/.zshrc',
    './configs/pypoetry_config.toml': '~/.config/pypoetry/config.toml',
}


def get_expand_config_files():
    """Return a dictionary of config files with expanded paths"""
    return {expand_path(config_file): expand_path(link_file) for config_file, link_file in _CONFIG_FILES.items()}


def expand_path(path):
    """Expand a path and return the absolute path"""
    return os.path.abspath(os.path.expanduser(path))


def create_symlink(config_file, link_file):
    """Create a symlink from config_file to link_file"""
    os.symlink(config_file, link_file)
    print(f"Created symlink from {config_file} to {link_file}")


def main():
    """Create symlinks for all config files in CONFIG_FILES"""
    for config_file, link_file in get_expand_config_files().items():
        if os.path.exists(link_file) or os.path.islink(link_file):
            overwrite = input(f"{link_file} exists. Overwrite? (y/n): ")
            if overwrite.lower() == 'y':
                os.remove(link_file)
                create_symlink(config_file, link_file)
            else:
                print(f"Skipping {link_file}")
        else:
            create_symlink(config_file, link_file)


if __name__ == '__main__':
    main()
