"""
The interfaces for implementing asynchronous IO.
"""
import abc

class Protocol(metaclass=abc.ABCMeta):
    def connected(self, transport):
        """
        Called when the connection is established.
        """
        self.transport = transport

    @abc.abstractmethod
    def data_received(self, data):
        """
        Called when some data is received.
        """

    def disconnected(self, reason):
        """
        Called when the connection is closed.
        """
        self.transport = None

class Transport(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self, data):
        """
        Write some data into the transport.

        The data must be buffer of bytes.
        """

    @abc.abstractmethod
    def write_sequence(self, sequence):
        """
        Write a sequence of data.

        The sequence must be a sequence of buffers of bytes.
        """

    @abc.abstractmethod
    def close(self):
        """
        Close the connection after sending queued data.
        """

    @abc.abstractmethod
    def abort(self):
        """
        Immediately close the connection without sending queued data.
        """

    @abc.abstractmethod 
    def half_close(self):
        """
        Close the connection after sending queued data.

        Incoming data will still be accepted. 
        """
