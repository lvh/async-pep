"""
Tests for chunk protocols.
"""
import unittest

from protocols import chunks

class LoggingChunkProtocol(chunks.ChunkProtocol):
    def __init__(self):
        super().__init__()
        self.raw, self.chunks = [], []

    def raw_data_received(self, data):
        self.raw.append(data)

    def chunk_received(self, chunk):
        self.chunks.append(chunk)


class ChunkProtocolTests(unittest.TestCase):
    def setUp(self):
        self.protocol = LoggingChunkProtocol()

    def test_whole(self):
        """
        Tests receiving a whole chunk with a delimiter.
        """
        self.protocol.data_received(b"a\0")
        self.assertEqual(self.protocol.chunks, [b"a"])

    def test_split(self):
        """
        Tests receiving some split chunks.
        """
        for piece in [b"abc", b"\0de", b"f\0g", b"hi\0"]:
            self.protocol.data_received(piece)
        self.assertEqual(self.protocol.chunks, [b"abc", b"def", b"ghi"])

    def test_raw(self):
        """
        Test receiving some raw data.
        """
        self.protocol.mode = chunks.RAW

        self.protocol.data_received(b"a")
        self.assertEqual(self.protocol.raw, [b"a"])

        self.protocol.data_received(b"b")
        self.assertEqual(self.protocol.raw, [b"a", b"b"])
