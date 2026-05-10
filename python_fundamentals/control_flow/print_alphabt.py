#!/usr/bin/env python3
print(
    '{0}'.format(
        ''.join(
            chr(i)
            for i in range(ord('a'), ord('z') + 1)
            if chr(i) not in 'qe'
        )
    )
)
