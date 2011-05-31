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

.. _Twisted: http://www.twistedmatrix.com/
.. _gevent: http://www.gevent.org/

Protocols
=========

Transports
==========

Consumers
=========

Producers
=========

References
==========

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
