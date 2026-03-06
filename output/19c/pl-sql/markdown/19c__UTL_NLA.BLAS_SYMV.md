---
id: 19c__UTL_NLA.BLAS_SYMV
name: UTL_NLA.BLAS_SYMV
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_SYMV

This procedure performs the matrix-vector operation y := alpha*A*x + beta*y , where alpha and beta are scalars, x and y are n element vectors and A is an n by n symmetric matrix.

## Syntax

```sql
UTL_NLA.BLAS_SYMV (
   uplo   IN      flag,
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
| uplo | flag | IN | Specifies whether the upper or lower triangular part of the array A is to be referenced: uplo = 'U' or 'u' . Only the upper triangular part of A is to be referenced. uplo = 'L' or 'l' . Only the lower triangular part of A is to be referenced. |
| n | POSITIVEN | IN | Specifies the order of the matrix A . n must be at least zero. |
| alpha | SCALAR_DOUBLE | IN | SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. |
| a | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda,n) . Before entry with uplo = 'U' or 'u' , the leading n by n upper triangular part of the array A must contain the upper triangular part of the symmetric matrix and the strictly lower triangular part of A is not referenced. Before entry with uplo = 'L' or 'l' , the leading n by n lower triangular part of the array A must contain the lower triangular part of the symmetric matrix and the strictly upper triangular part of A is not referenced. |
| lda | POSITIVEN | IN | Specifies the first dimension of a as declared in the calling (sub) program. lda must be at least max(1,n) . |
| x | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incx)) Before entry, the incremented array X must contain the n element vector x . |
| incx | POSITIVEN | IN | Specifies the increment for the elements of x . Must not be zero. |
| beta | SCALAR_DOUBLE | IN | SCALAR_FLOAT / DOUBLE . Specifies the scalar beta. When beta is supplied as zero then y need not be set on input. |
| y | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incy)) Before entry, the incremented array Y must contain the n element vector y . On exit, Y is overwritten by the updated vector y . |
| incy | POSITIVEN | IN | Specifies the increment for the elements of y . Must not be zero. |
| pack | flag | IN | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_SYMV ( uplo IN flag, n IN POSITIVEN, alpha IN SCALAR_DOUBLE, a IN UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, x IN UTL_NLA_ARRAY_DBL, incx IN POSITIVEN, beta IN SCALAR_DOUBLE, y IN OUT UTL_NLA_ARRAY_DBL, incy IN POSITIVEN, pack IN flag DEFAULT 'C'); UTL_NLA.BLAS_SYMV ( uplo IN flag, n IN POSITIVEN, alpha IN SCALAR_FLOAT, a IN UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, x IN UTL_NLA_ARRAY_FLT, incx IN POSITIVEN, beta IN SCALAR_FLOAT, y IN OUT UTL_NLA_ARRAY_FLT, incy IN POSITIVEN, pack IN flag DEFAULT 'C'); Parameters Table 271-26 BLAS_SYMV Procedure Parameters Parameter Description uplo Specifies whether the upper or lower triangular part of the array A is to be referenced: uplo = 'U' or 'u' . Only the upper triangular part of A is to be referenced. uplo = 'L' or 'l' . Only the lower triangular part of A is to be referenced. n Specifies the order of the matrix A . n must be at least zero. alpha SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. a UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda,n) . Before entry with uplo = 'U' or 'u' , the leading n by n upper triangular part of the array A must contain the upper triangular part of the symmetric matrix and the strictly lower triangular part of A is not referenced. Before entry with uplo = 'L' or 'l' , the leading n by n lower triangular part of the array A must contain the lower triangular part of the symmetric matrix and the strictly upper triangular part of A is not referenced. lda Specifies the first dimension of a as declared in the calling (sub) program. lda must be at least max(1,n) . x UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incx)) Before entry, the incremented array X must contain the n element vector x . incx Specifies the increment for the elements of x . Must not be zero. beta SCALAR_FLOAT / DOUBLE . Specifies the scalar beta. When beta is supplied as zero then y need not be set on input. y UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incy)) Before entry, the incremented array Y must contain the n element vector y . On exit, Y is overwritten by the updated vector y . incy Specifies the increment for the elements of y . Must not be zero. pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major