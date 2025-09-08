class SectionInfo:

    def __init__(self, sec_name, branch, mentor):
        self.th_sub_list = {}
        self.th_sub_fac={}
        self.lab_sub_list={}
        self.lab_sub_fac={}
        self.sec_name=sec_name
        self.branch=branch
        self.mentor=mentor
        self.tt=[]

    def set_sec_name(self, sec_name):
        self.sec_name=sec_name

    def get_sec_name(self):
        return self.sec_name

    def set_branch(self, branch):
        self.branch=branch

    def get_branch(self):
        return self.branch

    def set_mentor(self, fac):
        self.mentor=fac

    def get_mentor(self):
        return self.mentor

    def set_time_table(self, tt):
        self.tt=tt

    def get_time_table(self):
        return self.tt

    def set_th_sub_list(self, th_sub_list):
        self.th_sub_list=th_sub_list

    def get_th_sub_list(self):
        return self.th_sub_list

    def set_th_sub_fac(self, th_sub_fac):
        self.th_sub_fac=th_sub_fac

    def get_th_sub_fac(self):
        return self.th_sub_fac

    def set_lab_sub_list(self, lab_sub_list):
        self.lab_sub_list=lab_sub_list

    def get_lab_sub_list(self):
        return self.lab_sub_list

    def set_lab_sub_fac(self, lab_sub_fac):
        self.lab_sub_fac=lab_sub_fac

    def get_lab_sub_fac(self):
        return self.lab_sub_fac


