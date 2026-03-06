---
id: 19c__UTL_NLA.BLAS_SYR2
name: UTL_NLA.BLAS_SYR2
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_SYR2

This procedure performs the rank 2 operation A := alpha*x*y' + alpha*y*x' + A , where alpha is a scalar, x and y are n element vectors, and A is an n by n symmetric matrix.

## Syntax

```sql
UTL_NLA.BLAS_SYR2 (
   uplo   IN      flag,
   n      IN      POSITIVEN,
   alpha  IN      SCALAR_DBL,
   x      IN      UTL_NLA_ARRAY_DBL,
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
| uplo | flag | IN | Specifies whether the upper or lower triangular part of the array A is to be referenced: uplo = 'U' or 'u' : Only the upper triangular part of A is to be referenced. uplo = 'L' or 'l' : Only the lower triangular part of A is to be referenced. |
| n | POSITIVEN | IN | Specifies the order of the matrix A . n must be at least zero. |
| alpha | SCALAR_DBL | IN | Specifies the scalar alpha. |
| x | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 )*abs( incx ) ) Before entry, the incremented array X must contain the m element vector x . |
| incx | POSITIVEN | IN | Specifies the increment for the elements of x . incx must not be zero. |
| y | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 )*abs( incy ) ) Before entry, the incremented array Y must contain the m element vector y . |
| incy | POSITIVEN | IN | Specifies the increment for the elements of y . incy must not be zero. |
| a | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda, n) With uplo = 'U' or 'u' , the leading n by n upper triangular part of the array A must contain the upper triangular part of the symmetric matrix and the strictly lower triangular part of A is not referenced. On exit, the upper triangular part of the array A is overwritten by the upper triangular part of the updated matrix. With uplo = 'L' or 'l' , the leading n by n lower triangular part of the array A must contain the lower triangular part of the symmetric matrix and the strictly upper triangular part of A is not referenced. On exit, the lower triangular part of the array A is overwritten by the lower triangular part of the updated matrix. |
| lda | POSITIVEN | IN | Specifies the first dimension of a as declared in the calling (sub) program. lda must be at least max( 1, n ) |
| pack | flag | IN | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_SYR2 ( uplo IN flag, n IN POSITIVEN, alpha IN SCALAR_DBL, x IN UTL_NLA_ARRAY_DBL, incx IN POSITIVEN, y IN UTL_NLA_ARRAY_DBL, incy IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, pack IN flag DEFAULT 'C'); UTL_NLA.BLAS_SYR2 ( uplo IN flag, n IN POSITIVEN, alpha IN SCALAR_FLT, x IN UTL_NLA_ARRAY_FLT, incx IN POSITIVEN, y IN UTL_NLA_ARRAY_FLT, incy IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, pack IN flag DEFAULT 'C'); Parameters Table 271-28 BLAS_SYR2 Procedure Parameters Parameter Description uplo Specifies whether the upper or lower triangular part of the array A is to be referenced: uplo = 'U' or 'u' : Only the upper triangular part of A is to be referenced. uplo = 'L' or 'l' : Only the lower triangular part of A is to be referenced. n Specifies the order of the matrix A . n must be at least zero. alpha Specifies the scalar alpha. x UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 )*abs( incx ) ) Before entry, the incremented array X must contain the m element vector x . incx Specifies the increment for the elements of x . incx must not be zero. y UTL_NLA_ARRAY_FLT / DBL of dimension at least ( 1 + ( n - 1 )*abs( incy ) ) Before entry, the incremented array Y must contain the m element vector y . incy Specifies the increment for the elements of y . incy must not be zero. a UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda, n) With uplo = 'U' or 'u' , the leading n by n upper triangular part of the array A must contain the upper triangular part of the symmetric matrix and the strictly lower triangular part of A is not referenced. On exit, the upper triangular part of the array A is overwritten by the upper triangular part of the updated matrix. With uplo = 'L' or 'l' , the leading n by n lower triangular part of the array A must contain the lower triangular part of the symmetric matrix and the strictly upper triangular part of A is not referenced. On exit, the lower triangular part of the array A is overwritten by the lower triangular part of the updated matrix. lda Specifies the first dimension of a as declared in the calling (sub) program. lda must be at least max( 1, n ) pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major