	.file	"04-asmTest.cpp"
	.text
	.globl	_Z3addii
	.def	_Z3addii;	.scl	2;	.type	32;	.endef
	.seh_proc	_Z3addii
_Z3addii:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	.seh_endprologue
	movl	%ecx, 16(%rbp)
	movl	%edx, 24(%rbp)
	movl	16(%rbp), %edx
	movl	24(%rbp), %eax
	addl	%edx, %eax
	popq	%rbp
	ret
	.seh_endproc
	.globl	_Z6callerv
	.def	_Z6callerv;	.scl	2;	.type	32;	.endef
	.seh_proc	_Z6callerv
_Z6callerv:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$48, %rsp
	.seh_stackalloc	48
	.seh_endprologue
	movl	$10, -4(%rbp)
	movl	$10, -8(%rbp)
	movl	-8(%rbp), %edx
	movl	-4(%rbp), %eax
	movl	%eax, %ecx
	call	_Z3addii
	movl	%eax, -12(%rbp)
	movl	-12(%rbp), %eax
	addq	$48, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.ident	"GCC: (x86_64-win32-sjlj-rev0, Built by MinGW-W64 project) 8.1.0"
