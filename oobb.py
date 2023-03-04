import opsc 

os = 15             # spacing between holes
os_minus = 1        # amount to take off between sheets (at 1 OOBB 3 = 44 mm)
os_hole = "M6"      # defaulthole size
oobb_save_type = "none"
oobb_save_type = "all"

def make_pl(width,height,depth=3,overwrite=True):
    
    modes = ["laser", "3d_print"]
    for mode in modes:
        objects=[]
        opsc.set_mode(mode)
        width_mm = (width * os) - os_minus
        height_mm = (height * os) - os_minus
        depth_mm = depth
        x = width_mm/2 + os_minus/2
        y = height_mm/2 + os_minus/2
        objects.append(opsc.opsc_easy("positive", "rounded_rectangle", size=[width_mm, height_mm, depth_mm], pos=[x,y,0]))
        objects.extend(opsc.opsc_easy_array("negative", "hole", repeats=[width,height], pos_start = [os/2,os/2], shift_arr = [os,os], r=os_hole ))
        type = "pl"
        opsc.opsc_make_object('parts/' + type + "_" + str(width).zfill(2) + "_" + str(height).zfill(2) + "_" + str(depth).zfill(2) + "/" + mode + ".scad", objects, mode=mode,save_type=oobb_save_type, overwrite=overwrite)


def make_ci(diameter,depth=3, overwrite=True):
    modes = ["laser", "3d_print"]
    for mode in modes:
        objects=[]
        opsc.set_mode(mode)
        diameter_mm = (diameter * os) - os_minus
        depth_mm = depth
        #x = diameter_mm/2 + os_minus/2        
        #y = diameter_mm/2 + os_minus/2
        x=0
        y=0
        objects.append(opsc.opsc_easy("positive", "cylinder", r=diameter_mm/2, h=depth_mm, pos=[x,y,0]))

        center=True

        diameter_mm_holes = diameter_mm - 10
        for i in range(0,diameter):
            for j in range(0,diameter):
                x = -(diameter-1)/2*os + i*os
                y = -(diameter-1)/2*os + j*os
                if(x*x + y*y) <= (diameter_mm_holes/2)**2:
                    pos = [x,y,0]
                    objects.append(opsc.opsc_easy("negative", "hole", r=os_hole, pos=pos, center=center))
                
                #add holes in corners for ci_03
                if diameter == 3:
                    positions = [[10.607,10.607,0],[10.607,-10.607,0],[-10.607,10.607,0],[-10.607,-10.607,0]]
                    for pos in positions:
                        objects.append(opsc.opsc_easy("negative", "hole", r=os_hole, pos=pos, center=center))


        typ="ci"
        opsc.opsc_make_object(f'parts/{typ}_{str(diameter).zfill(2)}_{str(depth).zfill(2)}/{mode}.scad', objects, mode=mode,save_type=oobb_save_type, overwrite=overwrite)

        
