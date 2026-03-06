---
id: 19c__UTL_NLA.BLAS_SWAP
name: UTL_NLA.BLAS_SWAP
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_SWAP

This procedure swaps the contents of two vectors each of size n.

## Syntax

```sql
UTL_NLA.BLAS_SWAP (
   n     IN     POSITIVEN,
   x     IN OUT UTL_NLA_ARRAY_DBL,
   incx  IN     POSITIVEN,
   y     IN OUT UTL_NLA_ARRAY_DBL,
   incy  IN     POSITIVEN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | POSITIVEN | IN | Specifies the number of elements of the vectors x and y . n must be at least zero. |
| x | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incx)) |
| incx | POSITIVEN | IN | Specifies the increment for the elements of x . incx must not be zero. |
| y | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of DIMENSION at least (1+(n-1)*abs(incy)) |
| incy | POSITIVEN) | IN | Specifies the increment for the elements of y . incy must not be zero. |

## Usage Notes

Syntax UTL_NLA.BLAS_SWAP ( n IN POSITIVEN, x IN OUT UTL_NLA_ARRAY_DBL, incx IN POSITIVEN, y IN OUT UTL_NLA_ARRAY_DBL, incy IN POSITIVEN); UTL_NLA.BLAS_SWAP ( n IN POSITIVEN, x IN OUT UTL_NLA_ARRAY_FLT, incx IN POSITIVEN, y IN OUT UTL_NLA_ARRAY_FLT, incy IN POSITIVEN); Parameters Table 271-24 BLAS_SWAP Procedure Parameters Parameter Description n Specifies the number of elements of the vectors x and y . n must be at least zero. x UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incx)) incx Specifies the increment for the elements of x . incx must not be zero. y UTL_NLA_ARRAY_FLT / DBL of DIMENSION at least (1+(n-1)*abs(incy)) incy Specifies the increment for the elements of y . incy must not be zero.