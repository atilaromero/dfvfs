#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2013 The dfVFS Project Authors.
# Please see the AUTHORS file for details on individual authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dfvfs.analyzer import bde_analyzer_helper
from dfvfs.analyzer import bzip2_analyzer_helper
from dfvfs.analyzer import ewf_analyzer_helper
from dfvfs.analyzer import gzip_analyzer_helper
from dfvfs.analyzer import qcow_analyzer_helper
from dfvfs.analyzer import tar_analyzer_helper

try:
  from dfvfs.analyzer import tsk_analyzer_helper
except ImportError:
  pass

try:
  from dfvfs.analyzer import tsk_partition_analyzer_helper
except ImportError:
  pass

from dfvfs.analyzer import vhdi_analyzer_helper
from dfvfs.analyzer import vmdk_analyzer_helper
from dfvfs.analyzer import vshadow_analyzer_helper
from dfvfs.analyzer import zip_analyzer_helper
