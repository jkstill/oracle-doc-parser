---
id: 19c__UTL_NLA.BLAS_GEMM
name: UTL_NLA.BLAS_GEMM
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_GEMM

This procedure performs one of the matrix-matrix operations.

## Syntax

```sql
C := alpha*op( A )*op( B ) + beta*C
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| transa |  |  | Specifies the form of op(A) to be used in the matrix multiplication as follows: transa = 'N' or 'n' : op(A) = 'A' transa = 'T' or 't' : op(A) = 'A' transa = 'C' or 'c' : op(A) = 'A' |
| transb |  |  | Specifies the form of op (B) to be used in the matrix multiplication as follows: transb = 'N' or 'n' : op(B) = B transb = 'T' or 't' : op(B) = B' transb = 'C' or 'c' : op(B) = B' |
| m |  |  | Specifies the number of rows of the matrix op (A) and of the matrix C . m must be at least zero. |
| n |  |  | Specifies the number of columns of the matrix op (B) and of the matrix C . n must be at least zero. |
| k |  |  | Specifies the rows of the matrix op(A) and the number of columns of the matrix op(B) . k must be at least zero. |
| alpha |  |  | SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. |
| a |  |  | UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda, ka) where ka is k when transa = 'N' or 'n' , and is m otherwise. Before entry with transa = 'N' or 'n' , the leading m by k part of the array A must contain the matrix A , otherwise the leading k by m part of the array A must contain the matrix A . |
| lda |  |  | Specifies the first dimension of a as declared in the calling (sub) program. When transa = 'N' or 'n', lda must be at least max (1,k) . |
| b |  |  | UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda, kb) where kb is n when transb = ' 'N' or 'n' , and is k otherwise. Before entry with transb = 'N' or 'n' , the leading k by n part of the array b must contain the matrix B , otherwise the leading n by k part of the array b must contain the matrix B . |
| ldb |  |  | Specifies the first dimension of b as declared in the calling (sub) program. When transb = 'N' or 'n', ldb must be at least max (1, n) . |
| beta |  |  | SCALAR_FLOAT / DOUBLE . Specifies the scalar beta. When beta is supplied as zero then c need not be set on input. |
| c |  |  | UTL_NLA_ARRAY_FLT / DBL of DIMENSION (ldc, n). Before entry, the leading m by n part of the array C must contain the matrix C , except when beta is zero, in which case C need not be set on entry. On exit, the array C is overwritten by the m by n matrix (alpha*op(A)*op(B) + beta*C) . |
| ldc |  |  | Specifies the first dimension of C as declared in the calling (sub) program. ldc must be at least max(1, m) . |
| pack |  |  | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

C := alpha*op( A )*op( B ) + beta*C where op(X) is one of op(X) = X or op(X) = X' where alpha and beta are scalars, and A , B and C are matrices, with op(A) an m by k matrix, op(B) a k by n matrix and C an m by n matrix. See Also: BLAS Level 3 (Matrix-Matrix Operations) Subprograms for other subprograms in this group See Also: BLAS Level 3 (Matrix-Matrix Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_GEMM ( transa IN flag, transb IN flag, m IN POSITIVEN, n IN POSITIVEN, k IN POSITIVEN, alpha IN SCALAR_DOUBLE, a IN UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, b IN UTL_NLA_ARRAY_DBL, ldb IN POSITIVEN, beta IN SCALAR_DOUBLE, c IN OUT UTL_NLA_ARRAY_DBL, ldc IN POSITIVEN, pack IN flag DEFAULT 'C'); UTL_NLA.BLAS_GEMM ( transa IN flag, transb IN flag, m IN POSITIVEN, n IN POSITIVEN, k IN POSITIVEN, alpha IN SCALAR_FLOAT, a IN UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, b IN UTL_NLA_ARRAY_FLT, ldb IN POSITIVEN, beta IN SCALAR_FLOAT, c IN OUT UTL_NLA_ARRAY_FLT, ldc IN POSITIVEN, pack IN flag DEFAULT 'C'); Parameters Table 271-12 BLAS_GEMM Procedure Parameters Parameter Description transa Specifies the form of op(A) to be used in the matrix multiplication as follows: transa = 'N' or 'n' : op(A) = 'A' transa = 'T' or 't' : op(A) = 'A' transa = 'C' or 'c' : op(A) = 'A' transb Specifies the form of op (B) to be used in the matrix multiplication as follows: transb = 'N' or 'n' : op(B) = B transb = 'T' or 't' : op(B) = B' transb = 'C' or 'c' : op(B) = B' m Specifies the number of rows of the matrix op (A) and of the matrix C . m must be at least zero. n Specifies the number of columns of the matrix op (B) and of the matrix C . n must be at least zero. k Specifies the rows of the matrix op(A) and the number of columns of the matrix op(B) . k must be at least zero. alpha SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. a UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda, ka) where ka is k when transa = 'N' or 'n' , and is m otherwise. Before entry with transa = 'N' or 'n' , the leading m by k part of the array A must contain the matrix A , otherwise the leading k by m part of the array A must contain the matrix A . lda Specifies the first dimension of a as declared in the calling (sub) program. When transa = 'N' or 'n', lda must be at least max (1,k) . b UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda, kb) where kb is n when transb = ' 'N' or 'n' , and is k otherwise. Before entry with transb = 'N' or 'n' , the leading k by n part of the array b must contain the matrix B , otherwise the leading n by k part of the array b must contain the matrix B . ldb Specifies the first dimension of b as declared in the calling (sub) program. When transb = 'N' or 'n', ldb must be at least max (1, n) . beta SCALAR_FLOAT / DOUBLE . Specifies the scalar beta. When beta is supplied as zero then c need not be set on input. c UTL_NLA_ARRAY_FLT / DBL of DIMENSION (ldc, n). Before entry, the leading m by n part of the array C must contain the matrix C , except when beta is zero, in which case C need not be set on entry. On exit, the array C is overwritten by the m by n matrix (alpha*op(A)*op(B) + beta*C) . ldc Specifies the first dimension of C as declared in the calling (sub) program. ldc must be at least max(1, m) . pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major