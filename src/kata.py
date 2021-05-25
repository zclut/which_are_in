def in_array(array1, array2):
    result = []
    longArray = array1 if (len(array1) > len(array2)) else array2
    shortArray = array1 if (len(array1) < len(array2)) else array2
    
    if len(shortArray) == 0:
        return result

    for index in range(len(array1)):
        # Comparamos el indice actual con cada uno de los de longArray
        if any(array1[index] in string for string in longArray):
            result.append(array1[index])
    
    # Ordenamos el resultado y eliminamos valores repetidos
    result = list(set(result))
    result.sort()

    return result
