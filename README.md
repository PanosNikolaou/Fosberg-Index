# Fosberg Fire Weather Index

A small Python script that calculates a Fosberg Fire Weather Index value from hard-coded temperature, humidity, and wind-speed inputs.

## Run

The script uses only Python's standard library:

```sh
python fosberg.py
```

It prints the rounded index value. To try other inputs, edit `temperature`, `humidity`, and `windspeed` at the top of `fosberg.py` and run the script again. The calculation treats humidity as a percentage and wind speed as miles per hour.

## Limitations

This is a standalone formula demonstration, not a validated operational fire-risk forecast. Confirm input units, applicable formula assumptions, and results against an authoritative implementation before using it for decisions.
