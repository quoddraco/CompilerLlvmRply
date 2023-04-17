; ModuleID = "/home/quoddraco/PycharmProjects/compiler/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry:
  %"a" = alloca i32
  store i32 323, i32* %"a"
  %"e" = alloca i32
  store i32 503, i32* %"e"
  %".4" = load i32, i32* %"e"
  %".5" = load i32, i32* %"a"
  %".6" = sdiv i32 %".4", %".5"
  %".7" = bitcast [5 x i8]* @"fstr" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".6")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr" = internal constant [5 x i8] c"%i \0a\00"