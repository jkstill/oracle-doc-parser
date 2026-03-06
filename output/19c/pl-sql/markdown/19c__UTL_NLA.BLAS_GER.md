---
id: 19c__UTL_NLA.BLAS_GER
name: UTL_NLA.BLAS_GER
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_GER

This procedure performs the rank 1 operation: A := alpha*x*y' + A where alpha is a scalar, x is an m element vector, y is an n element vector and A is an m by n matrix.

## Syntax

```sql
UTL_NLA.BLAS_GER (
   m      IN      POSITIVEN,
   n      IN      POSITIVEN,
   alpha  IN      SCALAR_DBL,
   x      IN OUT  UTL_NLA_ARRAY_DBL,
   incx   IN      POSITIVEN,
   y      IN      UTL_NLA_ARRAY_DBL,
   incy   IN      POSITIVEN,
   a      IN OUT  UTL_NLA_ARRAY_DBL,
   lda    IN      POSITIVEN,
   pack   IN      flag DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| m | POSITIVEN | IN | Specifies the number of rows of the matrix A . m must be at least zero. |
| n | POSITIVEN | IN | Specifies the number of columns of the matrix A . n must be at least zero. |
| alpha | SCALAR_DBL | IN | Specifies the scalar alpha. |
| x | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( m - 1 )*abs( incx ) ) Before entry, the incremented array X must contain the m element vector x . |
| incx | POSITIVEN | IN | Specifies the increment for the elements of x . incx must not be zero. |
| y | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 )*abs( incy ) ) Before entry, the incremented array Y must contain the m element vector y. |
| incy | POSITIVEN | IN | Specifies the increment for the elements of y . incx must not be zero. |
| a | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of DIMENSION ( lda , n ). Before entry, the leading m by n part of the array a must contain the matrix of coefficients. On exit, a is overwritten by the updated matrix. |
| lda | POSITIVEN | IN | Specifies the first dimension of a as declared in the calling (sub) program. lda must be at least max( 1, m ) |
| pack | flag | IN | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_GER ( m IN POSITIVEN, n IN POSITIVEN, alpha IN SCALAR_DBL, x IN OUT UTL_NLA_ARRAY_DBL, incx IN POSITIVEN, y IN UTL_NLA_ARRAY_DBL, incy IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, pack IN flag DEFAULT 'C'); UTL_NLA.BLAS_GER ( m IN POSITIVEN, n IN POSITIVEN, alpha IN SCALAR_FLT, x IN OUT UTL_NLA_ARRAY_FLT, incx IN POSITIVEN, y IN UTL_NLA_ARRAY_FLT, incy IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, pack IN flag DEFAULT 'C'); Parameters Table 271-14 BLAS_GER Procedure Parameters Parameter Description m Specifies the number of rows of the matrix A . m must be at least zero. n Specifies the number of columns of the matrix A . n must be at least zero. alpha Specifies the scalar alpha. x UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( m - 1 )*abs( incx ) ) Before entry, the incremented array X must contain the m element vector x . incx Specifies the increment for the elements of x . incx must not be zero. y UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 )*abs( incy ) ) Before entry, the incremented array Y must contain the m element vector y. incy Specifies the increment for the elements of y . incx must not be zero. a UTL_NLA_ARRAY_FLT / DBL of DIMENSION ( lda , n ). Before entry, the leading m by n part of the array a must contain the matrix of coefficients. On exit, a is overwritten by the updated matrix. lda Specifies the first dimension of a as declared in the calling (sub) program. lda must be at least max( 1, m ) pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major