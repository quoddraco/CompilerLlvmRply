begin

func chet(a){
   int w = 1;
   return w;
};
func nechet(a){
   int r = 0;
   return r;
};

int result = 0;
int chislo = 5;
chislo = chislo mod 2;

if ( chislo != 0){
   result = nechet(0);
};

if ( chislo == 0 ){
   result = chet(1);
};

write(result);
end




