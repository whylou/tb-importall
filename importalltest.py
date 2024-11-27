import mset
sceneMaterials = mset.getAllMaterials()
""" print(sceneMaterials[1].name)
print(sceneMaterials[1].setSubroutine('Emissive', 'Emissive')) """
print(sceneMaterials[0].getSubroutine('Reflectivity').getFieldNames())