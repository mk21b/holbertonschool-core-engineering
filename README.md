# holbertonschool-core-engineering

Small Python fundamentals exercises—mostly printing things and branching on simple conditions.

## `python_fundamentals/hello_world/structured_output.py`

This one is deliberately rigid: every line of output has to match the checker exactly.

It pulls `math.pi`, rounds it to two decimal places, and prints that as `3.14`. The “computation valid” line is just comparing that rounded value to `314 / 100`, which should come out `True` when everything lines up. Nothing fancy—no input, no CLI flags—run it and you get the four fixed lines every time.

```bash
./python_fundamentals/hello_world/structured_output.py
```

## `python_fundamentals/control_flow/positive_or_negative.py`

Here the program picks a random integer from -10 through 10 (inclusive) using the line Holberton gives you with `__import__('random')`. Then it checks the value: above zero prints “positive”, exactly zero prints “zero”, otherwise “negative”. Run it a few times and you’ll see different numbers; the logic itself stays the same.

```bash
./python_fundamentals/control_flow/positive_or_negative.py
```

---

mk21b
