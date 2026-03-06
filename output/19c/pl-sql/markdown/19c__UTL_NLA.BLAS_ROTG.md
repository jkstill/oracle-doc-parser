---
id: 19c__UTL_NLA.BLAS_ROTG
name: UTL_NLA.BLAS_ROTG
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_ROTG

This procedure returns the Givens rotation of points.

## Syntax

```sql
UTL_NLA.BLAS_ROTG (
   a   IN OUT   SCALAR_DOUBLE,
   b   IN OUT   SCALAR_DOUBLE,
   c   IN OUT   SCALAR_DOUBLE,
   s   IN OUT   SCALAR_DOUBLE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| a | SCALAR_DOUBLE | IN OUT | SCALAR_FLOAT / DOUBLE . Specifies the scalar A. |
| b | SCALAR_DOUBLE | IN OUT | SCALAR_FLOAT / DOUBLE . Specifies the scalar B. |
| c | SCALAR_DOUBLE | IN OUT | SCALAR_FLOAT / DOUBLE . Specifies the scalar C. |
| s | SCALAR_DOUBLE) | IN OUT | SCALAR_FLOAT / DOUBLE . Specifies the scalar S. |

## Usage Notes

See Also: BLAS Level 1 (Vector-Vector Operations) Subprograms for other subprograms in this group See Also: BLAS Level 1 (Vector-Vector Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_ROTG ( a IN OUT SCALAR_DOUBLE, b IN OUT SCALAR_DOUBLE, c IN OUT SCALAR_DOUBLE, s IN OUT SCALAR_DOUBLE); UTL_NLA.BLAS_ROTG ( a IN OUT SCALAR_FLOAT, b IN OUT SCALAR_FLOAT, c IN OUT SCALAR_FLOAT, s IN OUT SCALAR_FLOAT); Parameters Table 271-18 BLAS_ROTG Procedure Parameters Parameter Description a SCALAR_FLOAT / DOUBLE . Specifies the scalar A. b SCALAR_FLOAT / DOUBLE . Specifies the scalar B. c SCALAR_FLOAT / DOUBLE . Specifies the scalar C. s SCALAR_FLOAT / DOUBLE . Specifies the scalar S.