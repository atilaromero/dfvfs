#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for the encoded stream resolver helper implementation."""

from __future__ import unicode_literals

import unittest

from dfvfs.resolver import encoded_stream_resolver_helper

from tests.resolver import test_lib


class EncodedStreamResolverHelperTest(test_lib.ResolverHelperTestCase):
  """Tests for the encoded stream resolver helper implementation."""

  def testNewFileObject(self):
    """Tests the NewFileObject function."""
    resolver_helper_object = (
        encoded_stream_resolver_helper.EncodedStreamResolverHelper())
    self._TestNewFileObject(resolver_helper_object)

  def testNewFileSystem(self):
    """Tests the NewFileSystem function."""
    resolver_helper_object = (
        encoded_stream_resolver_helper.EncodedStreamResolverHelper())
    self._TestNewFileSystem(resolver_helper_object)


if __name__ == '__main__':
  unittest.main()
