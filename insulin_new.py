a = "ORIGIN      1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed 61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn//"
demo = a.replace("//", "")
insulin = demo.replace("ORIGIN","")
insulin = insulin.replace("1","")
insulin = insulin.replace("6", "")
insulin = insulin.replace(" ","")
print("the insulin - ", insulin)

isinsulin = insulin[0:24]
lengthis = len(isinsulin)
print("the isinsulin - ", isinsulin)
print("the length of isinsulin - ", lengthis)

binsulin = insulin[24:54]
lengthb = len(binsulin)
print("the isinsulin - ", binsulin)
print("the length of isinsulin - ", lengthb)

cinsulin = insulin[54:89]
lengthc = len(cinsulin)
print("the isinsulin - ", cinsulin)
print("the length of isinsulin - ", lengthc)

ainsulin = insulin[89:110]
lengtha = len(ainsulin)
print("the isinsulin - ", ainsulin)
print("the length of isinsulin - ", lengtha)