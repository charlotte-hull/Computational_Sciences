class fibonacci:
    k=1
    f_k_minus1=1
    f_k_minus2=0

    def update(self):
        self.k+=1
        f_k= self.f_k_minus1 + self.f_k_minus2
        self.f_k_minus2 = self.f_k_minus1
        self.f_k_minus1 = f_k

    def evaluate(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            while self.k<n:
                self.update()
            return self.f_k_minus1
        
    def reset(self):
            self.k = 1
            self.f_k_minus1 = 1
            self.f_k_minus2 = 0


n = 6
fibonacci=fibonacci()
print(fibonacci.evaluate(n))
   
