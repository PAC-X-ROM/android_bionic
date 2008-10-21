# this module contains all the defaults used by the generation of cleaned-up headers
# for the Bionic C library
#

import time, os, sys
from utils import *

# the list of supported architectures
#
kernel_archs = [ 'arm', 'x86' ]

# the list of include directories that belong to the kernel
# tree. used when looking for sources...
#
kernel_dirs = [ "linux", "asm", "asm-generic", "mtd" ]

# path to the directory containing the original kernel headers
#
kernel_original_path = os.path.normpath( find_program_dir() + '/../original' )

# a special value that is used to indicate that a given macro is known to be
# undefined during optimization
kCppUndefinedMacro = "<<<undefined>>>"

# this is the set of known macros we want to totally optimize out from the
# final headers
kernel_known_macros = {
    "__KERNEL__": kCppUndefinedMacro,
    "__KERNEL_STRICT_NAMES":"1",
    "__CHECKER__": kCppUndefinedMacro,
    "__CHECK_ENDIAN__": kCppUndefinedMacro,
    }

# define to true if you want to remove all defined(CONFIG_FOO) tests
# from the clean headers. testing shows that this is not strictly necessary
# but just generates cleaner results
kernel_remove_config_macros = True

# this is the set of known static inline functions that we want to keep
# in the final ARM headers. this is only used to keep optimized byteswapping
# static functions and stuff like that.
kernel_known_arm_statics = set(
       [ "___arch__swab32",    # asm-arm/byteorder.h
       ]
    )

kernel_known_x86_statics = set(
        [ "___arch__swab32",  # asm-x86/byteorder.h
          "___arch__swab64",  # asm-x86/byteorder.h
        ]
    )

kernel_known_generic_statics = set(
        [ "__invalid_size_argument_for_IOC",  # asm-generic/ioctl.h
          "__cmsg_nxthdr",                    # linux/socket.h
          "cmsg_nxthdr",                      # linux/socket.h
          "ipt_get_target",
        ]
    )

# this maps an architecture to the set of static inline functions that
# we want to keep in the final headers
#
kernel_known_statics = {
        "arm" : kernel_known_arm_statics,
        "x86" : kernel_known_x86_statics
    }

# this is the standard disclaimer
#
kernel_disclaimer = """\
/****************************************************************************
 ****************************************************************************
 ***
 ***   This header was automatically generated from a Linux kernel header
 ***   of the same name, to make information necessary for userspace to
 ***   call into the kernel available to libc.  It contains only constants,
 ***   structures, and macros generated from the original header, and thus,
 ***   contains no copyrightable information.
 ***
 ****************************************************************************
 ****************************************************************************/
"""
