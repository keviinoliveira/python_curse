titulos = ["ADV2466","ADV2599","ADV2668","ADV2709","ADV2784","ADV2873","ADV2900","ADV2939","ADV2957","ADV2959","ADV2970","ADV2997","ADV4426","ADV4439","ADV4441","ADV4444","ADV4449","ADV4451","ADV4460","ADV4463","RES019/24","RES4423","RES4442","RES4452","RES4456"]
x = 0
print (len(titulos))
print(titulos)

for titulo in titulos:
    if (titulo.find("/") > 0):
        del titulos[x]
    x += 1

print(x)
print(titulos)

