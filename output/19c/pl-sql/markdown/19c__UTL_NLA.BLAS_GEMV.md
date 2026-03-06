---
id: 19c__UTL_NLA.BLAS_GEMV
name: UTL_NLA.BLAS_GEMV
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_GEMV

This procedure performs one of the matrix-vector operations: y := alpha*A*x + beta*y or y := alpha*A'*x + beta*y where alpha and beta are scalars, x and y are vectors and A is an m by n matrix.

## Syntax

```sql
UTL_NLA.BLAS_GEMV (
   trans  IN      flag,
   m      IN      POSITIVEN,
   n      IN      POSITIVEN,
   alpha  IN      SCALAR_DOUBLE,
   a      IN      UTL_NLA_ARRAY_DBL,
   lda    IN      POSITIVEN,
   x      IN      UTL_NLA_ARRAY_DBL,
   incx   IN      POSITIVEN,
   beta   IN      SCALAR_DOUBLE,
   y      IN OUT  UTL_NLA_ARRAY_DBL,
   incy   IN      POSITIVEN,
   pack   IN      flag DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| trans | flag | IN | Specifies the operation to be performed: trans = 'N' or 'n' , y := alpha * A * x + beta * y trans = 'T' or 't' y := alpha * A '* x + beta * y trans = ' C ' or ' c ' y := alpha * A '* x + beta * y |
| m | POSITIVEN | IN | Specifies the number of rows of the matrix A. m must be at least zero. |
| n | POSITIVEN | IN | Specifies the number of columns of the matrix A. n must be at least zero. |
| alpha | SCALAR_DOUBLE | IN | SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. |
| a | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda, n ). Before entry, the leading m by n part of the array a must contain the matrix of coefficients. |
| lda | POSITIVEN | IN | Specifies the first dimension of a as declared in the calling (sub) program. lda must be at least max (1, m ). |
| x | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 )*abs( incx ) ) when trans = ' 'N' or 'n' and at least (1+(m-1)*abs(incx)) otherwise. Before entry, the incremented array X must contain the vector x . |
| incx | POSITIVEN | IN | Specifies the increment for the elements of x . Must not be zero. |
| beta | SCALAR_DOUBLE | IN | SCALAR_FLOAT / DOUBLE . Specifies the scalar beta. When beta is supplied as zero then y need not be set on input. |
| y | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( m - 1 )*abs( incy ) ) when trans = 'N' or 'n' and at least ( 1 + ( n - 1 )*abs( incy ) ) otherwise. Before entry with beta nonzero, the incremented array Y must contain the vector y . On exit, Y is overwritten by the updated vector y . |
| incy | POSITIVEN | IN | Specifies the increment for the elements of y . Must not be zero. |
| pack | flag | IN | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_GEMV ( trans IN flag, m IN POSITIVEN, n IN POSITIVEN, alpha IN SCALAR_DOUBLE, a IN UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, x IN UTL_NLA_ARRAY_DBL, incx IN POSITIVEN, beta IN SCALAR_DOUBLE, y IN OUT UTL_NLA_ARRAY_DBL, incy IN POSITIVEN, pack IN flag DEFAULT 'C'); UTL_NLA.BLAS_GEMV ( trans IN flag, m IN POSITIVEN, n IN POSITIVEN, alpha IN SCALAR_FLOAT, a IN UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, x IN UTL_NLA_ARRAY_FLT, incx IN POSITIVEN, beta IN SCALAR_FLOAT, y IN OUT UTL_NLA_ARRAY_FLT, incy IN POSITIVEN, pack IN flag DEFAULT 'C'); Parameters Table 271-13 BLAS_GEMV Procedure Parameters Parameter Description trans Specifies the operation to be performed: trans = 'N' or 'n' , y := alpha * A * x + beta * y trans = 'T' or 't' y := alpha * A '* x + beta * y trans = ' C ' or ' c ' y := alpha * A '* x + beta * y m Specifies the number of rows of the matrix A. m must be at least zero. n Specifies the number of columns of the matrix A. n must be at least zero. alpha SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. a UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda, n ). Before entry, the leading m by n part of the array a must contain the matrix of coefficients. lda Specifies the first dimension of a as declared in the calling (sub) program. lda must be at least max (1, m ). x UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 )*abs( incx ) ) when trans = ' 'N' or 'n' and at least (1+(m-1)*abs(incx)) otherwise. Before entry, the incremented array X must contain the vector x . incx Specifies the increment for the elements of x . Must not be zero. beta SCALAR_FLOAT / DOUBLE . Specifies the scalar beta. When beta is supplied as zero then y need not be set on input. y UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( m - 1 )*abs( incy ) ) when trans = 'N' or 'n' and at least ( 1 + ( n - 1 )*abs( incy ) ) otherwise. Before entry with beta nonzero, the incremented array Y must contain the vector y . On exit, Y is overwritten by the updated vector y . incy Specifies the increment for the elements of y . Must not be zero. pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major