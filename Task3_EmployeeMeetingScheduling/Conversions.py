def hrToMinString(str):

    strSplit = str.split(":")
    hours = int(strSplit[0])
    minutes = int(strSplit[1])

    retMinutes = hours * 60 + minutes

    return int(retMinutes)


def hrToMinInteger(inte):

    inteStr = inte.split(".")
    inteFirst = int(inteStr[0])
    inteSecond = int(inteStr[1])
    inteTotal = inteFirst * 60 + inteSecond/100 * 60

    print(inteTotal)
    return (inteTotal)


def minutesToHours(inte):
    varMin = (inte % 60)/60
    varHours = inte//60
    varTotal = varMin + varHours

    return varTotal

