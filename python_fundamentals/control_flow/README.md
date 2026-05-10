# control_flow

Scripts here play with branching—mostly simple `if`/`elif`/`else` and letting the program take different paths based on a value.

## `positive_or_negative.py`

Each run pulls one random integer from **-10 through 10** using:

```python
number = __import__('random').randint(-10, 10)
```

After that it’s straightforward: if the number’s above zero, it prints that it’s positive; if it’s exactly zero, it says zero; otherwise negative. Every execution prints exactly one of those three sentences—whatever matches the random draw.

From this folder:

```bash
./positive_or_negative.py
```

mk21b
