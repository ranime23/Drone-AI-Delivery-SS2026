# Contributing

For every flight-critical parameter change, document:

1. Parameter name
2. Old value
3. New value
4. Reason
5. Test
6. Result

Example:

```text
ATC_RAT_PIT_P
old: 0.08
new: 0.06
reason: reduce oscillation
test: controlled hover
result: improved stability
```

Keep the raw final parameter export versioned.
