def formatx(text):
    data = text.replace(",",".")
    data = data.split(" ")

    data_refined = []
    x = []
    y = []

    for i in data:
        try:
            temp = float(i)
            data_refined.append(i)
        except ValueError:
            pass

    for i in range(len(data_refined)):
        if i%2 == 0:
            x.append(data_refined[i])
        else:
            y.append(data_refined[i])

    return x


def formaty(text):
    data = text.replace(",",".")
    data = data.split(" ")

    data_refined = []
    x = []
    y = []

    for i in data:
        try:
            temp = float(i)
            data_refined.append(i)
        except ValueError:
            pass

    for i in range(len(data_refined)):
        if i%2 == 0:
            x.append(data_refined[i])
        else:
            y.append(data_refined[i])

    return y

def rotate(arr, n):
    return arr[n:] + arr[:n]


def formatdata():
    data_input = input("enter data :\n")
    data_input = data_input.split("FIELD")
    print(f"------------{data_input[1]}")
    a = data_input[1]
    a = a.split("CURVE")
    a = a[1::]
    
    a = [item.split("PART") for item in a]

    temp_refined_x = []
    temp_refined_y = []
    
    for i in range(len(a)):
        a[i] = a[i][1::]
        for j in range(len(a[i])):
            temp_refined_x.append(formatx(str(a[i][j])))
            temp_refined_y.append(formaty(str(a[i][j])))

    for j in range(len(temp_refined_x)):
        if temp_refined_x[j][0] == "0":
            temp_refined_x[j] = rotate(temp_refined_x[j], 1)
            temp_refined_y[j] = rotate(temp_refined_y[j], 1)
    
    temp_refined_x = str(temp_refined_x).replace("'","")
    temp_refined_y = str(temp_refined_y).replace("'","")

    return temp_refined_x, temp_refined_y

