; ModuleID = "/home/quoddraco/PycharmProjects/compiler/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry:
  %"t" = alloca i32
  store i32 0, i32* %"t"
  %"a" = alloca double
  store double 0x4004000000000000, double* %"a"
  %"e" = alloca i32
  store i32 3, i32* %"e"
  %".5" = load i32, i32* %"e"
  %".6" = sitofp i32 %".5" to double
  store double %".6", double* %"a"
  %".8" = load i32, i32* %"t"
  %".9" = bitcast [5 x i8]* @"fstr1" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %".8")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr1" = internal constant [5 x i8] c"%i \0a\00"