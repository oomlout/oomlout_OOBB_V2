import opsc 

os = 15             # spacing between holes
os_minus = 1        # amount to take off between sheets (at 1 OOBB 3 = 44 mm)
os_hole = "M6"      # defaulthole size
oobb_save_type = "none"
oobb_save_type = "all"

def make_pl(width,height,depth=3):
    pass

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
        type = "PL"
        opsc.opsc_make_object('parts/' + type + '/' + type + "-" + str(width).zfill(2) + "-" + str(height).zfill(2) + "-" + str(depth).zfill(2) + "/" + mode + ".scad", objects, mode=mode,save_type=oobb_save_type)



