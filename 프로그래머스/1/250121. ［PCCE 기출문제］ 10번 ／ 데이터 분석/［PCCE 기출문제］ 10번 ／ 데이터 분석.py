def solution(data, ext, val_ext, sort_by):
    answer = [[]]  
    composition = ["code", "date", "maximum", "remain"]
    sel_data = []
    
    for i in range(len(data)):
        code = data[i][0]
        date = data[i][1]
        maximum = data[i][2]
        remain = data[i][3]
        
        if ext == "date":
            if date < val_ext:
                sel_data.append(data[i])
        elif ext == "code":
            if code < val_ext:
                sel_data.append(data[i])
        elif ext == "maximum":
            if maximum < val_ext:
                sel_data.append(data[i])
        elif ext == "remain":
            if remain < val_ext:
                sel_data.append(data[i])
                
    for i in range(len(composition)):
        if sort_by == composition[i]:
            sel_data.sort(key=lambda x:x[i])
    
    answer = sel_data
    
    return answer