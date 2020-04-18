import multiprocessing
from pathlib import Path
import time


PROJECT_DIR = "../Example"


def count_line(file_name):
    with open(file_name, 'r') as file_:
        lines = file_.read().splitlines()
        return len(lines)


def count_all_lines(all_files):
    with multiprocessing.Pool() as pool:
        pool_output = pool.map(count_line, all_files)
        return pool_output


if __name__ == '__main__':
    p = Path(PROJECT_DIR)
    files = list(p.glob('**/*.json'))

    single_start = time.time()
    lines = []
    for file_ in files:
        line = count_line(file_)
        lines.append(line)
    single_duration = time.time() - single_start

    print("Single process => {}, time => {}".format(lines, single_duration))

    start = time.time()
    all_lines = count_all_lines(Path(PROJECT_DIR).rglob('*.json'))
    duration = time.time() - start
    print("Multi process => {}, time => {}".format(all_lines, duration))

