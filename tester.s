	.text
	.file	"<string>"
	.globl	main
	.p2align	4, 0x90
	.type	main,@function
main:
	pushq	%rax
	movl	$4, %edi
	callq	rip
	movl	$fstr1, %edi
	movl	%eax, %esi
	xorl	%eax, %eax
	popq	%rcx
	jmp	printf
.Lfunc_end0:
	.size	main, .Lfunc_end0-main

	.globl	rip
	.p2align	4, 0x90
	.type	rip,@function
rip:
	leal	(%rdi,%rdi), %eax
	retq
.Lfunc_end1:
	.size	rip, .Lfunc_end1-rip

	.type	fstr1,@object
	.section	.rodata,"a",@progbits
fstr1:
	.asciz	"%i \n"
	.size	fstr1, 5

	.section	".note.GNU-stack","",@progbits
