import fire
from aiokit.utils import sync_fu
from izihawa_utils.importlib import import_object
from library.logging import (
    configure_logging,
    error_log,
)
from nexus.ingest.configs import get_config


async def run_job(name, **kwargs):
    config = get_config()
    configure_logging(config)

    job_config = config['jobs'][name]
    job_class = import_object(job_config['class'])
    real_kwargs = job_config['kwargs'].copy()
    real_kwargs.update(kwargs)
    job = job_class(**real_kwargs)

    try:
        await job.start_and_wait()
    except Exception as e:
        error_log(e)
        raise
    finally:
        await job.stop()


def main():
    fire.Fire({'run-job': sync_fu(run_job)})


if __name__ == '__main__':
    main()
