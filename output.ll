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
  %".6" = icmp sgt i32 %".5", 33
  br i1 %".6", label %"if", label %"else"
if:
  %"a" = alloca i32
  store i32 6, i32* %"a"
  br label %"merge"
else:
  br label %"merge"
merge:
  %".11" = load i32, i32* %"b"
  %".12" = icmp sgt i32 %".11", 11
  br i1 %".12", label %"if.1", label %"else.1"
if.1:
  %"a.1" = alloca i32
  store i32 5, i32* %"a.1"
  br label %"merge.1"
else.1:
  br label %"merge.1"
merge.1:
  %".17" = bitcast [5 x i8]* @"fstr" to i8*
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i32 2)
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr" = internal constant [5 x i8] c"%i \0a\00"