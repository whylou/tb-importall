import mset
sceneMaterials = mset.getAllMaterials()
Mat=sceneMaterials[0]
""" print(sceneMaterials[1].name)
print(sceneMaterials[1].setSubroutine('Emissive', 'Emissive'))
print(sceneMaterials[0].getSubroutine('Reflectivity').getFieldNames())
print(sceneMaterials[0].getSubroutine('Reflectivity').getField('Metalness'))
tex = mset.Texture("E:/tietu/importalltesttex/importtext3/tex1_Metalness.png")
tex.sRGB=False
shader = Mat.getSubroutine('Reflectivity')
shader.setField('Metalness', 1.0)
shader.setField('Metalness Map', tex) """
Mat.setSubroutine('Transmission','Subsurface Scattering')
if not Mat.getSubroutine('Transmission'):
    print("open failed")
""" shader=Mat.getSubroutine('Transmission')
print(shader.name)
print(Mat.getSubroutine('Transmission').getFieldNames()) """