def calculate_euclidean(px_f, py_f, qx_f, qy_f):
    result_f = ((px_f - qx_f)**2 + (py_f - qy_f)**2)**0.5
    return result_f

def check_metastasis(distance):
    if(distance < 7 and distance > 0):
        print("metastasis")
    elif(distance < 14 and distance >= 7):
        print("suspicious")
    else:
        print("irrelevant")


px = int(input("Enter Px Point: "))
py = int(input("Enter Py Point: "))

qx = int(input("Enter Qx Point: "))
qy = int(input("Enter Qy Point: "))

result = calculate_euclidean(px, py, qx, qy)

check_metastasis(result)