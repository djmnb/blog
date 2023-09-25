	.file	"test.c"
	.text
	.section .rdata,"dr"
.LC0:
	.ascii "my_entry\0"
	.text
	.globl	my_entry
	.def	my_entry;	.scl	2;	.type	32;	.endef
	.seh_proc	my_entry
my_entry:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	leaq	.LC0(%rip), %rcx
	call	printf
	nop
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.def	__main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
.LC1:
	.ascii "main\0"
	.text
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	call	__main
	leaq	.LC1(%rip), %rcx
	call	printf
	movl	$0, %eax
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.section	.init,"x"
	.globl	another_entry
	.def	another_entry;	.scl	2;	.type	32;	.endef
	.seh_proc	another_entry
another_entry:
	.seh_endprologue
/APP
 # 17 "test.c" 1
	call my_entry
 # 0 "" 2
/NO_APP
	nop
	ret
	.seh_endproc
	.ident	"GCC: (x86_64-win32-sjlj-rev0, Built by MinGW-W64 project) 8.1.0"
	.def	printf;	.scl	2;	.type	32;	.endef
