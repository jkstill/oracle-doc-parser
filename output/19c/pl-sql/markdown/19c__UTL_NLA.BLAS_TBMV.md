---
id: 19c__UTL_NLA.BLAS_TBMV
name: UTL_NLA.BLAS_TBMV
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_TBMV

This procedure performs the matrix-vector operations x := A*x or x := A'*x , where x is an n element vector and A is an n by n unit, or non-unit, upper or lower triangular band matrix, with (k+1) diagonals.

## Syntax

```sql
UTL_NLA.BLAS_TBMV (
   uplo   IN      flag,
   trans  IN      flag,
   diag   IN      flag,
   n      IN      POSITIVEN,
   k      IN      NATURALN,
   a      IN      UTL_NLA_ARRAY_DBL,
   lda    IN      POSITIVEN,
   x      IN OUT  UTL_NLA_ARRAY_DBL,
   incx   IN      POSITIVEN,
   pack   IN      flag DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| uplo | flag | IN | Specifies whether the matrix is an upper or lower triangular matrix: uplo = 'U' or 'u' . A is an upper triangular matrix. uplo = 'L' or 'l' . A is a lower triangular matrix. |
| trans | flag | IN | Specifies the operation to be performed: trans = 'N' or 'n' x := A *x trans = 'T' or 't'x := A'*x trans = 'C' or 'c'x := A'*x |
| diag | flag | IN | Specifies whether or not A is unit triangular: diag = 'U' or 'u' . A is assumed to be unit triangular. diag = 'N' or 'n' . A is not assumed to be unit triangular. |
| n | POSITIVEN | IN | Specifies the order of the matrix A . n must be at least zero. |
| k | NATURALN | IN | Specifies whether or not A is unit triangular: with uplo = 'U' or 'u' , K specifies the number of super-diagonals of the matrix A . with uplo = 'L' or 'l' , K specifies the number of sub-diagonals of the matrix A . K must satisfy 0 .le. k . |
| a | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of DIMENSION ( lda , n ). Before entry with uplo = 'U' or 'u' , the leading (k+1) by n part of the array A must contain the upper triangular band part of the matrix of coefficients, supplied column by column, with the leading diagonal of the matrix in row (k+1) of the array, the first super-diagonal starting at position 2 in row k , and so on. The top left k by k triangle of the array A is not referenced. Before entry with uplo = 'L' or 'l' , the leading (k+1) by n part of the array A must contain the lower triangular band part of the matrix of coefficients, supplied column by column, with the leading diagonal of the matrix in row 1 of the array, the first sub-diagonal starting at position 1 in row 2, and so on. The bottom right k by k triangle of the array A is not referenced. Note that when diag = ' 'U' or 'u' , the elements of the array A corresponding to the diagonal elements of the matrix are not referenced, but are assumed to be unity. |
| lda | POSITIVEN | IN | Specifies the first dimension of a as declared in the calling (sub) program. lda must be at least (k+1) . |
| x | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incx)) . Before entry, the incremented array X must contain the n element vector x . On exit, X is overwritten with the transformed vector x . |
| incx | POSITIVEN | IN | Specifies the increment for the elements of x . Must not be zero. |
| pack | flag | IN | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_TBMV ( uplo IN flag, trans IN flag, diag IN flag, n IN POSITIVEN, k IN NATURALN, a IN UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, x IN OUT UTL_NLA_ARRAY_DBL, incx IN POSITIVEN, pack IN flag DEFAULT 'C'); UTL_NLA.BLAS_TBMV ( uplo IN flag, trans IN flag, diag IN flag, n IN POSITIVEN, k IN NATURALN, a IN UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, x IN OUT UTL_NLA_ARRAY_FLT, incx IN POSITIVEN, pack IN flag DEFAULT 'C'); Parameters Table 271-31 BLAS_TBMV Procedure Parameters Parameter Description uplo Specifies whether the matrix is an upper or lower triangular matrix: uplo = 'U' or 'u' . A is an upper triangular matrix. uplo = 'L' or 'l' . A is a lower triangular matrix. trans Specifies the operation to be performed: trans = 'N' or 'n' x := A *x trans = 'T' or 't'x := A'*x trans = 'C' or 'c'x := A'*x diag Specifies whether or not A is unit triangular: diag = 'U' or 'u' . A is assumed to be unit triangular. diag = 'N' or 'n' . A is not assumed to be unit triangular. n Specifies the order of the matrix A . n must be at least zero. k Specifies whether or not A is unit triangular: with uplo = 'U' or 'u' , K specifies the number of super-diagonals of the matrix A . with uplo = 'L' or 'l' , K specifies the number of sub-diagonals of the matrix A . K must satisfy 0 .le. k . a UTL_NLA_ARRAY_FLT / DBL of DIMENSION ( lda , n ). Before entry with uplo = 'U' or 'u' , the leading (k+1) by n part of the array A must contain the upper triangular band part of the matrix of coefficients, supplied column by column, with the leading diagonal of the matrix in row (k+1) of the array, the first super-diagonal starting at position 2 in row k , and so on. The top left k by k triangle of the array A is not referenced. Before entry with uplo = 'L' or 'l' , the leading (k+1) by n part of the array A must contain the lower triangular band part of the matrix of coefficients, supplied column by column, with the leading diagonal of the matrix in row 1 of the array, the first sub-diagonal starting at position 1 in row 2, and so on. The bottom right k by k triangle of the array A is not referenced. Note that when diag = ' 'U' or 'u' , the elements of the array A corresponding to the diagonal elements of the matrix are not referenced, but are assumed to be unity. lda Specifies the first dimension of a as declared in the calling (sub) program. lda must be at least (k+1) . x UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incx)) . Before entry, the incremented array X must contain the n element vector x . On exit, X is overwritten with the transformed vector x . incx Specifies the increment for the elements of x . Must not be zero. pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major