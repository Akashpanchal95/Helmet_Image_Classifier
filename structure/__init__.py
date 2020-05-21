# from PIL import Image
#
# i1 = Image.open(r"E:\IRCTC_DATA\katpadi_Packing_FinalData\7486756_20180404_090017____PERSON\crop_5.jpg")
# i2 = Image.open(r"E:\IRCTC_DATA\katpadi_Packing_FinalData\7486756_20180404_090017____PERSON\crop_65.jpg")
# #assert i1.mode == i2.mode, "Different kinds of images."
# #assert i1.size == i2.size, "Different sizes."
#
# pairs = zip(i1.getdata(), i2.getdata())
# if len(i1.getbands()) == 1:
#     # for gray-scale jpegs
#     dif = sum(abs(p1 - p2) for p1, p2 in pairs)
# else:
#     dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))
#
# ncomponents = i1.size[0] * i1.size[1] * 3
# print("Difference (percentage):", (dif / 255.0 * 100) / ncomponents)

ls = [0,1,8,3,4,5]

del ls[-3:]

print(ls)

for i in range(4):
    print(i)