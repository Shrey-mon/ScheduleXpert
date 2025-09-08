

def getCSSubNames():
    sub_names = {
        'CS402': 'ANALYSIS & DESIGN OF ALGORITHM',
        'CS403': 'SOFTWARE ENGINEERING',
        'CS404': 'COMPUTER SYSTEM ORGANIZATION',
        'CS405': 'OPERATING SYSTEM',
        'CS406': 'PROGRAMMING PRACTICE ( JAVA )',
        'CS407': 'INTERNSHIP - MINI PROJECT'
    }
    return sub_names


def getALSubNames():
    sub_names = {
        'AL402': 'ANALYSIS & DESIGN OF ALGORITHM',
        'AL403': 'SOFTWARE ENGINEERING',
        'AL404': 'COMPUTER ORG. & ARCHITECTURE',
        'AL405': 'MACHINE LEARNING',
        'AL406': 'PROGRAMMING PRACTICE ( JAVA )',
        'AL407': 'INTERNSHIP - MINI PROJECT'
    }
    return sub_names


def getCYSubNames():
    sub_names = {
        'CY402': 'FUNDAMENTALS OF LINEAR ALGEBRA',
        'CY403': 'COMPUTER NETWORKS',
        'CY404': 'OPERATING SYSTEM',
        'CY405': 'DATABASE MANAGEMENT SYSTEM',
        'CY406': 'PROGRAMMING PRACTICE ( PYHTON )',
        'CY407': 'INTERNSHIP - MINI PROJECT'
    }
    return sub_names


def getSubInfoCS():
    subjectinfo = {
        'CS402': ['t', 'l'],
        'CS403': ['t', 'l'],
        'CS404': ['t', 'l'],
        'CS405': ['t', 'l'],
        'CS406': ['l'],
        'CS407': ['l'],
    }
    return subjectinfo


def getSubInfoAL():
    subjectinfo = {
        'AL402': ['t', 'l'],
        'AL403': ['t', 'l'],
        'AL404': ['t', 'l'],
        'AL405': ['t', 'l'],
        'AL406': ['l'],
        'AL407': ['l'],
    }
    return subjectinfo


def getSubInfoCY():
    subjectinfo = {
        'CY402': ['t', 'l'],
        'CY403': ['t', 'l'],
        'CY404': ['t', 'l'],
        'CY405': ['t', 'l'],
        'CY406': ['l'],
        'CY407': ['l'],
    }
    return subjectinfo


def getLabInfo():
    # lab_no: [lab_capacity, max_slots/week]
    labInfo = {
        'F-11 OLD': ['f', 36],
        'F-13 NEW': ['h', 36],
        'F-14 NEW': ['h', 36],
        'F-15 NEW': ['h', 36],
        'F-10(A) OLD': ['h', 36],
        'F-10(B) OLD': ['h', 36],
        'F-01 OLD': ['f', 36],
        'F-09 OLD': ['f', 36]
    }
    return labInfo


# l=['a','b','c','d','e']
# a=l.pop(0)
# l.append(a)
# print(l)

    # if section_tt[sec][day][time] == '' and section_tt[sec][day][time + 1] == '':
    #     pass
    # else:
    #     # slots_copy.remove(slot)
    #     return False
    #
    # if sub in section_tt[sec][day]:
    #     return False
    #
    # if ('08' not in lab) and ('07' not in lab) and ('5' not in sec):
    #     if lab_tt[labs[lab][0]][day][time] == '' and lab_tt[labs[lab][0]][day][time + 1] == '':
    #         pass
    #     else:
    #         return False
    #     if lab_tt[labs[lab][1]][day][time] == '' and lab_tt[labs[lab][1]][day][time + 1] == '':
    #         pass
    #     else:
    #         return False
    #     if faculty_tt[labs_fac[lab][0].getFName()][day][time] == '' and \
    #             faculty_tt[labs_fac[lab][0].getFName()][day][time + 1] == '':
    #         pass
    #     else:
    #         return False
    #     if faculty_tt[labs_fac[lab][1].getFName()][day][time] == '' and \
    #             faculty_tt[labs_fac[lab][1].getFName()][day][time + 1] == '':
    #         pass
    #     else:
    #         return False
    #     if time == 0:
    #         fac1 = faculty_tt[labs_fac[lab][0].getFName()][day]
    #         fac2 = faculty_tt[labs_fac[lab][1].getFName()][day]
    #         if (fac1[time + 2] == '' and fac2[time + 2] == '') or (fac1[time + 3] == '' and fac2[time + 3] == '') or \
    #                 (fac1[time + 2] == '' and fac2[time + 3] == '') or (fac1[time + 3] == '' and fac2[time + 2] == ''):
    #             pass
    #         else:
    #             return False
    #     elif time == 2:
    #         fac1 = faculty_tt[labs_fac[lab][0].getFName()][day]
    #         fac2 = faculty_tt[labs_fac[lab][1].getFName()][day]
    #         if (fac1[time - 2] == '' and fac2[time - 2] == '') or (fac1[time - 1] == '' and fac2[time - 1] == '') or \
    #                 (fac1[time - 2] == '' and fac2[time - 1] == '') or (fac1[time - 1] == '' and fac2[time - 2] == ''):
    #             pass
    #         else:
    #             return False
    #
    #     # cse_labs_fac[lab][0].getFLoad()[sec]
    #
    # else:
    #     if lab_tt[labs[lab][0]][day][time] == '' and lab_tt[labs[lab][0]][day][time + 1] == '':
    #         pass
    #     else:
    #         return False
    #     if faculty_tt[labs_fac[lab][0].getFName()][day][time] == '' and \
    #             faculty_tt[labs_fac[lab][0].getFName()][day][time + 1] == '':
    #         pass
    #     else:
    #         return False
    #     if time == 2:
    #         if faculty_tt[labs_fac[lab][0].getFName()][day][time - 2] == '' or \
    #                 faculty_tt[labs_fac[lab][0].getFName()][day][time - 1] == '':
    #             pass
    #         else:
    #             return False
    # if len(labs_fac[lab]) > 1:
    #     for i in labs_fac[lab]:
    #         if len(i.getFLoad()[sec]) > 1:
    #             for j in i.getFLoad()[sec]:
    #                 if 4 >= j[3] > 0:
    #                     # j[3]=j[3]-2
    #                     break
    #                 else:
    #                     return False
    #         else:
    #             if 4 >= i.getFLoad()[sec][0][3] > 0:
    #                 # i.getFLoad()[sec][0][3]=i.getFLoad()[sec][0][3]-2
    #                 break
    #             else:
    #                 return False
    # else:
    #     if len(labs_fac[lab][0].getFLoad()[sec]) > 1:
    #         for i in labs_fac[lab][0].getFLoad()[sec]:
    #             if 2 >= i[3] > 0:
    #                 # i[3]=i[3]-2
    #                 break
    #             else:
    #                 return False
    #     else:
    #         if 4 >= labs_fac[lab][0].getFLoad()[sec][0][3] > 0:
    #             # cse_labs_fac[lab][0].getFLoad()[sec][0][3]=cse_labs_fac[lab][0].getFLoad()[sec][0][3]-2
    #             pass
    #         else:
    #             return False


# l=[0,6,1,2,3,4]
# l.remove(0)
# print(l)