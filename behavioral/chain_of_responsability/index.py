from __future__ import annotations
from abc import abstractmethod, ABC

"""
consider an app to simulate musical instruments.
Before playing a sample it should check:
  1. if the user has permission to access the sample;
  2. if the sample is cached or should be fetched from the database;
  3. if the sample can be downloaded.
"""


# Helper - not part of the pattern
class PlaySampleRequest:
    def __init__(self, sample_id: str, sample_type: str, user_plan: str):
        self.sample_id = sample_id
        self.sample_type = sample_type
        self.user_plan = user_plan


# Handler
class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> str:
        pass

    @abstractmethod
    def handle(self, request) -> str:
        pass


# Handler
class PlaySampleHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: PlaySampleRequest) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return True


# Concrete Handlers
class SampleAccessHandler(PlaySampleHandler):
    def handle(self, request: PlaySampleRequest) -> str:
        if request.sample_type == 'free' or request.user_plan == 'premium':
            print('AccessHandler: Access granted to sample '
                  f'{request.sample_id}')
            return super().handle(request)

        print(f'AccessHandler: Access denied to sample {request.sample_id}')
        return None


class FetchSampleHandler(PlaySampleHandler):
    _sample_cache = ['sample1', 'sample3']

    def handle(self, request: PlaySampleRequest) -> str:
        if request.sample_id in self._sample_cache:
            print(f'FetchHandler: Sample {request.sample_id} fetched '
                  'from cache')
            return super().handle(request)

        print(f'FetchHandler: Sample {request.sample_id} fetched '
              f'from database')
        self._sample_cache.append(request.sample_id)
        return super().handle(request)


class SampleExportHandler(PlaySampleHandler):
    exportable_samples = ['sample2', 'sample4']

    def handle(self, request: PlaySampleRequest) -> str:
        if request.sample_id in self.exportable_samples:
            print(f'ExportHandler: Sample {request.sample_id} can be exported')

        print(f'ExportHandler: Sample {request.sample_id} cannot be exported')
        return super().handle(request)


# Client code
def play_sample(handler: Handler, request: PlaySampleRequest) -> None:
    print(f'Requesting to play sample {request.sample_id}')

    request = PlaySampleRequest(**request_example)
    result = handler.handle(request)
    if result:
        print(f'♪ Playing sample {request.sample_id}')
    else:
        print(f'✖ Cannot play sample {request.sample_id}')


if __name__ == '__main__':
    request_examples = [
        {
            'sample_id': 'sample1',
            'sample_type': 'free',
            'user_plan': 'free'
        },
        {
            'sample_id': 'sample2',
            'sample_type': 'free',
            'user_plan': 'premium'
        },
        {
            'sample_id': 'sample3',
            'sample_type': 'premium',
            'user_plan': 'free'
        },
        {
            'sample_id': 'sample4',
            'sample_type': 'premium',
            'user_plan': 'premium'
        }
    ]

    access_handler = SampleAccessHandler()
    fetch_handler = FetchSampleHandler()
    export_handler = SampleExportHandler()

    access_handler.set_next(fetch_handler).set_next(export_handler)

    for request_example in request_examples:
        print()
        play_sample(
            access_handler,
            request=PlaySampleRequest(**request_example))
