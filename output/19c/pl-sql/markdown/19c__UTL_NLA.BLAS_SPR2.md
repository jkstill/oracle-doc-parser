---
id: 19c__UTL_NLA.BLAS_SPR2
name: UTL_NLA.BLAS_SPR2
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_SPR2

This procedure performs the rank 2 operation A := alpha*x*y' + alpha*y*x' +A , where alpha is a scalar, x and y are n element vectors, and A is an n by n symmetric matrix, supplied in packed form.

## Syntax

```sql
UTL_NLA.BLAS_SPR2 (
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
| uplo | flag | IN | Specifies whether the upper or lower triangular part of the matrix A is supplied in the packed array ap : uplo = 'U' or 'u' : The upper triangular part of A is supplied in ap . uplo = 'L' or 'l' : The lower triangular part of A is supplied in ap . |
| n | POSITIVEN | IN | Specifies the order of the matrix A . n must be at least zero. |
| alpha | SCALAR_DBL | IN | Specifies the scalar alpha. |
| x | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incx)) Before entry, the incremented array X must contain the m element vector x . |
| incx | POSITIVEN | IN | Specifies the increment for the elements of x . incx must not be zero. |
| y | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incy)) Before entry, the incremented array X must contain the m element vector y . |
| incy | POSITIVEN | IN | Specifies the increment for the elements of y . incy must not be zero. |
| ap |  |  | UTL_NLA_ARRAY_FLT / DBL of dimension at least ((n*(n+1))/2) Before entry with uplo = 'U' or 'u' , the array ap must contain the upper triangular part of the symmetric matrix packed sequentially, column by column, so that ap(1) contains ap(1) contains a(1,1) , ap(2) and ap(3) contain a(1,2) and a(2,2) respectively, and so on. On exit, the array ap is overwritten by the upper triangular part of the updated matrix. Before entry with uplo = 'L' or 'l' , the array ap must contain the lower triangular part of the symmetric matrix packed sequentially, column by column, so that ap(1) contains a(1,1) , ap(2) and ap(3) contain a(2,1) and a(3,1) respectively, and so on. On exit, the array ap is overwritten by the lower triangular part of the updated matrix |
| lda | POSITIVEN | IN | Specifies the first dimension of a as declared in the calling (sub) program. lda must be at least (k + 1) . |
| pack | flag | IN | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_SPR2 ( uplo IN flag, n IN POSITIVEN, alpha IN SCALAR_DBL, x IN UTL_NLA_ARRAY_DBL, incx IN POSITIVEN, y IN UTL_NLA_ARRAY_DBL, incy IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, pack IN flag DEFAULT 'C'); UTL_NLA.BLAS_SPR2 ( uplo IN flag, n IN POSITIVEN, alpha IN SCALAR_FLT, x IN UTL_NLA_ARRAY_FLT, incx IN POSITIVEN, y IN UTL_NLA_ARRAY_FLT, incy IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, pack IN flag DEFAULT 'C'); Parameters Table 271-22 BLAS_SPR2 Procedure Parameters Parameter Description uplo Specifies whether the upper or lower triangular part of the matrix A is supplied in the packed array ap : uplo = 'U' or 'u' : The upper triangular part of A is supplied in ap . uplo = 'L' or 'l' : The lower triangular part of A is supplied in ap . n Specifies the order of the matrix A . n must be at least zero. alpha Specifies the scalar alpha. x UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incx)) Before entry, the incremented array X must contain the m element vector x . incx Specifies the increment for the elements of x . incx must not be zero. y UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incy)) Before entry, the incremented array X must contain the m element vector y . incy Specifies the increment for the elements of y . incy must not be zero. ap UTL_NLA_ARRAY_FLT / DBL of dimension at least ((n*(n+1))/2) Before entry with uplo = 'U' or 'u' , the array ap must contain the upper triangular part of the symmetric matrix packed sequentially, column by column, so that ap(1) contains ap(1) contains a(1,1) , ap(2) and ap(3) contain a(1,2) and a(2,2) respectively, and so on. On exit, the array ap is overwritten by the upper triangular part of the updated matrix. Before entry with uplo = 'L' or 'l' , the array ap must contain the lower triangular part of the symmetric matrix packed sequentially, column by column, so that ap(1) contains a(1,1) , ap(2) and ap(3) contain a(2,1) and a(3,1) respectively, and so on. On exit, the array ap is overwritten by the lower triangular part of the updated matrix lda Specifies the first dimension of a as declared in the calling (sub) program. lda must be at least (k + 1) . pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major