import logging
from functools import partial

from aiokit import MultiprocessAsyncExecutor
from izihawa_utils.env import node_name
from izihawa_utils.importlib import (
    import_object,
    instantiate_object,
)
from library.logging import configure_logging
from nexus.pipe.configs import config


def create_aiothing(consumer_cls, topic_names, group_id, processors, shard):
    processors = [instantiate_object(processor) for processor in processors]
    return consumer_cls(
        topic_names=topic_names,
        processors=processors,
        bootstrap_servers=config['pipe']['bootstrap_servers'],
        group_id=group_id,
    )


def main():
    configure_logging(config)

    logger = logging.getLogger('statbox')
    logger.info({
        'action': 'started',
        'mode': 'startup',
    })

    create_aiothings = []
    for instance_config in config['pipe']['schema']:
        node_names = instance_config.get('node_names', [])
        if node_names and node_name not in node_names:
            continue
        for consumer_config in instance_config['consumers']:
            consumer_cls = import_object(consumer_config['class'])
            for topic_config in consumer_config['topics']:
                for _ in range(topic_config['workers']):
                    create_aiothings.append(partial(
                        create_aiothing,
                        consumer_cls,
                        topic_config['name'],
                        instance_config['group_id'],
                        instance_config['processors'],
                    ))

    executor = MultiprocessAsyncExecutor(create_aiothings=create_aiothings)
    executor.start()
    executor.join()


if __name__ == '__main__':
    main()
