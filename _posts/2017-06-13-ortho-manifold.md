---
layout: post
title: How the set of n by n orthogonal matrices forms a lie group.
---

Preface: This article is the beginning of a series of articles about 
random parts about math that I find really cool.

Before we get started, it is always good to give some definitions so
as to avoid any confusion.

What is a (smooth) manifold?

A set \\( X\subset\mathbb{R}^n \\) such that for any point $x\in X$, 
there exists a neighbourhood \\( N(x,\epsilon) \\) such that there
exists a diffeomorphism ( \\( C^{\infty} \\) and bijective) 
\\( f: \mathbb{R}^k \to N(x,\epsilon) \\). In this case, 
\\( X \\) is said to be of dimension \\( k \\).

What is a tangent space?

Let \\(X\\) be a \\(k\\)-dimensional manifold. Then,
there exists a mapping \\( f: \mathbb{R}^k \to N(x,\epsilon) \\). Let
\\(df_{x}: \mathbb{R}^k \to \mathbb{R}^n \\)
be the directional derivative of \\(f\\) at \\(x\in\mathbb{R}^k\\). The
image of \\(df_{x}\\) is called the tangent space of \\(X\\) denoted by
\\(T_{x}(X)\\). Thus \\(df_{x}\\) is the mapping from \\(\mathbb{R}^k\to T_{x}(X)\\).

What is an orthogonal matrix? A symmetric matrix?

An orthogonal matrix is a generalized notion of the rotation matrix \\(R\theta\\) in \\(\mathbb{R}^2\\)
in the sense that these matrices are distance preserving functions or more
formally known as isomoteries which are perhaps one of the nicest functions we can
find between two arbitrary metric spaces. An orthogonal matrix is a matrix consisting
of orthonormal vectors, or more specifically, a matrix \\(Q\\) is orthogonal if:
\\[ QQ^{T} = I \\] where \\(I\\) is the identity \\(n\times n\\) matrix. Symmetric
matrices are matrices which can be diagonalized by orthogonal matrices i.e. for
every symmetric matrix \\(A\\), there exists an orthogonal matrix \\(Q\\) such that
\\[ D = Q^{T}AQ \\] where \\(D\\) is the diagonal matrix. A much more usual definition
of symmetric matrices is any matrix whose transpose is itself, i.e.
\\[ A = A^{T} \\]

Let \\(O(n)\\) be the set of \\(n\times n\\) orthogonal matrices, \\(S(n)\\) for symmetric matrices and
\\(M(n)\\) for any general matrix in \\(\mathbb{R}^{n}\\). 

Remark: Consider the matrix \\(A\in M(n)\\) which
has \\(n^2\\) entries. Thus, \\(M(n)\\) can be viewed as the set \\(\mathbb{R}^{n^{2}}\\).

Remark: We know that, \\(S(n)\\) forms a subspace under the vector space \\(M(n)\\). Thus, we can calculate
the dimension of this subspace explicitly. We know that to uniquely determine a symmetric matrix,
it suffices to only list the entries in the upper triangle part of the matrix as well as the 
diagonal. Thus, to uniquely determine an element in \\(S(n)\\), we need:
\\[ \frac{n^{2}}{2} + n = \frac{(n)(n+1)}{2} \\]
elements. Thus, \\(S(n)\\) is of dimension \\(\mathbb{R}^{k}\\) where \\(k=\frac{(n)(n+1)}{2}\\).

This proof that \\(O(n)\\) is a manifold under \\(M(n)=\mathbb{R}^{n^{2}}\\) is a very clear
application of the pre-image theorem so we state it first but before, we state that, we need to have
a notion of a regular value. So we state these two things now before attempting to prove anything:

What is a regular value?

Let \\(f: X\to Y\\) be a smooth map between manifolds. Then \\(y\\) is a regular value of \\(f\\) if
and only if every for all \\(x\in f^{-1}(y) \\), \\(df_{x}: T_{x}(X) \to T_{y}(Y)\\) is surjective
where \\(y = f(x)\\).

What is the pre-image theorem?

If \\(y\\) is a regular value of \\(f: X\to Y\\), then the preimage \\(f^{-1}(y)\\) is a
submanifold of \\(X\\), with dim \\(f^{-1}(y) =\\) dim \\(X\\) - dim \\(Y\\).

Thus, for our purposes, let \\(f: M(n) \to S(n)\\) via \\(A \mapsto AA^{T}\\). Since for any orthogonal
matrix \\(Q\\), \\(QQ^{T} = I\\), it follows that we want to determine if the preimage \\(f^{-1}(I)\\)
is a submanifold of \\(M(n)\\). Thus, it leaves us to check that \\(I\\) is a regular value of \\(f\\)
or in other words, it leaves us to check that for any \\(A\in f^{-1}(I)\\) (so any orthogonal matrix),
\\(df_{A}: T_{A}(M(n)) \to T_{f(A)}(S(n))\\) is surjective. First, note that for any \\(B\in M(n)\\):

\begin{align}
        df_{A}(B) = \lim_{h\to 0} \frac{f(A+h)-f(A)}{h}
        = \lim_{h\to 0} BA^{T} + AB^{T} + hBB^{T}
        = BA^{T} + AB^{T}
\end{align}

So, we want to check that for any matrix \\(C\in S(n)\\), that, there exists \\(B\in M(n)\\) such
that \\(df_{A}(B) = BA^{T} + AB^{T} = C\\). Note that since \\(C\\) is symmetric, then
\\(\frac{1}{2}C + \frac{1}{2}C^{T} = C\\). Thus, if we suppose that \\(BA^{T} = \frac{1}{2}C\\), then:
\\[ BA^{T} = \frac{1}{2}C \implies B = \frac{1}{2}CA\\]
so,
\begin{align}
    BA^{T} + AB^{T} = (\frac{1}{2}CA)A^{T} + A(\frac{1}{2}CA)^{T} = \frac{1}{2}(C+C^{T}) = C
\end{align}

So, we see that \\(df_{A}: M(n) \to S(n)\\) is surjective for any \\(A\in O(n)\\), proving that
\\(f^{-1}(I)=O(n)\\) is a manifold under \\(M(n)\\).

In order, to show this is a lie group under the operation of matrix multiplication:
\\[ O(n) \times O(n) \to O(n) \\]
is a smooth operation, it suffices to show that if \\(A,B\in O(n)\\), then \\(AB\\) is an
orthogonal matrix. Note that:
\\[ (AB)^{T}(AB) = B^{T}A^{T}(AB) = B^{T}B = I\\]
so that \\(AB\\) is an orthogonal matrix. The inverse of this operation comes from the fact
that:
\\[ A^{T} = A^{-1} \\]
so this set also fulfills the definition of a group with the additional property that its
operation is smooth. Thus, \\(O(n)\\) is a lie group!
