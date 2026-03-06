---
id: 19c__UTL_NLA.BLAS_ROT
name: UTL_NLA.BLAS_ROT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_ROT

This procedure returns the plane rotation of points.

## Syntax

```sql
UTL_NLA.BLAS_ROT (
   n      IN      POSITIVEN,
   x      IN OUT  UTL_NLA_ARRAY_DBL,
   incx   IN      POSITIVEN,
   y      IN OUT  UTL_NLA_ARRAY_DBL,
   incy   IN      POSITIVEN,
   c      IN      SCALAR_DOUBLE,
   s      IN      SCALAR_DOUBLE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | POSITIVEN | IN | Specifies the number of elements of the vectors x and y . n must be at least zero. |
| x | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)* abs(incx)) |
| incx | POSITIVEN | IN | Specifies the increment for the elements of x . incx must not be zero. |
| y | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of DIMENSION at least (1+(n-1)*abs(incy)) |
| incy | POSITIVEN | IN | Specifies the increment for the elements of y . incy must not be zero. |
| c | SCALAR_DOUBLE | IN | SCALAR_FLOAT / DOUBLE .Specifies the scalar C. |
| s | SCALAR_DOUBLE) | IN | SCALAR_FLOAT / DOUBLE .Specifies the scalar S. |

## Usage Notes

See Also: BLAS Level 1 (Vector-Vector Operations) Subprograms for other subprograms in this group See Also: BLAS Level 1 (Vector-Vector Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_ROT ( n IN POSITIVEN, x IN OUT UTL_NLA_ARRAY_DBL, incx IN POSITIVEN, y IN OUT UTL_NLA_ARRAY_DBL, incy IN POSITIVEN, c IN SCALAR_DOUBLE, s IN SCALAR_DOUBLE); UTL_NLA.BLAS_ROT ( n IN POSITIVEN, x IN OUT UTL_NLA_ARRAY_FLT, incx IN POSITIVEN, y IN OUT UTL_NLA_ARRAY_FLT, incy IN POSITIVEN, c IN SCALAR_DOUBLE, s IN SCALAR_DOUBLE); Parameters Table 271-17 BLAS_ROT Procedure Parameters Parameter Description n Specifies the number of elements of the vectors x and y . n must be at least zero. x UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)* abs(incx)) incx Specifies the increment for the elements of x . incx must not be zero. y UTL_NLA_ARRAY_FLT / DBL of DIMENSION at least (1+(n-1)*abs(incy)) incy Specifies the increment for the elements of y . incy must not be zero. c SCALAR_FLOAT / DOUBLE .Specifies the scalar C. s SCALAR_FLOAT / DOUBLE .Specifies the scalar S.