---
id: 19c__UTL_NLA.BLAS_SPMV
name: UTL_NLA.BLAS_SPMV
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_SPMV

This procedure performs the matrix-vector operation y := alpha*A*x + beta*y , where alpha and beta are scalars, x and y are n element vectors and A is an n by n symmetric matrix, supplied in packed form.

## Syntax

```sql
UTL_NLA.BLAS_SPMV (
   uplo   IN      flag,
   n      IN      POSITIVEN,
   alpha  IN      SCALAR_DOUBLE,
   ap     IN      UTL_NLA_ARRAY_DBL,
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
| uplo | flag | IN | Specifies the upper or lower triangular part of the matrix A is supplied in the packed array AP : uplo = 'U' or 'u' . The upper triangular part of A is supplied in AP . uplo = 'L' or 'l' . The lower triangular part of A is supplied in AP . |
| n | POSITIVEN | IN | Specifies the order of the matrix A . n must be at least zero. |
| alpha | SCALAR_DOUBLE | IN | SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. |
| ap | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of dimension at least ((n*(n+1))/2) Before entry with uplo = 'U' or 'u' , the array ap must contain the upper triangular part of the symmetric matrix packed sequentially, column by column, so that ap(1) contains a(1,1) , ap(2) and ap(3) contain a(1,2) and a(2,2) respectively, and so on. Before entry with uplo = 'L' or 'l' , the array ap must contain the lower triangular part of the symmetric matrix packed sequentially, column by column, so that ap(1) contains, ap(2) and ap(3) contain a(2,1) and a(3,1) respectively, and so on. |
| x | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incx)) Before entry, the incremented array X must contain the n element vector x . |
| incx | POSITIVEN | IN | Specifies the increment for the elements of x . Must not be zero. |
| beta | SCALAR_DOUBLE | IN | SCALAR_FLOAT / DOUBLE . Specifies the scalar beta. When beta is supplied as zero then Y need not be set on input. |
| y | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of dimension at leasT (1+( n -1)*abs(incy)) Before entry, the incremented array Y must contain the n element vector y . On exit, Y is overwritten by the updated vector y . |
| incy | POSITIVEN | IN | Specifies the increment for the elements of y . Must not be zero. |
| pack | flag | IN | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_SPMV ( uplo IN flag, n IN POSITIVEN, alpha IN SCALAR_DOUBLE, ap IN UTL_NLA_ARRAY_DBL, x IN UTL_NLA_ARRAY_DBL, incx IN POSITIVEN, beta IN SCALAR_DOUBLE, y IN OUT UTL_NLA_ARRAY_DBL, incy IN POSITIVEN, pack IN flag DEFAULT 'C'); UTL_NLA.BLAS_SPMV ( uplo IN flag, n IN POSITIVEN, alpha IN SCALAR_FLOAT, ap IN UTL_NLA_ARRAY_FLT, x IN UTL_NLA_ARRAY_FLT, incx IN POSITIVEN, beta IN SCALAR_FLOAT, y IN OUT UTL_NLA_ARRAY_FLT, incy IN POSITIVEN, pack IN flag DEFAULT 'C'); Parameters Table 271-20 BLAS_SPMV Procedure Parameters Parameter Description uplo Specifies the upper or lower triangular part of the matrix A is supplied in the packed array AP : uplo = 'U' or 'u' . The upper triangular part of A is supplied in AP . uplo = 'L' or 'l' . The lower triangular part of A is supplied in AP . n Specifies the order of the matrix A . n must be at least zero. alpha SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. ap UTL_NLA_ARRAY_FLT / DBL of dimension at least ((n*(n+1))/2) Before entry with uplo = 'U' or 'u' , the array ap must contain the upper triangular part of the symmetric matrix packed sequentially, column by column, so that ap(1) contains a(1,1) , ap(2) and ap(3) contain a(1,2) and a(2,2) respectively, and so on. Before entry with uplo = 'L' or 'l' , the array ap must contain the lower triangular part of the symmetric matrix packed sequentially, column by column, so that ap(1) contains, ap(2) and ap(3) contain a(2,1) and a(3,1) respectively, and so on. x UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incx)) Before entry, the incremented array X must contain the n element vector x . incx Specifies the increment for the elements of x . Must not be zero. beta SCALAR_FLOAT / DOUBLE . Specifies the scalar beta. When beta is supplied as zero then Y need not be set on input. y UTL_NLA_ARRAY_FLT / DBL of dimension at leasT (1+( n -1)*abs(incy)) Before entry, the incremented array Y must contain the n element vector y . On exit, Y is overwritten by the updated vector y . incy Specifies the increment for the elements of y . Must not be zero. pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major