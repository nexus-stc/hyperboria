import time

import fire
from nexus.cognitron.installer.scripts.iterate import iterate

if __name__ == '__main__':
    start = time.time()
    fire.Fire({
        'iterate': iterate,
    })
    print(f'Elapsed {time.time() - start:.2f} secs')
