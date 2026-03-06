---
id: 19c__UTL_NLA.BLAS_SYRK
name: UTL_NLA.BLAS_SYRK
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_SYRK

This procedure performs one of the symmetric rank k operations C := alpha*A*A' + beta*C or C := alpha*A'*A + beta*C , where alpha and beta are scalars, C is an n by n symmetric matrix and A is an n by k matrix in the first case and a k by n matrix in the second case.

## Syntax

```sql
UTL_NLA.BLAS_SYRK (
   uplo   IN      flag,
   trans  IN      flag,
   n      IN      POSITIVEN,
   k      IN      POSITIVEN,
   alpha  IN      SCALAR_DOUBLE,
   a      IN      UTL_NLA_ARRAY_DBL,
   lda    IN      POSITIVEN,
   beta   IN      SCALAR_DOUBLE,
   c      IN OUT  UTL_NLA_ARRAY_DBL,
   ldc    IN      POSITIVEN,
   pack   IN      flag DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| uplo | flag | IN | Specifies whether the upper or lower triangular part of the array C is to be referenced: uplo = 'U' or 'u' : Only the upper triangular part of C is to be referenced. uplo = 'L' or 'l' : Only the lower triangular part of C is to be referenced. |
| trans | flag | IN | Specifies the operations to be performed: trans = 'N' or 'n' : C := alpha*A*A' + beta*C trans = 'T' or 't' : C := alpha*A'*A + beta*C trans = 'C' or 'c' : C := alpha*A'*A + beta*C |
| n | POSITIVEN | IN | Specifies the order of matrix C . n must be at least zero. |
| k | POSITIVEN | IN | On entry with trans = 'N' or 'n' , k specifies the number of columns of the matrix A . On entry with trans = 'T' or 't' or trans = 'C' or 'c' , k specifies the number of rows of the matrix A . k must be at least zero. |
| alpha | SCALAR_DOUBLE | IN | SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. |
| a | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda,ka) where ka is k when trans = 'N' or 'n' , and is n otherwise. Before entry with trans = 'N' or 'n' , the leading n by k part of the array A must contain the matrix A , otherwise the leading k by n part of the array A must contain the matrix A. |
| lda | POSITIVEN | IN | Specifies the first dimension of a as declared in the calling (sub) program. When trans = 'N' or 'n' , lda must be at least max(1,n) , otherwise lda must be at least max(1,k) . |
| beta | SCALAR_DOUBLE | IN | SCALAR_FLOAT / DOUBLE . Specifies the scalar beta. |
| c | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of DIMENSION (ldc,n) . Before entry with uplo = 'U' or 'u' , the leading n by n upper triangular part of the array C must contain the upper triangular part of the symmetric matrix and the strictly lower triangular part of C is not referenced. On exit, the upper triangular part of the array C is overwritten by the upper triangular part of the updated matrix. Before entry with uplo = 'L' or 'l' , the leading n by n lower triangular part of the array C must contain the lower triangular part of the symmetric matrix and the strictly upper triangular part of C is not referenced. On exit, the lower triangular part of the array C is overwritten by the lower triangular part of the updated matrix. |
| ldc | POSITIVEN | IN | Specifies the first dimension of C as declared in the calling (sub) program. ldc must be at least max(1,n) . |
| pack | flag | IN | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

See Also: BLAS Level 3 (Matrix-Matrix Operations) Subprograms for other subprograms in this group See Also: BLAS Level 3 (Matrix-Matrix Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_SYRK ( uplo IN flag, trans IN flag, n IN POSITIVEN, k IN POSITIVEN, alpha IN SCALAR_DOUBLE, a IN UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, beta IN SCALAR_DOUBLE, c IN OUT UTL_NLA_ARRAY_DBL, ldc IN POSITIVEN, pack IN flag DEFAULT 'C'); UTL_NLA.BLAS_SYRK ( uplo IN flag, trans IN flag, n IN POSITIVEN, k IN POSITIVEN, alpha IN SCALAR_FLOAT, a IN UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, beta IN SCALAR_FLOAT, c IN OUT UTL_NLA_ARRAY_DBL, ldc IN POSITIVEN, pack IN flag DEFAULT 'C'); Parameters Table 271-30 BLAS_SYRK Procedure Parameters Parameter Description uplo Specifies whether the upper or lower triangular part of the array C is to be referenced: uplo = 'U' or 'u' : Only the upper triangular part of C is to be referenced. uplo = 'L' or 'l' : Only the lower triangular part of C is to be referenced. trans Specifies the operations to be performed: trans = 'N' or 'n' : C := alpha*A*A' + beta*C trans = 'T' or 't' : C := alpha*A'*A + beta*C trans = 'C' or 'c' : C := alpha*A'*A + beta*C n Specifies the order of matrix C . n must be at least zero. k On entry with trans = 'N' or 'n' , k specifies the number of columns of the matrix A . On entry with trans = 'T' or 't' or trans = 'C' or 'c' , k specifies the number of rows of the matrix A . k must be at least zero. alpha SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. a UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda,ka) where ka is k when trans = 'N' or 'n' , and is n otherwise. Before entry with trans = 'N' or 'n' , the leading n by k part of the array A must contain the matrix A , otherwise the leading k by n part of the array A must contain the matrix A. lda Specifies the first dimension of a as declared in the calling (sub) program. When trans = 'N' or 'n' , lda must be at least max(1,n) , otherwise lda must be at least max(1,k) . beta SCALAR_FLOAT / DOUBLE . Specifies the scalar beta. c UTL_NLA_ARRAY_FLT / DBL of DIMENSION (ldc,n) . Before entry with uplo = 'U' or 'u' , the leading n by n upper triangular part of the array C must contain the upper triangular part of the symmetric matrix and the strictly lower triangular part of C is not referenced. On exit, the upper triangular part of the array C is overwritten by the upper triangular part of the updated matrix. Before entry with uplo = 'L' or 'l' , the leading n by n lower triangular part of the array C must contain the lower triangular part of the symmetric matrix and the strictly upper triangular part of C is not referenced. On exit, the lower triangular part of the array C is overwritten by the lower triangular part of the updated matrix. ldc Specifies the first dimension of C as declared in the calling (sub) program. ldc must be at least max(1,n) . pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major