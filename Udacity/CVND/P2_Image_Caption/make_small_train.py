import numpy as np
import os
import sys
import tqdm
import json

from collections import defaultdict

def make_img_anno_pairs(annotations):
  result = defaultdict(list)  # key=image_id, value=annotation list
  for anno in annotations:
    result[anno['image_id']].append(anno)
  return result

def small_train(anno_loc, in_file_name, image_num, save=True, out_file_name=None):
  in_file = os.path.join(anno_loc, in_file_name)
  dataset = None
  with open(in_file, 'r') as in_f:
    dataset = json.load(in_f)
    assert type(dataset)==dict, 'annotation file format {} not supported'.format(type(dataset))

  result = {'licenses': dataset['licenses'], 'info': dataset['info'], 'images': [], 'annotations': []}

  # Getting `image_num` images and their annotations.
  total_images = dataset['images']
  np.random.shuffle(total_images)
  random_imgs = total_images[:image_num]
  total_annotations = make_img_anno_pairs(dataset['annotations'])

  for image_anno in tqdm.tqdm(random_imgs):
    result['images'].append(image_anno)
    result['annotations'].extend(total_annotations[image_anno['id']])
  
  
    out_file = os.path.join(anno_loc, out_file_name)
    with open(out_file, 'w') as out_f:
      json.dump(result, out_f)
  print("Created {} images with {} annotations to {}...".format(len(result['images']), len(result['annotations']), out_file))
  return result

if __name__ == '__main__':
  n_img = 10
  if len(sys.argv) > 1:
    n_img = int(sys.argv[1])
  COCOPATH = '/home/zafar/Desktop/Data/COCO' if os.environ['USER'] == 'zafar' else '/opt/cocoapi'
  COCODATA = os.path.join(COCOPATH, 'annotations')
  small_train(anno_loc = COCODATA, in_file_name = 'captions_train2014.json', out_file_name = 'captions_train2014_small.json', image_num = n_img)