; ModuleID = "/home/quoddraco/PycharmProjects/compiler/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"()
{
entry:
  %"t" = alloca i32
  store i32 0, i32* %"t"
  %".3" = call i32 @"zalupa"()
  store i32 %".3", i32* %"t"
  %".5" = load i32, i32* %"t"
  %".6" = bitcast [5 x i8]* @"fstr1" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %".5")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

define i32 @"zalupa"()
{
entry:
  %"q" = alloca i32
  store i32 0, i32* %"q"
  %".3" = add i32 2, 2
  store i32 %".3", i32* %"q"
  %".5" = load i32, i32* %"q"
  ret i32 %".5"
}

@"fstr1" = internal constant [5 x i8] c"%i \0a\00"