class library :
    l1 = []
    def __init__(self,name,no_of_books,newname) :
        self.name=name
        self.no_of_books=no_of_books
        self.newname=newname

    def library1(self):
        d1={1:self.name,2:self.no_of_books}
        print(d1)
        self.l1.append(self.name)
        self.l1.append(self.no_of_books)
        print(self.l1)

    def update(self):
        for i in range(len(self.l1)):
            if self.l1[i] == self.name:
               self.l1[i] = self.newname
               print(self.l1)
               break
            else:
                print ("not found")


p1=library("alex",2,"anu")
p1.library1()
p1.update()
