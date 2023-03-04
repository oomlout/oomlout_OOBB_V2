import oobb
import oobb_generate
import oomB


#oobb_generate.make_pl_all()
width = 15        
height = 14
thickness = 3
#oobb.make_pl(width,height,thickness)
width = 15        
height = 13
thickness = 3
#oobb.make_pl(width,height,thickness)

width = 15        
height = 12
thickness = 3
#oobb.make_pl(width,height,thickness)
width = 15        
height = 11
thickness = 3
#oobb.make_pl(width,height,thickness)
width = 15        
height = 9
thickness = 3
#oobb.make_pl(width,height,thickness)
width = 15        
height = 5
thickness = 3
#oobb.make_pl(width,height,thickness)
width = 14
height = 5
thickness = 3
#oobb.make_pl(width,height,thickness)
width = 13        
height = 5
thickness = 3
#oobb.make_pl(width,height,thickness)

diameter = 3        
thickness = 3
#oobb.make_ci(diameter,thickness)

#oobb_generate.make_ci_all()

overwrite = False
oobb_generate.make_all(overwrite=overwrite)

#oobb_generate.dxf_copy_to_laser()