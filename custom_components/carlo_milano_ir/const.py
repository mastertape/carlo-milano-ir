"""Constants for the Compact 9000 BTU IR integration."""

from __future__ import annotations

DOMAIN = "carlo_milano_ir"
NAME = "Compact 9000 BTU IR"

DEFAULT_EMITTER = "infrared.xiao_smart_ir_mate_ir_proxy_transmitter"
PICON_URL_PATH = "/carlo_milano_ir/picon.png"

CONF_CODE = "code"
CONF_FAN = "fan"
CONF_MODE = "mode"
CONF_POWER = "power"
CONF_REPEAT = "repeat"
CONF_SWING = "swing"
CONF_TEMPERATURE = "temperature"
CONF_TEMPERATURE_UNIT = "temperature_unit"
CONF_TIMER_HOURS = "timer_hours"

MAX_REPEAT = 5

MODES = ("auto", "cool", "dry", "fan_only", "off")
FANS = ("low", "mid", "high")

TEMP_MIN_C = 17
TEMP_MAX_C = 30
TEMP_MIN_F = 62
TEMP_MAX_F = 86

TEMP_UNIT_CELSIUS = "celsius"
TEMP_UNIT_FAHRENHEIT = "fahrenheit"
TEMP_UNITS = (TEMP_UNIT_CELSIUS, TEMP_UNIT_FAHRENHEIT)

CARLO_MILANO_MODULATION = 38000
CARLO_MILANO_STATE_LENGTH = 9
CARLO_MILANO_BITS = 72

CARLO_MILANO_HDR_MARK = 12000
CARLO_MILANO_HDR_SPACE = 5130
CARLO_MILANO_BIT_MARK = 550
CARLO_MILANO_ONE_SPACE = 1950
CARLO_MILANO_ZERO_SPACE = 500
CARLO_MILANO_MESSAGE_GAP = 100000

CARLO_MILANO_INTRO = 0x55
CARLO_MILANO_CELSIUS_STABLE = 0x88
CARLO_MILANO_FAHRENHEIT = 0x40
CARLO_MILANO_CELSIUS_TIMER_SELECTED = 0x82
CARLO_MILANO_TIMER_SET_BIT = 0x08

CARLO_MILANO_MIN_TEMP_C = 16
CARLO_MILANO_MIN_TEMP_F = 59

TIMER_MIN_HOURS = 0
TIMER_MAX_HOURS = 24

MODE_VALUES = {
    "auto": 0x00,
    "cool": 0x01,
    "dry": 0x02,
    "fan_only": 0x03,
    "off": 0x01,
}

FAN_VALUES = {
    "low": 0x01,
    "mid": 0x02,
    "high": 0x03,
}
