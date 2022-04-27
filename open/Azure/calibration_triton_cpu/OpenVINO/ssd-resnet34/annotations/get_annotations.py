from pycocotools.coco import COCO
import requests
import csv
import json
import random


anno_file = 'cali_instances_train2017.json' # 'instances_train2017.json'
coco = COCO(anno_file)



all_image_ids = coco.getImgIds()

cali_file = 'cali.txt'

with open(cali_file) as f:
    cali_names = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
cali_names = [x.strip() for x in cali_names]





with open(anno_file) as json_file:
    data = json.load(json_file)
    #print(data['annotations'][0])
    #print(data['licenses'][0])
    #print(data['categories'][0])
    #print(data['info'])


cali_ids = list()
for item in data['images']:
    if item['file_name'] in cali_names:
        cali_ids.append(item['id'])

print(len(cali_ids)) # should be 500

# [457884, 277020, 79969, 288062, 166165, 484351, 84431, 84650, 223182, 246454, 433204, 577864, 506933, 90108, 185802, 372466, 159791, 161128, 152870, 575243, 176901, 389812, 184338, 139, 499768, 300842, 527784, 26690, 363188, 464089, 262631, 157756, 134096, 46872, 205776, 322352, 488251, 409211, 543581, 521141, 562229, 103548, 203864, 48924, 462643, 224337, 222118, 372718, 527427, 376322, 5193, 110972, 201072, 407083, 14380, 20333, 491008, 34257, 80413, 575815, 192871, 50145, 239857, 235064, 39785, 546823, 242946, 354547, 179141, 237864, 327769, 143961, 500826, 180798, 326970, 65736, 38825, 28993, 511453, 344059, 66231, 175364, 329219, 272049, 191845, 177893, 391140, 134856, 302990, 308394, 140076, 327605, 571857, 125405, 234366, 129135, 557884, 338901, 404534, 98853, 336356, 479248, 325991, 509258, 353051, 29596, 478393, 214224, 109827, 530457, 211825, 301421, 509403, 65455, 100428, 377368, 33221, 68933, 197796, 479155, 107554, 222863, 8211, 231097, 248334, 215644, 329455, 535523, 133819, 529966, 433103, 213033, 521405, 59920, 87476, 55167, 290843, 160772, 50149, 249550, 494634, 159458, 396200, 47740, 534270, 572555, 470924, 519764, 52007, 41872, 551215, 127530, 231088, 251824, 494188, 234757, 464522, 398905, 106563, 518326, 524456, 426203, 252507, 506178, 173008, 516038, 463849, 514376, 313034, 183104, 287545, 446206, 31248, 427655, 6894, 545007, 439623, 425390, 191672, 329827, 327601, 439290, 289516, 267670, 451308, 410735, 128654, 304291, 525247, 383838, 171050, 546219, 42276, 572620, 295713, 138819, 240940, 21465, 172877, 507015, 335328, 454978, 547519, 66926, 473406, 384661, 521601, 220310, 320554, 356531, 422836, 334767, 537812, 430073, 410428, 448448, 450075, 389566, 482100, 90284, 559348, 485424, 5037, 516804, 80949, 1268, 314034, 560178, 266768, 491613, 35770, 214192, 229997, 257566, 278848, 552612, 127182, 28809, 259382, 97585, 35062, 359833, 363666, 88485, 84674, 388927, 84752, 60835, 167540, 552902, 255401, 439522, 548780, 326128, 267191, 515025, 528705, 189451, 39551, 343937, 46048, 63047, 32887, 250127, 545407, 98261, 304365, 173799, 486104, 245311, 251537, 186282, 459757, 22396, 305609, 51712, 306437, 417043, 368982, 88265, 460841, 410496, 205647, 286660, 377486, 292446, 430377, 15335, 18491, 222299, 346968, 382111, 515077, 99428, 572408, 508101, 430875, 184791, 457848, 512657, 517056, 11511, 279145, 451571, 333745, 463802, 428867, 476491, 377497, 365745, 51738, 234779, 407868, 483050, 292908, 477955, 479912, 155291, 579307, 255912, 443498, 578871, 570782, 288430, 453001, 546717, 32285, 2431, 438876, 529105, 136600, 65485, 171757, 102411, 374727, 395388, 74092, 392228, 500477, 162858, 378244, 370900, 377882, 292997, 480021, 142092, 456143, 188906, 50679, 494863, 333069, 327890, 523194, 537506, 101762, 578967, 496409, 453841, 549930, 463199, 155451, 478721, 160556, 222455, 441468, 138979, 70158, 447465, 322429, 330396, 465129, 14038, 336209, 359855, 342295, 531135, 340015, 535094, 40757, 467176, 389532, 561335, 247806, 11615, 340272, 128658, 562121, 362434, 471893, 343496, 232649, 345027, 211674, 502168, 511384, 109976, 257896, 9378, 25386, 250901, 23126, 481413, 259640, 398810, 231237, 350405, 87144, 26465, 512776, 374052, 48555, 408696, 356612, 408830, 94336, 325838, 522940, 206411, 482719, 262938, 396338, 15254, 550426, 359135, 546659, 83113, 433515, 569825, 464251, 476704, 301981, 193494, 224200, 122606, 453302, 135604, 284279, 338219, 562581, 308391, 94326, 31322, 308753, 73533, 113051, 470779, 22705, 104455, 447611, 154000, 419408, 419379, 125778, 68078, 167067, 565469, 231822, 17714, 56350, 187362, 401244, 92091, 164602, 161032, 429109, 492905, 291619, 234807, 74646, 29984, 369757, 147338, 229659, 123321, 134034, 223955, 333402, 410712, 17627, 309655, 359781, 133000, 472030, 302882, 100723, 165831, 161044, 423798, 455981, 440617, 361551, 369675, 462728, 270066, 297578, 283717, 438269, 475904, 286994, 280710]
print('*******************************')


new_data = dict()

# process annotations
new_data['annotations'] = list()
for item in data['annotations']:
    if item['image_id'] in cali_ids:
        new_data['annotations'].append(item)


print(len(data['annotations']))
print(len(new_data['annotations']))
# 36781
# 3948
# it is about 1/10 so it makes sense.

# not saving licenses
# new_data['licenses'] = list()
# for item in data['licenses']:
#     if item['id'] in cali_ids:
#         new_data['licenses'].append(item)
# print(len(data['licenses']), len(new_data['licenses']))
#

# keep the categories:
new_data['categories'] = data['categories']
#
# process images
new_data['images'] = list()

for item in data['images']:
    if item['file_name'] in cali_names:
        new_data['images'].append(item)

print(len(data['images']), len(new_data['images']))
# 5000 500


# not saving info for now
# new_data['info'] = data['info']
#
with open('out_cali_instances_train2017.json', 'w') as outfile:
    json.dump(new_data, outfile)


print('Done!')











