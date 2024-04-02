from abc import abstractmethod, ABC

"""
consider an app to simulate musical instruments.
It has a big list of instruments and each instruments
has dozen of audio sample files, which are stored on a database.
Accessing that databse is not always required, only from time to time,
and those requests are slow and consumes a vast amount of system resources.
"""


# Subject
class SampleService(ABC):
    @abstractmethod
    def get_sample(self, instrument: str, sample_name: str) -> str:
        pass


# RealSubject
class SampleDBService(SampleService):
    def get_sample(self, instrument: str, sample_name: str) -> str:
        print(f'SampleDBService: fetching {sample_name} for {instrument}')
        return f'{instrument}-{sample_name}.wav'


# Proxy
class SampleProxy(SampleService):
    def __init__(self, sample_db_service: SampleDBService) -> None:
        self._sample_db_service = sample_db_service

    def get_sample(
            self,
            instrument: str,
            sample_name: str,
            user: str = ''
            ) -> None:
        if self.check_access(user):
            self._sample_db_service.get_sample(instrument, sample_name)
            self.log('info', 'get sample', instrument, sample_name)
        else:
            self.log('error', 'access denied', instrument, sample_name)

    def check_access(self, user: str) -> bool:
        print('SampleProxy: checking access')
        return True if len(user) else False

    def log(
            self,
            level: str,
            message: str,
            instrument: str,
            sample_name: str
            ) -> None:
        print('SampleProxy log:')
        print(f'\t{level} - {message} - {instrument} - {sample_name}')


# client code
def play_instrument_samples(
        sample_service: SampleService,
        instrument: str,
        sample_name: str,
        user: str = '',
        ) -> None:
    print('Client: requesting sample play')
    sample_service.get_sample(instrument, sample_name, user)


if __name__ == "__main__":
    sample_db_service = SampleDBService()
    sample_proxy = SampleProxy(sample_db_service)

    play_instrument_samples(sample_proxy, 'guitar', 'sample1')
    print()

    play_instrument_samples(sample_proxy, 'guitar', 'sample2', 'user1')
    print()
