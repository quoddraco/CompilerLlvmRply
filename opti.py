def optimize_assembler_code(code):
    # Удаление ненужных инструкций и оптимизация
    optimized_code = []
    used_registers = set()
    modified_registers = set()

    for line in code:
        if line.startswith(("pushq", "popq")):
            # Удаление бесполезных push/pop инструкций
            continue
        elif line.startswith("movl"):
            parts = line.split()
            dest = parts[1]
            src = parts[2]
            if dest in modified_registers:
                # Удаление ненужных movl инструкций, если регистр уже был изменен
                continue
            if src in used_registers:
                # Если исходный регистр используется позже, добавляем его в использованные регистры
                used_registers.add(dest)
            else:
                # Удаляем ненужные movl инструкции и добавляем их в измененные регистры
                modified_registers.add(dest)
                continue
        elif line.startswith(("callq", "retq")):
            # Удаление ненужных callq и retq инструкций
            continue

        optimized_code.append(line)

    return optimized_code


# Пример использования
assembler_code = [
    "	.text",
    "	.file	\"<string>\"",
    "	.globl	main",
    "	.p2align	4, 0x90",
    "	.type	main,@function",
    "main:",
    "	.cfi_startproc",
    "	pushq	%rax",
    "	.cfi_def_cfa_offset 16",
    "	movl	$0, 4(%rsp)",
    "	movl	$4, %edi",
    "	callq	rip",
    "	movl	%eax, 4(%rsp)",
    "	movl	$fstr1, %edi",
    "	movl	%eax, %esi",
    "	xorl	%eax, %eax",
    "	callq	printf",
    "	popq	%rax",
    "	.cfi_def_cfa_offset 8",
    "	retq",
    ".Lfunc_end0:",
    "	.size	main, .Lfunc_end0-main",
    "	.cfi_endproc",
    "",
    "	.globl	rip",
    "	.p2align	4, 0x90",
    "	.type	rip,@function",
    "rip:",
    "	.cfi_startproc",
    "	movl	%edi, %eax",
    "	movl	%edi, -4(%rsp)",
    "	incl	%eax",
    "	movl	%eax, -8(%rsp)",
    "	retq",
    ".Lfunc_end1:",
    "	.size	rip, .Lfunc_end1-rip",
    "	.cfi_endproc",
    "",
    "	.type	fstr1,@object",
    "	.section	.rodata,\"a\",@progbits",
    "fstr1:",
    "	.asciz	\"%i \\n\"",
    "	.size	fstr1, 5",
    "",
    "	.section	\".note.GNU-stack\",\"\",@progbits",
]

optimized_code = optimize_assembler_code(assembler_code)
for line in optimized_code:
    print(line)