import argparse
import os
import shutil
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))

def _get_cookie_headers() -> dict[str, str]:
    with open(os.path.join(HERE, '../.env')) as f:
        contents = f.read().strip()
    return {'Cookie': contents}


def get_input(year: int, day: int) -> str:
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    req = urllib.request.Request(url, headers=_get_cookie_headers())
    return urllib.request.urlopen(req).read().decode()


def download_input(year: int, day: int, dest: str) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('year', type=int)
    parser.add_argument('day', type=int)
    args = parser.parse_args()

    for i in range(5):
        try:
            s = get_input(year, day)
        except urllib.error.URLError as e:
            print(f'zzz: not ready yet: {e}')
            time.sleep(1)
        else:
            break
    else:
        raise SystemExit('timed out after attempting many times')

    with open(f'{dest}/input.txt', 'w') as f:
        f.write(s)
    os.chmod('input.txt', 0o400)

    lines = s.splitlines()
    if len(lines) > 10:
        for line in lines[:10]:
            print(line)
        print('...')
    else:
        print(lines[0][:80])
        print('...')

    return 0

def init_folder():
    parser = argparse.ArgumentParser()
    parser.add_argument('year', type=int)
    parser.add_argument('day', type=int)
    args = parser.parse_args()

    source_folder = 'utils/day00'
    destination_folder = f'aoc{args.year}/day{args.day}'

    if os.path.exists(source_folder):
        shutil.copytree(source_folder, destination_folder)
        print(f"Folder '{source_folder}' copied to '{destination_folder}'")
        print('Fetching puzzle input')
        download_input(year=args.year, day=args.day, dest=destination_folder)
    else:
        print(f"Source folder '{source_folder}' does not exist.")

    return 0
