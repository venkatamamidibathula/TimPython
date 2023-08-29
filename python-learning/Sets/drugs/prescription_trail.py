from prescription_data import *

patients_trail = ["Denise" , "Eddie", "Frank", "Georgia", "Kenny"]

for patient in patients_trail:
    prescribed_medicines = patients[patient]
    try:
        prescribed_medicines.remove('warfarin')
        prescribed_medicines.add('edoxaban')
    except KeyError:
        print(f"{patient} needs to removed from trail")
    print(f"{patient}:{prescribed_medicines}")


