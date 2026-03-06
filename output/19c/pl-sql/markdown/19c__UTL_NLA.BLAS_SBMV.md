---
id: 19c__UTL_NLA.BLAS_SBMV
name: UTL_NLA.BLAS_SBMV
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_SBMV

This procedure performs the matrix-vector operation y := alpha*A*x + beta*y , where alpha and beta are scalars, x and y are n element vectors and A is an n by n symmetric band matrix, with k super-diagonals.

## Syntax

```sql
UTL_NLA.BLAS_SBMV (
   uplo   IN      flag,
   n      IN      POSITIVEN,
   k      IN      NATURALN,
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
| uplo | flag | IN | Specifies whether the upper or lower triangular part of the band matrix A is being supplied: uplo = 'U' or 'u' . The upper triangular part of A is supplied. uplo = 'L' or 'l' . The lower triangular part of A is supplied. |
| n | POSITIVEN | IN | Specifies the order of the matrix A . n must be at least zero. |
| k | NATURALN | IN | Specifies the number of super-diagonals of the matrix A . k must satisfy 0 .le. k . |
| alpha | SCALAR_DOUBLE | IN | SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. |
| a | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda,n) . Before entry with uplo = 'U' or 'u' , the leading (k+1) by n part of the array A must contain the upper triangular band part of the symmetric matrix, supplied column by column, with the leading diagonal of the matrix in row (k+1) of the array, the first super-diagonal starting at position 2 in row k , and so on. The top left k by k triangle of the array A is not referenced. Before entry with uplo = 'L' or 'l' , the leading (k+1) by n part of the array A must contain the lower triangular band part of the symmetric matrix, supplied column by column, with the leading diagonal of the matrix in row 1 of the array, the first sub-diagonal starting at position 1 in row 2, and so on. The bottom right k by k triangle of the array A is not referenced. Unchanged on exit |
| lda | POSITIVEN | IN | Specifies the first dimension of a as declared in the calling (sub) program. lda must be at least (k + 1) . |
| x | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incx)) Before entry, the incremented array X must contain the n element vector x . |
| incx | POSITIVEN | IN | Specifies the increment for the elements of x . Must not be zero. |
| beta | SCALAR_DOUBLE | IN | SCALAR_FLOAT / DOUBLE . Specifies the scalar beta. |
| y | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incy)) Before entry, the incremented array Y must contain the n element vector y . On exit, Y is overwritten by the updated vector y . |
| incy | POSITIVEN | IN | Specifies the increment for the elements of y . Must not be zero. |
| pack | flag | IN | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_SBMV ( uplo IN flag, n IN POSITIVEN, k IN NATURALN, alpha IN SCALAR_DOUBLE, a IN UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, x IN UTL_NLA_ARRAY_DBL, incx IN POSITIVEN, beta IN SCALAR_DOUBLE, y IN OUT UTL_NLA_ARRAY_DBL, incy IN POSITIVEN, pack IN flag DEFAULT 'C'); UTL_NLA.BLAS_SBMV ( uplo IN flag, n IN POSITIVEN, k IN NATURALN, alpha IN SCALAR_FLOAT, a IN UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, x IN UTL_NLA_ARRAY_FLT, incx IN POSITIVEN, beta IN SCALAR_FLOAT, y IN OUT UTL_NLA_ARRAY_FLT, incy IN POSITIVEN, pack IN flag DEFAULT 'C'); Parameters Table 271-23 BLAS_SBMV Procedure Parameters Parameter Description uplo Specifies whether the upper or lower triangular part of the band matrix A is being supplied: uplo = 'U' or 'u' . The upper triangular part of A is supplied. uplo = 'L' or 'l' . The lower triangular part of A is supplied. n Specifies the order of the matrix A . n must be at least zero. k Specifies the number of super-diagonals of the matrix A . k must satisfy 0 .le. k . alpha SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. a UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda,n) . Before entry with uplo = 'U' or 'u' , the leading (k+1) by n part of the array A must contain the upper triangular band part of the symmetric matrix, supplied column by column, with the leading diagonal of the matrix in row (k+1) of the array, the first super-diagonal starting at position 2 in row k , and so on. The top left k by k triangle of the array A is not referenced. Before entry with uplo = 'L' or 'l' , the leading (k+1) by n part of the array A must contain the lower triangular band part of the symmetric matrix, supplied column by column, with the leading diagonal of the matrix in row 1 of the array, the first sub-diagonal starting at position 1 in row 2, and so on. The bottom right k by k triangle of the array A is not referenced. Unchanged on exit lda Specifies the first dimension of a as declared in the calling (sub) program. lda must be at least (k + 1) . x UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incx)) Before entry, the incremented array X must contain the n element vector x . incx Specifies the increment for the elements of x . Must not be zero. beta SCALAR_FLOAT / DOUBLE . Specifies the scalar beta. y UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incy)) Before entry, the incremented array Y must contain the n element vector y . On exit, Y is overwritten by the updated vector y . incy Specifies the increment for the elements of y . Must not be zero. pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major