import mset
""" sceneMaterials = mset.getAllMaterials()
Mat=sceneMaterials[0]
print(sceneMaterials[1].name)
print(sceneMaterials[1].setSubroutine('Emissive', 'Emissive'))
print(sceneMaterials[0].getSubroutine('Reflectivity').getFieldNames())
print(sceneMaterials[0].getSubroutine('Reflectivity').getField('Metalness'))
tex = mset.Texture("E:/tietu/importalltesttex/importtext3/tex1_Metalness.png")
tex.sRGB=False
shader = Mat.getSubroutine('Reflectivity')
shader.setField('Metalness', 1.0)
shader.setField('Metalness Map', tex)
Mat.setSubroutine('Transmission','Subsurface Scattering')
if not Mat.getSubroutine('Transmission'):
    print("open failed")
shader=Mat.getSubroutine('Transmission')
print(shader.name)
print(Mat.getSubroutine('Transmission').getFieldNames())
 """
import time

# 记录起始时间
start_time = time.time()

# 要测量的代码块
for i in range(1000000):
    pass

# 记录结束时间
end_time = time.time()

# 计算执行时间
execution_time = end_time - start_time
print(f"程序执行时间: {execution_time:.6f} 秒")
