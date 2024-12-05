##思路：自动查询场景中所有材质，加入列表。手动选择材质所在文件夹，按照贴图名称查询对应材质，并将其赋予对应材质，一键导入。
import mset
import os
import time
starttime=time.time()
#材质属性关键词列表
MaterialType=['Normal','Albedo','Roughness','Metalness','Occlusion','Mask','Emissive','Alpha']
SubroutineType=['Surface','Albedo','Microsurface','Reflectivity','Occlusion','Transmission','Emissive','Transparency']
#将检索到的贴图文件放入对应插槽
def ImportTex(Path,Mat,keyword1,keyword2):#keyword1表示材质名称，keyword2表示插槽名称，即贴图类型
    if not Mat.getSubroutine(SubroutineType[MaterialType.index(keyword2)]):
        if keyword2=='Mask':
            Mat.setSubroutine(SubroutineType[MaterialType.index(keyword2)],'Subsurface Scattering')#打开对应通道
        elif keyword2=='Alpha':
            Mat.setSubroutine(SubroutineType[MaterialType.index(keyword2)],'Dither')#打开对应通道
        else:
            Mat.setSubroutine(SubroutineType[MaterialType.index(keyword2)],keyword2)#打开对应通道
    shader = Mat.getSubroutine(SubroutineType[MaterialType.index(keyword2)])#根据通道名获取通道对象
    tex = mset.Texture(Path + "/" + keyword1 + "_" + keyword2 + ".png")
    tex.useMipmaps=True
    if shader:
        if keyword2 == 'Roughness' or keyword2 == 'Metalness':
            shader.setField(keyword2, 1.0)
        if keyword2 == 'Occlusion':
            shader.setField(keyword2, 0.4)
        if keyword2 in ('Albedo','Emissive'):
            tex.sRGB=True
        shader.setField(keyword2+" Map", tex)
    else:
        print('NoneType')
#关键字查询
def FindFilesByKeywords(FloderPath,list1,list2):
    for root, dirs, files in os.walk(FloderPath):
        for file in files:
            # 检查文件名是否包含所有关键字
            if os.path.isfile(os.path.join(FloderPath,file)):
                for keyword1 in list1:
                    if keyword1 in file:
                        for keyword2 in list2:
                            if keyword2 in file:
                                ImportTex(FloderPath,mset.findMaterial(keyword1),keyword1,keyword2)
#创建一键导入窗口
mywindow = mset.UIWindow("ImportAll")
#一键导入功能实现
def doSomething():
    # 获取场景内所有材质，装入列表
    sceneMaterials = mset.getAllMaterials()
    print("sceneMaterials set")
    """ for M in sceneMaterials:
        print(M.name + ';') """
    sceneMaterialsName=[]
    for Mat in sceneMaterials:
        sceneMaterialsName.append(Mat.name)
    ChooseFloder=mset.showOpenFolderDialog()#弹出窗口选择贴图所在文件夹
    if ChooseFloder:
        FindFilesByKeywords(ChooseFloder,sceneMaterialsName,MaterialType)
        endtime=time.time()
        totaltime=endtime-starttime
        print(str(totaltime) + 'S')
        print("Import finish")
    else:
        print("no choose floder")
    mset.shutdownPlugin() # exit the plugin
#创建选择文件夹的按钮
mybutton = mset.UIButton("select tex floder")
mybutton.onClick = doSomething
#把按钮添加到窗口中
mywindow.addElement( mybutton )