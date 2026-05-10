#!/usr/bin/env python3
print(
    '{0}'.format(
        '\n'.join(
            '{0} = 0x{0:x}'.format(i)
            for i in range(99)
        )
    ),
)
