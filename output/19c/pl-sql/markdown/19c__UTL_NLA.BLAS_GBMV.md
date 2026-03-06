---
id: 19c__UTL_NLA.BLAS_GBMV
name: UTL_NLA.BLAS_GBMV
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_GBMV

This procedure performs one of the matrix-vector operations y := alpha*A*x + beta*y or y := alpha*A'*x + beta*y , where alpha and beta are scalars, x and y are vectors and A is an m by n band matrix, with kl sub-diagonals and ku super-diagonals.

## Syntax

```sql
UTL_NLA.BLAS_GBMV (
   trans  IN      flag,
   m      IN      POSITIVEN,   n      IN      POSITIVEN,
   kl     IN      NATURALN,
   ku     IN      NATURALN,
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
| trans | flag | IN | Specifies the operation to be performed: trans = ' N ' or ' n ' y := alpha * A * x + beta * y trans = 'T' or 't' y := alpha * A '* x + beta * y trans = ' C ' or ' c ' y := alpha * A '* x + beta * y |
| m | POSITIVEN | IN | Specifies the number of rows of the matrix A. m must be at least zero. |
| n | POSITIVEN | IN | Specifies the number of columns of the matrix A. n must be at least zero. |
| kl | NATURALN | IN | Specifies the number of sub-diagonals of the matrix A . kl must satisfy 0. le. kl . |
| ku | NATURALN | IN | Specifies the number of super-diagonals of the matrix A . ku must satisfy 0 .le. ku . |
| alpha | SCALAR_DOUBLE | IN | SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. |
| a | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda,n) . Before entry, the leading (kl + ku + 1) by n part of the array A must contain the matrix of coefficients, supplied column by column, with the leading diagonal of the matrix in row (ku+1) of the array, the first super-diagonal starting at position 2 in row ku , the first sub-diagonal starting at position 1 in row (ku+2) , and so on. Elements in the array A that do not correspond to elements in the band matrix (such as the top left ku by ku triangle) are not referenced. |
| lda | POSITIVEN | IN | Specifies the first dimension of a as declared in the calling (sub) program. lda must be at least (kl+ku+1) . |
| x | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 )*abs( incx ) ) when trans = ' 'N' or 'n' and at least ( 1 + ( m - 1 )*abs( incx ) ) otherwise. Before entry, the incremented array X must contain the vector x . |
| incx | POSITIVEN | IN | Specifies the increment for the elements of x . Must not be zero. |
| beta | SCALAR_DOUBLE | IN | SCALAR_FLOAT / DOUBLE . Specifies the scalar beta. When beta is supplied as zero then y need not be set on input. |
| y | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( m - 1 )*abs( incy ) ) when trans = 'N' or 'n' and at least (1+(n-1)*abs(incy)) otherwise. Before entry with beta nonzero, the incremented array Y must contain the vector y . On exit, Y is overwritten by the updated vector y . |
| incy | POSITIVEN | IN | Specifies the increment for the elements of y . Must not be zero. |
| pack | flag | IN | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_GBMV ( trans IN flag, m IN POSITIVEN, n IN POSITIVEN, kl IN NATURALN, ku IN NATURALN, alpha IN SCALAR_DOUBLE, a IN UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, x IN UTL_NLA_ARRAY_DBL, incx IN POSITIVEN, beta IN SCALAR_DOUBLE, y IN OUT UTL_NLA_ARRAY_DBL, incy IN POSITIVEN, pack IN flag DEFAULT 'C'); UTL_NLA.BLAS_GBMV ( trans IN flag, m IN POSITIVEN, n IN POSITIVEN, kl IN NATURALN, ku IN NATURALN, alpha IN SCALAR_FLOAT, a IN UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, x IN UTL_NLA_ARRAY_FLT, incx IN POSITIVEN, beta IN SCALAR_FLOAT, y IN OUT UTL_NLA_ARRAY_FLT, incy IN POSITIVEN, pack IN flag DEFAULT 'C'); Parameters Table 271-11 BLAS_GBMV Procedure Parameters Parameter Description trans Specifies the operation to be performed: trans = ' N ' or ' n ' y := alpha * A * x + beta * y trans = 'T' or 't' y := alpha * A '* x + beta * y trans = ' C ' or ' c ' y := alpha * A '* x + beta * y m Specifies the number of rows of the matrix A. m must be at least zero. n Specifies the number of columns of the matrix A. n must be at least zero. kl Specifies the number of sub-diagonals of the matrix A . kl must satisfy 0. le. kl . ku Specifies the number of super-diagonals of the matrix A . ku must satisfy 0 .le. ku . alpha SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. a UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda,n) . Before entry, the leading (kl + ku + 1) by n part of the array A must contain the matrix of coefficients, supplied column by column, with the leading diagonal of the matrix in row (ku+1) of the array, the first super-diagonal starting at position 2 in row ku , the first sub-diagonal starting at position 1 in row (ku+2) , and so on. Elements in the array A that do not correspond to elements in the band matrix (such as the top left ku by ku triangle) are not referenced. lda Specifies the first dimension of a as declared in the calling (sub) program. lda must be at least (kl+ku+1) . x UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 )*abs( incx ) ) when trans = ' 'N' or 'n' and at least ( 1 + ( m - 1 )*abs( incx ) ) otherwise. Before entry, the incremented array X must contain the vector x . incx Specifies the increment for the elements of x . Must not be zero. beta SCALAR_FLOAT / DOUBLE . Specifies the scalar beta. When beta is supplied as zero then y need not be set on input. y UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( m - 1 )*abs( incy ) ) when trans = 'N' or 'n' and at least (1+(n-1)*abs(incy)) otherwise. Before entry with beta nonzero, the incremented array Y must contain the vector y . On exit, Y is overwritten by the updated vector y . incy Specifies the increment for the elements of y . Must not be zero. pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major