---
id: 19c__UTL_NLA.BLAS_COPY
name: UTL_NLA.BLAS_COPY
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_COPY

This procedure copies the contents of vector X to vector Y .

## Syntax

```sql
UTL_NLA.BLAS_COPY (
   n     IN     POSITIVEN,
   x     IN     UTL_NLA_ARRAY_DBL,
   incx  IN     POSITIVEN,
   y     IN OUT UTL_NLA_ARRAY_DBL,
   incy  IN     POSITIVEN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | POSITIVEN | IN | Specifies the number of elements of the vectors x and y . n must be at least zero. |
| x | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 )*abs( incx ) ) |
| incx | POSITIVEN | IN | Specifies the increment for the elements of x . incx must not be zero. |
| y | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 )*abs( incy) ) |
| incy | POSITIVEN) | IN | Specifies the increment for the elements of y . incy must not be zero. |

## Usage Notes

See Also: BLAS Level 1 (Vector-Vector Operations) Subprograms for other subprograms in this group See Also: BLAS Level 1 (Vector-Vector Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_COPY ( n IN POSITIVEN, x IN UTL_NLA_ARRAY_DBL, incx IN POSITIVEN, y IN OUT UTL_NLA_ARRAY_DBL, incy IN POSITIVEN); UTL_NLA.BLAS_COPY ( n IN POSITIVEN, x IN UTL_NLA_ARRAY_FLT, incx IN POSITIVEN, y IN OUT UTL_NLA_ARRAY_FLT, incy IN POSITIVEN); Parameters Table 271-9 BLAS_COPY Procedure Parameters Parameter Description n Specifies the number of elements of the vectors x and y . n must be at least zero. x UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 )*abs( incx ) ) incx Specifies the increment for the elements of x . incx must not be zero. y UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 )*abs( incy) ) incy Specifies the increment for the elements of y . incy must not be zero.