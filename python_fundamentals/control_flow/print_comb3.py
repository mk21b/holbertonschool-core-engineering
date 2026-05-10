#!/usr/bin/env python3
print(
    '{0}'.format(
        ', '.join(
            '{0}{1}'.format(i, j)
            for i in range(10)
            for j in range(i + 1, 10)
        )
    ),
)
