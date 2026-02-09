
```
tool [global flags] <command> [command flags] [input]
```

### Input

```
tool <command> data.csv
tool <command> < data.csv
```

---

### Commands

```
tool columns [--match REGEX] [input]
```

```
tool select col1,col2,... [--ignore-missing] [input]
```

```
tool filter VALUE
    [--column col1[,col2,...]]
    [--regex]
    [--ignore-case]
    [--first N]
    [input]
```

---

### Chaining

```
tool <command> ... | tool <command> ...
```

---

### Global flags

```
--no-header
--delimiter CHAR
```

---

### Exit codes

```
0    success
>0   error
```
