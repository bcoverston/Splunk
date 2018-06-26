import sys

from builtins import print

__author__ = 'eMaM'


def main():
    settings_param = sys.argv[1]
    settings_profile = sys.argv[2]
    if settings_param == '--settings':
        if settings_profile.lower() == 'develop':
            pass


if __name__ == '__main__':
    main()
