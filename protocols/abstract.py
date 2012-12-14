"""
The interfaces for implementing asynchronous IO.
"""
import abc

class Protocol(metaclass=abc.ABCMeta):
    @abstractmethod
    def connected(self, transport):
        """
        Called when the connection is established.
        """

    @abstractmethod
    def data_received(self, data):
        """
        Called when some data is received.
        """

    @abstractmethod
    def disconnected(self, reason):
        """
        Called when the connection is closed.
        """

class Transport(FlowControl):
    @abstractmethod
    def write(self, data):
        """
        Write some data into the transport.

        The data must be buffer of bytes.
        """

    @abstractmethod
    def write_sequence(self, sequence):
        """
        Write a sequence of data.

        The sequence must be a sequence of buffers of bytes.
        """

    @abstractmethod
    def close(self):
        """
        Close the connection after sending queued data.
        """

    @abstractmethod
    def abort(self):
        """
        Immediately close the connection without sending queued data.
        """

    @abstractmethod
    def half_close(self):
        """
        Close the connection after sending queued data.

        Incoming data will still be accepted. 
        """
