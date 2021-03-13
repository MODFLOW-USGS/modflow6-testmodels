import os

ims_pths = []
for root, dirs, files in os.walk(".."):
   for name in files:
       if name.lower().endswith(".ims") or name.lower().endswith(".ims6"):
           pth = os.path.join(root, name)
           ims_pths.append(pth)

replace_dict = {
    "inner_hclose": "inner_dvclose",
    "outer_hclose": "outer_dvclose",

}

for idx, pth in enumerate(ims_pths):
    print("{:3d}: {}".format(idx + 1, pth))
    with open(pth) as f:
        lines = f.read().splitlines()

        f = open(pth, "w")
        for line in lines:
            for text0, text1 in replace_dict.items():
                line = line.lower().replace(text0, text1)
            f.write("{}\n".format(line))
        f.close()
