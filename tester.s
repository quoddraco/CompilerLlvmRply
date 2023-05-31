	.text
	.file	"<string>"
	.globl	main
	.p2align	4, 0x90
	.type	main,@function
main:
	.cfi_startproc
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	$4, 4(%rsp)
	movl	$4, %edi
	callq	rip
	movl	%eax, 4(%rsp)
	movl	$fstr1, %edi
	movl	%eax, %esi
	xorl	%eax, %eax
	callq	printf
	popq	%rax
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc

	.globl	rip
	.p2align	4, 0x90
	.type	rip,@function
rip:
	.cfi_startproc
	movl	%edi, %eax
	movl	%edi, -4(%rsp)
	addl	%edi, %eax
	movl	%eax, -8(%rsp)
	retq
.Lfunc_end1:
	.size	rip, .Lfunc_end1-rip
	.cfi_endproc

	.type	fstr1,@object
	.section	.rodata,"a",@progbits
fstr1:
	.asciz	"%i \n"
	.size	fstr1, 5

	.section	".note.GNU-stack","",@progbits
