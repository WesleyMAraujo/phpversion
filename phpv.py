#!/usr/bin/env python3

import subprocess
import sys

def set_php_version(version):
    try:
        subprocess.run(['sudo', 'update-alternatives', '--set', 'php', f'/usr/bin/php{version}'], check=True)
        print(f'Successfully set PHP version to {version}')
    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].replace('.', '').isdigit():
        set_php_version(sys.argv[1])
    else:
        print('Usage: sudo ./phpversion.py <version>')
        sys.exit(1)
