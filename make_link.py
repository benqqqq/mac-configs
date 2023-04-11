import os

from link_settings import CONFIG_FILES


def get_expand_config_files():
    """
    Return a dictionary of config files with expanded paths.
    """
    return {expand_path(config_file): expand_path(link_file) for config_file, link_file in CONFIG_FILES.items()}


def expand_path(path):
    """
    Expand a path and return the absolute path.
    """
    return os.path.abspath(os.path.expanduser(path))


def create_symlink(config_file, link_file):
    """
    Create a symlink from config_file to link_file.
    """
    os.symlink(config_file, link_file)
    print(f"Created symlink from {config_file} to {link_file}")


def main():
    """
    Create symlinks for all config files in CONFIG_FILES.
    """
    config_files = get_expand_config_files()
    existing_files = [link_file for link_file in config_files.values() if os.path.lexists(link_file)]
    new_files = list(set(config_files.values()) - set(existing_files))

    if new_files:
        new_files_repr = '\n'.join(new_files)
        print(f"Creating new symlinks for:\n {new_files_repr}\n")

    if existing_files:
        existing_files_repr = '\n'.join(existing_files)
        print(f"Overwrite Existing files:\n {existing_files_repr}\n")

    to_continue = input(f'Continue? (y/n): ')
    if to_continue.lower() == 'y':
        for existing_file in existing_files:
            os.remove(existing_file)

        for config_file, link_file in config_files.items():
            create_symlink(config_file, link_file)
    else:
        print("Aborting...")


if __name__ == '__main__':
    main()
