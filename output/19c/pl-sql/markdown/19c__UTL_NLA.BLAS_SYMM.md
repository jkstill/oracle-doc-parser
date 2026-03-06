---
id: 19c__UTL_NLA.BLAS_SYMM
name: UTL_NLA.BLAS_SYMM
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_SYMM

This procedure performs one of the matrix-matrix operations C := alpha*A*B + beta*C or C := alpha*B*A + beta*C , where alpha and beta are scalars, A is a symmetric matrix, and B and C are m by n matrices.

## Syntax

```sql
UTL_NLA.BLAS_SYMM (
   side   IN      flag,
   uplo   IN      flag,
   m      IN      POSITIVEN,
   n      IN      POSITIVEN,
   alpha  IN      SCALAR_DOUBLE,
   a      IN      UTL_NLA_ARRAY_DBL,
   lda    IN      POSITIVEN,
   b      IN      UTL_NLA_ARRAY_DBL,
   ldb    IN      POSITIVEN,
   beta   IN      SCALAR_DOUBLE,
   c      IN OUT  UTL_NLA_ARRAY_DBL,
   ldc    IN      POSITIVEN,
   pack   IN      flag DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| side | flag | IN | Specifies whether the symmetric matrix A appears on the left or right in the operation: side = 'L' or 'l' : C := alpha*A*B + beta*C side = 'R' or 'r' : C := alpha*B*A + beta*C |
| uplo | flag | IN | Specifies whether the upper or lower triangular part of the array A is to be referenced: uplo = 'U' or 'u' : Only the upper triangular part of the symmetric matrix is to be referenced. uplo = 'L' or 'l' : Only the lower triangular part of the symmetric matrix is to be referenced. |
| m | POSITIVEN | IN | Specifies the number of rows of the matrix C . m must be at least zero. |
| n | POSITIVEN | IN | Specifies the number of columns of the matrix C . n must be at least zero. |
| alpha | SCALAR_DOUBLE | IN | SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. |
| a | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda,ka) where ka is m when side = 'L' or 'l' , and is n otherwise. Before entry with side = 'L' or 'l' , the leading m by m part of the array A must contain the symmetric matrix, such that when uplo = 'U' or 'u' , the leading m by m upper triangular part of the array A must contain the upper triangular part of the symmetric matrix and the strictly lower triangular part of A is not referenced, and when uplo = 'L' or 'l' , the leading m by m lower triangular part of the array A must contain the lower triangular part of the symmetric matrix and the strictly upper triangular part of A is not referenced. Before entry with side = ' R ' or 'r', the n by n part of the array A must contain the symmetric matrix, such that when uplo = 'U' or 'u' , the leading n by n upper triangular part of the array A must contain the upper triangular part of the symmetric matrix and the strictly lower triangular part of A is not referenced, and when uplo = 'L' or 'l' , the leading n by n lower triangular part of the array A must contain the lower triangular part of the symmetric matrix and the strictly upper triangular part of A is not referenced. |
| lda | POSITIVEN | IN | Specifies the first dimension of a as declared in the calling (sub) program. When side = 'L' or 'l' , lda must be at least max(1,m) , otherwise lda must be at least max(1,n) . |
| b | UTL_NLA_ARRAY_DBL | IN | UTL_NLA_ARRAY_FLT / DBL of DIMENSION (ldb,n) . Before entry, the leading m by n part of the array B must contain the matrix B . |
| ldb | POSITIVEN | IN | Specifies the first dimension of b as declared in the calling (sub) program. ldb must be at least max(1,m) . |
| beta | SCALAR_DOUBLE | IN | SCALAR_FLOAT / DOUBLE . Specifies the scalar beta. When beta is supplied as zero then c need not be set on input. |
| c | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT / DBL of DIMENSION (ldc,n) . Before entry, the leading m by n part of the array C must contain the matrix C , except when beta is zero, in which case C need not be set on entry. On exit, the array C is overwritten by the m by n updated matrix. |
| ldc | POSITIVEN | IN | Specifies the first dimension of C as declared in the calling (sub) program. ldc must be at least max (1,m) . |
| pack | flag | IN | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

See Also: BLAS Level 3 (Matrix-Matrix Operations) Subprograms for other subprograms in this group See Also: BLAS Level 3 (Matrix-Matrix Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_SYMM ( side IN flag, uplo IN flag, m IN POSITIVEN, n IN POSITIVEN, alpha IN SCALAR_DOUBLE, a IN UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, b IN UTL_NLA_ARRAY_DBL, ldb IN POSITIVEN, beta IN SCALAR_DOUBLE, c IN OUT UTL_NLA_ARRAY_DBL, ldc IN POSITIVEN, pack IN flag DEFAULT 'C'); UTL_NLA.BLAS_SYMM ( side IN flag, uplo IN flag, m IN POSITIVEN, n IN POSITIVEN, alpha IN SCALAR_FLOAT, a IN UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, b IN UTL_NLA_ARRAY_FLT, ldb IN POSITIVEN, beta IN SCALAR_FLOAT, c IN OUT UTL_NLA_ARRAY_FLT, ldc IN POSITIVEN, pack IN flag DEFAULT 'C'); Parameters Table 271-25 BLAS_SYMM Procedure Parameters Parameter Description side Specifies whether the symmetric matrix A appears on the left or right in the operation: side = 'L' or 'l' : C := alpha*A*B + beta*C side = 'R' or 'r' : C := alpha*B*A + beta*C uplo Specifies whether the upper or lower triangular part of the array A is to be referenced: uplo = 'U' or 'u' : Only the upper triangular part of the symmetric matrix is to be referenced. uplo = 'L' or 'l' : Only the lower triangular part of the symmetric matrix is to be referenced. m Specifies the number of rows of the matrix C . m must be at least zero. n Specifies the number of columns of the matrix C . n must be at least zero. alpha SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. a UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda,ka) where ka is m when side = 'L' or 'l' , and is n otherwise. Before entry with side = 'L' or 'l' , the leading m by m part of the array A must contain the symmetric matrix, such that when uplo = 'U' or 'u' , the leading m by m upper triangular part of the array A must contain the upper triangular part of the symmetric matrix and the strictly lower triangular part of A is not referenced, and when uplo = 'L' or 'l' , the leading m by m lower triangular part of the array A must contain the lower triangular part of the symmetric matrix and the strictly upper triangular part of A is not referenced. Before entry with side = ' R ' or 'r', the n by n part of the array A must contain the symmetric matrix, such that when uplo = 'U' or 'u' , the leading n by n upper triangular part of the array A must contain the upper triangular part of the symmetric matrix and the strictly lower triangular part of A is not referenced, and when uplo = 'L' or 'l' , the leading n by n lower triangular part of the array A must contain the lower triangular part of the symmetric matrix and the strictly upper triangular part of A is not referenced. lda Specifies the first dimension of a as declared in the calling (sub) program. When side = 'L' or 'l' , lda must be at least max(1,m) , otherwise lda must be at least max(1,n) . b UTL_NLA_ARRAY_FLT / DBL of DIMENSION (ldb,n) . Before entry, the leading m by n part of the array B must contain the matrix B . ldb Specifies the first dimension of b as declared in the calling (sub) program. ldb must be at least max(1,m) . beta SCALAR_FLOAT / DOUBLE . Specifies the scalar beta. When beta is supplied as zero then c need not be set on input. c UTL_NLA_ARRAY_FLT / DBL of DIMENSION (ldc,n) . Before entry, the leading m by n part of the array C must contain the matrix C , except when beta is zero, in which case C need not be set on entry. On exit, the array C is overwritten by the m by n updated matrix. ldc Specifies the first dimension of C as declared in the calling (sub) program. ldc must be at least max (1,m) . pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major