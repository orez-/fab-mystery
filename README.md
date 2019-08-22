# Fab mystery

To demo:
```
~/src/fab-mystery $ python --version
Python 2.7.16
~/src/fab-mystery $ pip install "fabric<2"
~/src/fab-mystery $ fab bar.baz
calling bar.baz

Done.
~/src/fab-mystery $ fab foo.baz
calling bar.baz

~/src/fab-mystery $ ?????? that should be "calling foo.baz"
```
