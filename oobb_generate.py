import oobb
import oomB

def make_pl_all(overwrite=True):
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
    
    # larger plates of desire
    plates.append([15,9,3]) 
    
    #extra fives
    plates.append([15,5,3])
    plates.append([14,5,3])
    plates.append([13,5,3])
    plates.append([12,5,3])
    plates.append([11,5,3])
    plates.append([10,5,3])

    #extra fifteens
    plates.append([15,14,3])
    plates.append([15,13,3])
    plates.append([15,12,3])
    plates.append([15,11,3])

    for plate in plates:
        oobb.make_pl(plate[0],plate[1],plate[2],overwrite=overwrite)

def make_ci_all(overwrite=True):
    circles = []
    dias = [1,3,5,7,9,11,13,15,17,19,21,23,25]
    for dia in dias:
        circles.append([dia,3])
    
    for circle in circles:
        oobb.make_ci(circle[0],circle[1],overwrite=overwrite)

def make_all(overwrite=True):
    make_pl_all(overwrite=overwrite)
    make_ci_all(overwrite=overwrite)

def dxf_copy_to_laser():
    directory_base = r"parts"
    directory_laser= r'C:\DB\Dropbox\LALA-Laser Files\oobb'
    oomB.file_copy_search(directory_base,"laser-flat.dxf",output_dir=directory_laser)
