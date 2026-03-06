---
id: 19c__UTL_NLA.BLAS_SCAL
name: UTL_NLA.BLAS_SCAL
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_SCAL

This procedure scales a vector by a constant.

## Syntax

```sql
UTL_NLA.BLAS_SCAL (
   n      IN  POSITIVEN,
   alpha  IN  SCALAR_DOUBLE,
   x      IN  OUT UTL_NLA_ARRAY_DBL,
   incx   IN  POSITIVEN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | POSITIVEN | IN | Specifies the number of elements of the vectors x and y . n must be at least zero. |
| alpha | SCALAR_DOUBLE | IN | Specifies the scalar alpha. |
| x | UTL_NLA_ARRAY_DBL | IN  OUT | UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incx)) |
| incx | POSITIVEN) | IN | Specifies the increment for the elements of x . incx must not be zero. |

## Usage Notes

See Also: BLAS Level 1 (Vector-Vector Operations) Subprograms for other subprograms in this group See Also: BLAS Level 1 (Vector-Vector Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_SCAL ( n IN POSITIVEN, alpha IN SCALAR_DOUBLE, x IN OUT UTL_NLA_ARRAY_DBL, incx IN POSITIVEN); UTL_NLA.BLAS_SCAL ( n IN POSITIVEN, alpha IN SCALAR_FLOAT, x IN OUT UTL_NLA_ARRAY_FLT, incx IN POSITIVEN); Parameters Table 271-19 BLAS_SCAL Procedure Parameters Parameter Description n Specifies the number of elements of the vectors x and y . n must be at least zero. alpha Specifies the scalar alpha. x UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incx)) incx Specifies the increment for the elements of x . incx must not be zero.