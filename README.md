# timerdec

A timing decorator module.

## Installation

```
pip install git+https://github.com/goessl/timerdec.git
```

## Usage

This package provides a single decorator, `timerdec`.
The execution of any function decorated with `timerdec` gets timed and the elapsed time is then passed to the provided consumer, that was provided to the decorator in milliseconds.
```python
>>> from timerdec import timerdec
>>> @timerdec(lambda t: print('Took', 1000*t, 'ms.'))
... def foo():
...     for _ in range(1000000):
...         pass
>>> foo()
Took 23.371541989035904 ms.
```

## License (MIT)

Copyright (c) 2023 Sebastian Gössl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
