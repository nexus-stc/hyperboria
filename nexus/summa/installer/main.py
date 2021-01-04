import time

import fire
from nexus.summa.installer.scripts.import_to_summa import import_to_summa
from nexus.summa.installer.scripts.iterate import iterate

if __name__ == '__main__':
    start = time.time()
    fire.Fire({
        'import-to-summa': import_to_summa,
        'iterate': iterate,
    })
    print(f'Elapsed {time.time() - start:.2f} secs')
