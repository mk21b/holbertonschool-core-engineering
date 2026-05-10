#!/usr/bin/env python3
print(
    '{0}'.format(
        ', '.join(
            '{0:02d}'.format(i)
            for i in range(100)
        )
    ),
)
