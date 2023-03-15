#!/usr/bin/env python3
   
def survive(blood_type, donated_blood):
    blood_compat = {"O-": set(["O-"]),
                    "O+": set(["O-","O+"]),
                    "A-": set(["O-","A-"]),
                    "A+": set(["O-","O+","A-","A+"]),
                    "B-": set(["O-","B-"]),
                    "B+": set(["O-","O+","B-","B+"]),
                    "AB-":set(["O-","B-","A-","AB-"]),
                    "AB+":set(["O-","O+","A+","A-","B+","B-","AB+","AB-"])}
    return bool(blood_compat[blood_type].intersection(set(donated_blood)))

rec_blood_type = "B+"
avail_blood = ["A-", "B+", "AB+", "O+", "B+", "B-"]
print(survive(rec_blood_type,avail_blood))

rec_blood_type = "AB-"
avail_blood = ["O+", "AB+"]
print(survive(rec_blood_type,avail_blood))