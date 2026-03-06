---
id: 19c__UTL_NLA.BLAS_SPR
name: UTL_NLA.BLAS_SPR
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_SPR

This procedure performs the rank 1 operation A := alpha*x*x' + A , where alpha is a real scalar, x is an n element vector, and A is an n by n symmetric matrix, supplied in packed form.

## Syntax

```sql
UTL_NLA.BLAS_SPR (
   uplo   IN      flag,
   n      IN      POSITIVEN,
   alpha  IN      SCALAR_DBL,
   x      IN OUT  UTL_NLA_ARRAY_DBL,
   incx   IN      POSITIVEN,
   ap     IN OUT  UTL_NLA_ARRAY_DBL,
   pack   IN      flag DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| uplo | flag | IN | Specifies whether the upper or lower triangular part of the matrix A is supplied in the packed array ap : uplo = 'U' or 'u' : The upper triangular part of A is supplied in ap . uplo = 'L' or 'l' : The lower triangular part of A is supplied in ap . |
| n | POSITIVEN | IN | Specifies the order of the matrix A . n must be at least zero. |
| alpha | SCALAR_DBL | IN | Specifies the scalar alpha. |
| x | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incx)) Before entry, the incremented array X must contain the m element vector x . |
| incx | POSITIVEN | IN | Specifies the increment for the elements of x . incx must not be zero. |
| a p |  |  | UTL_NLA_ARRAY_FLT / DBL of dimension at least ((n*(n +1))/2) Before entry with uplo = 'U' or 'u' , the array ap must contain the upper triangular part of the symmetric matrix packed sequentially, column by column, so that ap(1) contains a(1,1) , ap(2) and ap(3) contain a(1,2) and a(2,2) respectively, and so on. On exit, the array ap is overwritten by the upper triangular part of the updated matrix. Before entry with uplo = 'L' or 'l' , the array ap must contain the lower triangular part of the symmetric matrix packed sequentially, column by column, so that ap(1) contains a(1,1) , ap(2) and ap(3) contain a(2,1) and a(3,1) respectively, and so on. On exit, the array ap is overwritten by the lower triangular part of the updated matrix |
| pack | flag | IN | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group See Also: BLAS Level 2 (Matrix-Vector Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_SPR ( uplo IN flag, n IN POSITIVEN, alpha IN SCALAR_DBL, x IN OUT UTL_NLA_ARRAY_DBL, incx IN POSITIVEN, ap IN OUT UTL_NLA_ARRAY_DBL, pack IN flag DEFAULT 'C'); UTL_NLA.BLAS_SPR ( uplo IN flag, n IN POSITIVEN, alpha IN SCALAR_FLT, x IN OUT UTL_NLA_ARRAY_FLT, incx IN POSITIVEN, ap IN OUT UTL_NLA_ARRAY_FLT, pack IN flag DEFAULT 'C'); Parameters Table 271-21 BLAS_SPR Procedure Parameters Parameter Description uplo Specifies whether the upper or lower triangular part of the matrix A is supplied in the packed array ap : uplo = 'U' or 'u' : The upper triangular part of A is supplied in ap . uplo = 'L' or 'l' : The lower triangular part of A is supplied in ap . n Specifies the order of the matrix A . n must be at least zero. alpha Specifies the scalar alpha. x UTL_NLA_ARRAY_FLT / DBL of dimension at least (1+(n-1)*abs(incx)) Before entry, the incremented array X must contain the m element vector x . incx Specifies the increment for the elements of x . incx must not be zero. a p UTL_NLA_ARRAY_FLT / DBL of dimension at least ((n*(n +1))/2) Before entry with uplo = 'U' or 'u' , the array ap must contain the upper triangular part of the symmetric matrix packed sequentially, column by column, so that ap(1) contains a(1,1) , ap(2) and ap(3) contain a(1,2) and a(2,2) respectively, and so on. On exit, the array ap is overwritten by the upper triangular part of the updated matrix. Before entry with uplo = 'L' or 'l' , the array ap must contain the lower triangular part of the symmetric matrix packed sequentially, column by column, so that ap(1) contains a(1,1) , ap(2) and ap(3) contain a(2,1) and a(3,1) respectively, and so on. On exit, the array ap is overwritten by the lower triangular part of the updated matrix pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major