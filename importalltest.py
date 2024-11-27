import mset
Mat.setSubroutine('Emmision','Emmisive')
tex = mset.Texture(Path)
if keyword2!='Normal':
    tex.sRGB=True
    tex.useMipmaps=True
if shader:
    shader.setField("Emmisive Map", tex)