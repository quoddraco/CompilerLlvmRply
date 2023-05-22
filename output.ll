; ModuleID = "/home/quoddraco/PycharmProjects/compiler/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry:
  %"t" = alloca i32
  store i32 2, i32* %"t"
  store i32 4, i32* %"t"
  %".4" = load i32, i32* %"t"
  %".5" = call i32 @"zalupa"(i32 %".4")
  store i32 %".5", i32* %"t"
  %".7" = load i32, i32* %"t"
  %".8" = bitcast [5 x i8]* @"fstr1" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 %".7")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

define i32 @"zalupa"(i32 %".1")
{
entry:
  %"a" = alloca i32
  store i32 %".1", i32* %"a"
  %".4" = load i32, i32* %"a"
  %".5" = add i32 %".4", 6
  store i32 %".5", i32* %"a"
  %".7" = load i32, i32* %"a"
  ret i32 %".7"
}

@"fstr1" = internal constant [5 x i8] c"%i \0a\00"