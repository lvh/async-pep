"""
An example composable protocol for receiving chunks delimited by some byte
sequence.
"""
import io

from protocols import abstract

MODES = CHUNKED, RAW = object(), object()

class ChunkProtocol(abstract.Protocol):
    """
    A protocol consisting of chunks delimited by some fixed delimiter. Common
    examples include line-delimited protocols such as HTTP, IRC...
    """
    delimiter = b"\0"
    mode = CHUNKED

    def __init__(self):
        self._buffer = b""


    def data_received(self, data):
        if self.mode is RAW:
            return self.raw_data_received(data)

        self._buffer += data
        *chunks, rest = self._buffer.split(self.delimiter)

        if chunks:
            self._buffer = rest
            for chunk in chunks:
                self.chunk_received(chunk)


    def raw_data_received(self, data):
        """
        Some data was received while the protocol was in ``RAW`` mode.

        This is exactly the same as ``data_received`` on an ordinary protocol.
        """


    def chunk_received(self, chunk):
        """
        A single chunk of data has been received.
        """



    def send_chunk(self, chunk):
        """
        Sends ``chunk`` through the transport, followed by a delimiter.
        """
        self.transport.write_sequence([chunk, self.delimiter])
