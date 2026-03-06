---
id: 19c__UTL_NLA.BLAS_NRM2
name: UTL_NLA.BLAS_NRM2
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_NRM2

This function computes the vector 2-norm (Euclidean norm).

## Syntax

```sql
UTL_NLA.BLAS_NRM2 (
   n     IN   POSITIVEN,
   x     IN   UTL_NLA_ARRAY_DBL,
   incx  IN   POSITIVEN)
  RETURN BINARY_DOUBLE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | POSITIVEN | IN | Specifies the number of elements of the vectors x and y . n must be at least zero. |
| x | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 )*abs( incx ) ) |
| incx | POSITIVEN) | IN | Specifies the increment for the elements of x . incx must not be zero. |

**Returns:** `BINARY_DOUBLE`

## Usage Notes

See Also: BLAS Level 1 (Vector-Vector Operations) Subprograms for other subprograms in this group See Also: BLAS Level 1 (Vector-Vector Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_NRM2 ( n IN POSITIVEN, x IN UTL_NLA_ARRAY_DBL, incx IN POSITIVEN) RETURN BINARY_DOUBLE; UTL_NLA.BLAS_NRM2 ( n IN POSITIVEN, x IN UTL_NLA_ARRAY_FLT, incx IN POSITIVEN) RETURN BINARY_FLOAT; Parameters Table 271-16 BLAS_NRM2 Function Parameters Parameter Description n Specifies the number of elements of the vectors x and y . n must be at least zero. x UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 )*abs( incx ) ) incx Specifies the increment for the elements of x . incx must not be zero.