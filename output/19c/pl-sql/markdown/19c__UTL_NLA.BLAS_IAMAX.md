---
id: 19c__UTL_NLA.BLAS_IAMAX
name: UTL_NLA.BLAS_IAMAX
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_IAMAX

This function computes the index of first element of a vector that has the largest absolute value.

## Syntax

```sql
UTL_NLA.BLAS_IAMAX (
   n     IN   POSITIVEN,
   x     IN   UTL_NLA_ARRAY_DBL,
   incx  IN   POSITIVEN,
  RETURN POSITIVEN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | POSITIVEN | IN | Specifies the number of elements of the vectors x and y . n must be at least zero. |
| x | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of DIMENSION at least ( 1 + ( n - 1 )*abs( incx ) ) |
| incx | POSITIVEN | IN | Specifies the increment for the elements of x . incx must not be zero. |

**Returns:** `POSITIVEN`

## Usage Notes

See Also: BLAS Level 1 (Vector-Vector Operations) Subprograms for other subprograms in this group See Also: BLAS Level 1 (Vector-Vector Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_IAMAX ( n IN POSITIVEN, x IN UTL_NLA_ARRAY_DBL, incx IN POSITIVEN, RETURN POSITIVEN; UTL_NLA.BLAS_IAMAX ( n IN POSITIVEN, x IN UTL_NLA_ARRAY_FLT, incx IN POSITIVEN, RETURN POSITIVEN; Parameters Table 271-15 BLAS_IAMAX Function Parameters Parameter Description n Specifies the number of elements of the vectors x and y . n must be at least zero. x UTL_NLA_ARRAY_FLT / DBL of DIMENSION at least ( 1 + ( n - 1 )*abs( incx ) ) incx Specifies the increment for the elements of x . incx must not be zero.