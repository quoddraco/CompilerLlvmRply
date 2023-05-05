; ModuleID = "/home/quoddraco/PycharmProjects/compiler/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry:
  %"b" = alloca i32
  store i32 22, i32* %"b"
  %"f" = alloca i32
  store i32 33, i32* %"f"
  %"e" = alloca double
  store double 0x4036e66666666666, double* %"e"
  %".5" = load i32, i32* %"b"
  %".6" = icmp ne i32 %".5", 21
  %".7" = bitcast [5 x i8]* @"fstr" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i1 %".6")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr" = internal constant [5 x i8] c"%i \0a\00"