# This file is part of Telegram Desktop,
# the official desktop application for the Telegram messaging service.
#
# For license and copyright information please follow this link:
# https://github.com/telegramdesktop/tdesktop/blob/master/LEGAL

{
  'includes': [
    'helpers/common/common.gypi',
  ],
  'targets': [{
    'target_name': 'linux_glibc_wraps',
    'type': 'static_library',
    'sources': [
      '<(src_loc)/platform/linux/linux_glibc_wraps.c',
    ],
    'conditions': [[ '"<!(uname -m)" == "x86_64" or "<!(uname -m)" == "aarch64"', {
      'sources': [
        '<(src_loc)/platform/linux/linux_glibc_wraps_64.c',
      ],
    }, {
      'sources': [
        '<(src_loc)/platform/linux/linux_glibc_wraps_32.c',
      ],
    }]],
  }],
}
