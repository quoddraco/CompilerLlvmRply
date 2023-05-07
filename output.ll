; ModuleID = "/home/quoddraco/PycharmProjects/compiler/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry:
  %"b" = alloca i32
  store i32 22, i32* %"b"
  %"a" = alloca i32
  store i32 10, i32* %"a"
  %"c" = alloca i32
  %".4" = load i32, i32* %"b"
  %".5" = load i32, i32* %"a"
  %".6" = add i32 %".4", %".5"
  store i32 %".6", i32* %"c"
  %".8" = load i32, i32* %"c"
  %".9" = bitcast [5 x i8]* @"fstr" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %".8")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr" = internal constant [5 x i8] c"%i \0a\00"