from library.jobber import job_cli
from nexus.ingest.configs import get_config

if __name__ == '__main__':
    config = get_config()
    job_cli(config)
