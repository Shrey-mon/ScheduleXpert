class FacultyInfo:
    def __init__(self, fac):
        self.f_id = fac[0]
        self.f_name = fac[1]
        self.f_phone = fac[2]
        self.f_load = {}

    # def __init__(self,f_id,f_name,f_phone):
    #     self.f_id=f_id
    #     self.f_name=f_name
    #     self.f_phone=f_phone

    def getFId(self):
        return self.f_id

    def getFName(self):
        return self.f_name

    def getFPhone(self):
        return self.f_phone

    def getFLoad(self):
        return self.f_load

    def setFId(self, f_id):
        self.f_id = f_id

    def setFName(self, f_name):
        self.f_name = f_name

    def setFPhone(self, f_phone):
        self.f_phone = f_phone

    def resetFLoad(self):
        self.f_load={}

    def setFLoad(self, sec, val):
        if sec in self.f_load:
            l=list(self.f_load[sec])
            l.append(val)
            self.f_load[sec]=l
        else:
            self.f_load[sec] = [val]

    def __str__(self):
        return f"name: {self.f_name} ,id: {self.f_id} , phone: {self.f_phone}, load: {self.f_load}"
