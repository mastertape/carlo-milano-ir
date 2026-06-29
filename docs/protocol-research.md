# Protocol Research Notes

Primary source: reverse-engineered Carlo Milano NX-7532-675 / REV1_2016 IR
captures.

## Frame Shape

- Carrier: 38 kHz
- Length: 9 bytes / 72 bits
- Bit order: MSB-first
- Header: 12000 us mark, 5130 us space
- Bit mark: 550 us
- One space: 1950 us
- Zero space: 500 us
- Footer: 550 us mark
- Checksum: byte 8 is sum(byte 0..7) modulo 256

## Field Map

```text
Byte 0: fixed 0x55
Byte 1:
  bit 0: vertical swing
  bit 1: power
  bit 3: timer set
  bits 4-7: Celsius setpoint offset from 16 C
Byte 2: timer hours, 0-24 when timer bit is set
Byte 3: Fahrenheit setpoint offset from 59 F
Byte 4: observed 0x00
Byte 5: observed 0x00
Byte 6:
  bits 0-3: mode
  bits 4-7: fan
Byte 7: context / unit variant
Byte 8: checksum
```

## Mode Values

```text
0 = auto
1 = cool
2 = dry
3 = fan_only
```

Captured mode cycle from the remote:

```text
Cool -> Fan -> Dry -> Auto -> Cool
```

## Fan Values

```text
1 = low
2 = mid
3 = high
```

Known constraints from captures and manual behavior:

- cool supports low, mid, high
- dry is fixed to low
- fan_only is fixed to high on this remote
- auto is fixed to high on this remote

## Byte 7 Contexts

```text
0x88 = stable Celsius state used for confirmed sends
0x80 = Celsius remote adjustment / mode-cycle captures
0xC0 = Celsius temperature adjustment captures
0x40 = Fahrenheit temperature adjustment captures
0x82 = selected timer-hour value
0x83 = timer entry/display frame
```

The integration uses `0x88` for generated Celsius states because that variant
has been confirmed as sendable on the tested unit.

## Important Captured Frames

```text
Cool 17 C Fan High Swing Off Power On:
55 12 00 04 00 00 31 88 24

Cool 17 C Fan High Swing Off Power Off:
55 10 00 04 00 00 31 88 22

Max-cool convenience state:
55 12 00 04 00 00 31 88 24

Cool 29 C Fan Low:
55 D2 00 19 00 00 11 88 D9

Cool 29 C Fan Mid:
55 D2 00 19 00 00 21 88 E9

Cool 29 C Fan High Swing On:
55 D3 00 19 00 00 31 88 FA

Fahrenheit 62 F:
55 12 00 03 00 00 31 40 DB

Timer 24 h:
55 1A 18 04 00 00 31 82 3E
```

## Manual-Only / Not IR-Confirmed

The Carlo Milano manual describes panel-only functions:

- Super-Kuehlung: `TIMER + UP` on the unit panel while in COOL mode.
- Schlaf-Modus: `TIMER + DOWN` on the unit panel while in COOL mode.

The current integration does not claim to send the internal panel-only
Super-Kuehlung or Schlaf-Modus. `send_max_cool` only sends the strongest
confirmed remote-sendable state: Cool, 17 C, Fan High, Power On.

## Upstream Compatibility Reference

IRremoteESP8266 calls a compatible state format `TROTEC_3550`. This project
uses that name only as a protocol compatibility cross-check and does not infer
hardware origin from it.
