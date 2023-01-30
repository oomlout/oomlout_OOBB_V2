import oobb


def make_pl_all():
    plates = []
    for wid in range(1,7):
        for hei in range(1,7):
            if wid >= hei:
                plates.append([wid,hei,3])
    
    plates.append([1,1,6])    
    plates.append([1,1,9])    
    plates.append([1,1,12])   

    plates.append([7,1,3])    
    plates.append([8,1,3])    
    plates.append([9,1,3])    
    plates.append([10,1,3])    
    plates.append([11,1,3])    
    plates.append([14,1,3])    
    plates.append([15,1,3])    
    plates.append([20,1,3])    
    plates.append([25,1,3])    
    
    plates.append([7,3,3])    
    plates.append([8,3,3])    
    plates.append([9,3,3])    
    
    plates.append([7,5,3])    
    plates.append([8,5,3])    
    plates.append([9,5,3])    


    plates.append([12,12,3])    
    plates.append([14,14,3])   
    plates.append([15,15,3])     
    plates.append([20,20,3])   
    
    for plate in plates:
        oobb.make_pl(plate[0],plate[1],plate[2])


make_pl_all()        