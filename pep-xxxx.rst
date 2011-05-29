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
different asynchronous IO backends, provides a target for library
developers to write code portable between those different backends,
and to provide an obvious starting point for end users that want to
write asynchronous applications.

Rationale
=========

The current lack of portability between different asynchronous IO
libraries causes a lot of duplicated effort for third party library
developers. A sufficiently powerful abstraction could mean that
asynchronous code gets written once, but used everywhere.

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
