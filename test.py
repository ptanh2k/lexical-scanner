def read_file(path):
    x = 0
    with open(path) as f:
        data=  f.readlines()
        data = [i.strip() for i in data]
        ar = []
        while x < len(data):
        # for x in range(len(data)):
            if "//" in data[x]:
                ar.append(data[x].strip())
                pass

            elif "/" in data[x]:
                token = ""
                for j in range(x, len(data)):
                    token += str(data[x].strip()) 
                    x += 1 
                    if("/" in data[x]):
                        token += str(data[x].strip()) 
                        x += 1 
                        break
                ar.append(token)
            else:
                data[x] = data[x].strip()
                data[x] = data[x].split(' ')
                for i in data[x]:
                    if ";" in i:
                        token = [i[:len(i)-1], i[-1]]
                        for j in token:
                            ar += j
                    elif "," in i: 
                        token = [i[:len(i)-1], i[-1]]
                        for j in token:
                            ar += j
                    else:
                        ar.append(str(i))
            x = x + 1
    return ar

print(read_file('./input.vc'))