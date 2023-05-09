"""
Script to test .gitlab-ci.yml's syntax & it's contents.
"""

from yaml import load, Loader

def read_yaml(filepath: str) -> dict:
    with open(filepath, 'r') as f:
        return load(f, Loader=Loader)

if __name__ == '__main__':
    gitlab_ci_config = read_yaml('.gitlab-ci.yml')
    # print keys & their values
    print()
    for key, value in gitlab_ci_config.items():
        print(key + ':')
        print(value)
        print()
        print()
