import abc
from _typeshed import Incomplete

from pika.adapters.utils import io_services_utils, nbio_interface

LOGGER: Incomplete

class AbstractSelectorIOLoop(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def READ(self): ...
    @property
    @abc.abstractmethod
    def WRITE(self): ...
    @property
    @abc.abstractmethod
    def ERROR(self): ...
    @abc.abstractmethod
    def close(self): ...
    @abc.abstractmethod
    def start(self): ...
    @abc.abstractmethod
    def stop(self): ...
    @abc.abstractmethod
    def call_later(self, delay, callback): ...
    @abc.abstractmethod
    def remove_timeout(self, timeout_handle): ...
    @abc.abstractmethod
    def add_callback(self, callback): ...
    @abc.abstractmethod
    def add_handler(self, fd, handler, events): ...
    @abc.abstractmethod
    def update_handler(self, fd, events): ...
    @abc.abstractmethod
    def remove_handler(self, fd): ...

class SelectorIOServicesAdapter(
    io_services_utils.SocketConnectionMixin,
    io_services_utils.StreamingConnectionMixin,
    nbio_interface.AbstractIOServices,
    nbio_interface.AbstractFileDescriptorServices,
):
    def __init__(self, native_loop) -> None: ...
    def get_native_ioloop(self): ...
    def close(self) -> None: ...
    def run(self) -> None: ...
    def stop(self) -> None: ...
    def add_callback_threadsafe(self, callback) -> None: ...
    def call_later(self, delay, callback): ...
    def getaddrinfo(self, host, port, on_done, family: int = 0, socktype: int = 0, proto: int = 0, flags: int = 0): ...
    def set_reader(self, fd, on_readable) -> None: ...
    def remove_reader(self, fd): ...
    def set_writer(self, fd, on_writable) -> None: ...
    def remove_writer(self, fd): ...

class _FileDescriptorCallbacks:
    reader: Incomplete
    writer: Incomplete
    def __init__(self, reader: Incomplete | None = None, writer: Incomplete | None = None) -> None: ...

class _TimerHandle(nbio_interface.AbstractTimerReference):
    def __init__(self, handle, loop) -> None: ...
    def cancel(self) -> None: ...

class _SelectorIOLoopIOHandle(nbio_interface.AbstractIOReference):
    def __init__(self, subject) -> None: ...
    def cancel(self): ...

class _AddressResolver:
    NOT_STARTED: int
    ACTIVE: int
    CANCELED: int
    COMPLETED: int
    def __init__(self, native_loop, host, port, family, socktype, proto, flags, on_done) -> None: ...
    def start(self): ...
    def cancel(self): ...
