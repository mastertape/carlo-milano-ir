# Compatibility And White-Label Research

This integration is named for the broader Compact 9000 BTU platform while being
confirmed first on a PEARL / Carlo Milano NX-7532-675 portable air conditioner
with the REV1_2016 remote.

The likely broader product family is a compact 9000 BTU white-label portable
air-conditioner platform. Please treat the lists below as research status, not
as manufacturer claims.

## Confirmed With Local Captures

- PEARL / Carlo Milano NX-7532-675
- Remote marked REV1_2016
- Manual file observed locally: `NX7532_11_158208.pdf`
- Cooling class: 9000 BTU / 2.6 kW
- Body type: compact cube-style portable AC with top air outlet

## Likely Same Or Related Platform

These names are included for discovery and comparison. They still need
community confirmation with photos, manuals, type plates, or IR captures.

- Carlo Milano NX-7532
- Carlo Milano NX-7532-919
- electriQ Compact 9000 BTU
- electriQ COMPACT-V2
- electriQ Compact portable air conditioner

## Protocol Search Terms

The captured Compact 9000 BTU state format matches the timing and field layout
of the protocol known upstream as `TROTEC_3550` in IRremoteESP8266. This is a
protocol compatibility reference only, not a manufacturer claim.

Useful search terms:

- Carlo Milano NX-7532
- Carlo Milano NX-7532-675
- Carlo Milano NX-7532-919
- PEARL Compact 9000 BTU
- electriQ Compact
- electriQ Compact 9000 BTU
- electriQ COMPACT-V2
- compact 9000 BTU portable air conditioner
- TROTEC_3550
- IRremoteESP8266 Trotec3550
- REV1_2016 remote

## Not Confirmed As Hardware Twins

- Trotec PAC 2100 X
- Trotec PAC 2600 X

Those Trotec names are useful for protocol archaeology because of the upstream
`TROTEC_3550` label, but the known Trotec PAC device family should not be
treated as a confirmed physical twin of the tested Compact 9000 BTU unit without
matching captures or documentation.

## Help Wanted

If you own a similar compact 9000 BTU portable AC, please open an issue with:

- brand and exact model number
- photos of the unit, type plate, and remote
- manual PDF or public product/manual link
- whether the remote has a REV1_2016 or similar marking
- one or more decoded IR frames, preferably:
  - power on
  - cool 17 C fan high swing off
  - mode cycle
  - fan cycle
  - timer values
  - Celsius/Fahrenheit toggle

Please do not submit assumptions such as "looks like Trotec" as confirmed
compatibility. The useful evidence is a matching manual, matching remote, or a
checksum-valid 9-byte frame compatible with this integration.
