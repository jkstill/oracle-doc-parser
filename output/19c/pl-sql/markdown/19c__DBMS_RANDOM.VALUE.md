---
id: 19c__DBMS_RANDOM.VALUE
name: DBMS_RANDOM.VALUE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RANDOM
tags: [dbms_random]
source_file: DBMS_RANDOM.html
---

# DBMS_RANDOM.VALUE

The basic function gets a random number, greater than or equal to 0 and less than 1, with 38 digits to the right of the decimal (38-digit precision). Alternatively, you can get a random Oracle number x, where x is greater than or equal to low and less than high .

## Syntax

```sql
DBMS_RANDOM.VALUE
  RETURN NUMBER;

DBMS_RANDOM.VALUE(
  low  IN  NUMBER,
  high IN  NUMBER)
RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| low | NUMBER | IN | Lowest number in a range from which to generate a random number. The number generated may be equal to low |
| high | NUMBER) | IN | Highest number below which to generate a random number. The number generated will be less than high |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_RANDOM.VALUE RETURN NUMBER; DBMS_RANDOM.VALUE( low IN NUMBER, high IN NUMBER) RETURN NUMBER; Parameters Table 136-8 VALUE Function Parameters Parameter Description low Lowest number in a range from which to generate a random number. The number generated may be equal to low high Highest number below which to generate a random number. The number generated will be less than high Return Values Table 136-9 VALUE Function Return Values Parameter Description NUMBER Returns an Oracle Number