class Vector:
    def __init__ (self,x=0,y=0,z=0,w=0):
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)
        self.set_w(w)
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def get_z(self):
        return self.__z
    def get_w(self):
        return self.__w
    #setters
    def set_x(self,x):
        if isinstance(x,int)or isinstance(x,float):
            self.__x=x
            return True
        return False
    @property
    def z(self):
        return self.__z
    @z.setter

    def set_y(self,y):
        if isinstance(y,int)or isinstance(y,float):
            self.__y=y
            return True
        return False
    def set_z(self,z):
        if isinstance(z,int)or isinstance(z,float):
            self.__z=z
            return True
        return False
    def set_w(self,w):
        if isinstance(w,int)or isinstance(w,float):
            self.__w=w
            return True
        return False
    pass
vec1=Vector(4,2)
print(vec1.x,',',vec1.y)

vec1.x=2.3
print(vec1.x,',',vec1.y)



