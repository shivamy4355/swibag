class ajus:
    def __init(self, a=0,b=0):
        self.a=a;
        self.b=b;
    def __del__(self):
        class_name=self.__class__init.__name__;
        print(class__name,"angee");
a1=ajus(); a2=ajus(); a3=a2;
#print(id)
del  a1,a2,a3;
