PEP: XXX
Title: Asynchronous IO support
Version: $Revision$
Last-Modified: $Date$
Author: Laurens Van Houtven <_@lvh.cc>
Status: Draft
Type: Standards Track
Content-Type: text/x-rst
Created: 29-May-2011
Post-History: TBD

Abstract
========

This PEP describes an abstraction of asynchronous IO for the Python
standard library.

The goal is to reach a abstraction that can be implemented by many
different asynchronous IO backends and provides a target for library
developers to write code portable between those different backends.

Rationale
=========

People who want to write asynchronous code in Python right now have a
few options:

 - ``asyncore`` and ``asynchat``
 - something bespoke, most likely based on the ``select`` module
 - using a third party library, such as Twisted_ or gevent_

Unfortunately, each of these options has its downsides, which this PEP
tries to address.

XXX Find a way to describe how bad asyncore is in 1 or 2 paragraphs

The most popular solution right now used in production involves the
use of third party libraries. These often provide satisfactory
solutions, but there is a lack of compatibility between these
libraries, which tends to make codebases very tightly coupled to the
library they use.

This current lack of portability between different asynchronous IO
libraries causes a lot of duplicated effort for third party library
developers. A sufficiently powerful abstraction could mean that
asynchronous code gets written once, but used everywhere.

An eventual added goal would be for standard library implementations
of wire and network protocols to evolve towards being real protocol
implementations, as opposed to standalone libraries that do everything
including calling ``recv()`` blockingly. This means they could be
easily reused for both synchronous and asynchronous code.

.. _Twisted: http://www.twistedmatrix.com/
.. _gevent: http://www.gevent.org/

Transports
==========

A transport is responsible for getting bytes from and to the other side of a connection. It is the interface to something like a socket, a (named) pipe, a serial port... A transport encapsulates all of the specific implementation details to it.

Transports talk to two things: that other side of the connection one one hand, and a protocol on the other. It's a bridge between that specific underlying transfer mechanism and the protocol. Its job can be described as allowing the protocol to just send and receive bytes, taking care of all of the magic that needs to happen for those bytes to be eventually sent across the wire.

The primary feature of a transport is sending bytes to a protocol and receiving bytes from the underlying protocol. Writing to the transport is done using the ``write`` and ``write_sequence`` methods. The latter method is a performance optimization, to allow software to take advantage of specific capabilities in some transport mechanisms. Specifically, this allows transports to use writev_ instead of write_ or send_, also known as scatter/gather IO.

A transport can be paused and resumed. This will cause it to buffer data coming from protocols, and stop sending received data to the protocol.

A transport can also be closed, half-closed and aborted. A closed transport will finish writing all of the data queued in it to the underlying mechanism. A half-closed transport can't be written to anymore, but will still accept incoming data.

Protocols
=========

Why separate protocols and transports?
======================================

This separation between protocol and transport often confuses people who first come across it. In fact, the standard library itself does not make this distinction in many cases, particularly not in the API it provides to users.

It is nonetheless a very useful distinction. In the worst case, it simplifies the implementation by clear separation of concerns. However, it often serves the far more useful purpose of being able to reuse protocols across different transports.

Consider a simple RPC protocol. The same bytes may be transferred across many different transports, for example pipes or sockets. To help with this, we separate the protocol out from the transport. The protocol just reads and writes bytes, and doesn't really care what mechanism is used to eventually transfer those bytes.

This also allows for protocols to be stacked or nested easily, allowing for even more code reuse. A common example of this is JSON-RPC: according to the specification, it can be used across both sockets and HTTP. In practice, it tends to be primarily encapsulated in HTTP. The protocol-transport abstraction allows us to build a stack of protocols and transports that allow you to use HTTP as if it were a transport. For JSONRPC, that might get you a stack somewhat like this:

1. TCP socket transport
2. HTTP protocol
3. HTTP-based transport (for which the above HTTP protocol is the underlying mechanism for transferring bytes)
4. JSON-RPC protocol
5. Application code

Consumers
=========

Producers
=========

References
==========

.. _writev: http://pubs.opengroup.org/onlinepubs/009695399/functions/writev.html
.. _write: http://pubs.opengroup.org/onlinepubs/009695399/functions/write.html
.. _send: http://pubs.opengroup.org/onlinepubs/009695399/functions/send.html

Copyright
=========

This document has been placed in the public domain.



..
   Local Variables:
   mode: indented-text
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   coding: utf-8
   End:
