#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:dynamic,slots
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *

COMPACT_TEST = CompactProtoTestStruct(**{
  "a_byte" : 127,
  "a_i16" : 32000,
  "a_i32" : 1000000000,
  "a_i64" : 1099511627775,
  "a_double" : 5.6789,
  "a_string" : "my string",
  "true_field" : True,
  "false_field" : False,
  "empty_struct_field" : Empty(**{
  }),
  "byte_list" : [
    -127,
    -1,
    0,
    1,
    127,
  ],
  "i16_list" : [
    -1,
    0,
    1,
    32767,
  ],
  "i32_list" : [
    -1,
    0,
    255,
    65535,
    16777215,
    2147483647,
  ],
  "i64_list" : [
    -1,
    0,
    255,
    65535,
    16777215,
    4294967295,
    1099511627775,
    281474976710655,
    72057594037927935,
    9223372036854775807,
  ],
  "double_list" : [
    0.1,
    0.2,
    0.3,
  ],
  "string_list" : [
    "first",
    "second",
    "third",
  ],
  "boolean_list" : [
    True,
    True,
    True,
    False,
    False,
    False,
  ],
  "struct_list" : [
    Empty(**{
    }),
    Empty(**{
    }),
  ],
  "byte_set" : set([
    -127,
    -1,
    0,
    1,
    127,
  ]),
  "i16_set" : set([
    -1,
    0,
    1,
    32767,
  ]),
  "i32_set" : set([
    1,
    2,
    3,
  ]),
  "i64_set" : set([
    -1,
    0,
    255,
    65535,
    16777215,
    4294967295,
    1099511627775,
    281474976710655,
    72057594037927935,
    9223372036854775807,
  ]),
  "double_set" : set([
    0.1,
    0.2,
    0.3,
  ]),
  "string_set" : set([
    "first",
    "second",
    "third",
  ]),
  "boolean_set" : set([
    True,
    False,
  ]),
  "struct_set" : set([
    Empty(**{
    }),
  ]),
  "byte_byte_map" : {
    1 : 2,
  },
  "i16_byte_map" : {
    1 : 1,
    -1 : 1,
    32767 : 1,
  },
  "i32_byte_map" : {
    1 : 1,
    -1 : 1,
    2147483647 : 1,
  },
  "i64_byte_map" : {
    0 : 1,
    1 : 1,
    -1 : 1,
    9223372036854775807 : 1,
  },
  "double_byte_map" : {
    -1.1 : 1,
    1.1 : 1,
  },
  "string_byte_map" : {
    "first" : 1,
    "second" : 2,
    "third" : 3,
    "" : 0,
  },
  "boolean_byte_map" : {
    True : 1,
    False : 0,
  },
  "byte_i16_map" : {
    1 : 1,
    2 : -1,
    3 : 32767,
  },
  "byte_i32_map" : {
    1 : 1,
    2 : -1,
    3 : 2147483647,
  },
  "byte_i64_map" : {
    1 : 1,
    2 : -1,
    3 : 9223372036854775807,
  },
  "byte_double_map" : {
    1 : 0.1,
    2 : -0.1,
    3 : 1e+06,
  },
  "byte_string_map" : {
    1 : "",
    2 : "blah",
    3 : "loooooooooooooong string",
  },
  "byte_boolean_map" : {
    1 : True,
    2 : False,
  },
  "list_byte_map" : {
    [
      1,
      2,
      3,
    ] : 1,
    [
      0,
      1,
    ] : 2,
    [
    ] : 0,
  },
  "set_byte_map" : {
    set([
      1,
      2,
      3,
    ]) : 1,
    set([
      0,
      1,
    ]) : 2,
    set([
    ]) : 0,
  },
  "map_byte_map" : {
    {
      1 : 1,
    } : 1,
    {
      2 : 2,
    } : 2,
    {
    } : 0,
  },
  "byte_map_map" : {
    0 : {
    },
    1 : {
      1 : 1,
    },
    2 : {
      1 : 1,
      2 : 2,
    },
  },
  "byte_set_map" : {
    0 : set([
    ]),
    1 : set([
      1,
    ]),
    2 : set([
      1,
      2,
    ]),
  },
  "byte_list_map" : {
    0 : [
    ],
    1 : [
      1,
    ],
    2 : [
      1,
      2,
    ],
  },
})
MYCONST = 2
MY_SOME_ENUM = 1
MY_SOME_ENUM_1 = 1
MY_ENUM_MAP = {
    1 :   2,
}
EXTRA_CRAZY_MAP = {
    1 : StructWithSomeEnum(**{
    "blah" :     2,
  }),
}
