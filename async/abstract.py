"""
The interfaces for implementing asynchronous IO.
"""
import abc

class FlowControl(metaclass=abc.ABCMeta):
    @abstractmethod
    def pause(self):
        """
        Pause sending data.
        """

    @abstractmethod
    def resume(self): 
        """
        Resume sending data sending data.
        """

class Protocol(FlowControl):
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
    def connection_closed(self, reason):
        """
        Called when the connection is closed.
        """

class Transport(FlowControl):
    @abstractmethod
    def write(self, data):
        """
        Write some data into the transport.

        The data must be a bytestring.
        """

    @abstractmethod
    def write_sequence(self, sequence_of_strings):
        """
        Write a sequence of data.

        Each piece of data must be a bytestring.
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
