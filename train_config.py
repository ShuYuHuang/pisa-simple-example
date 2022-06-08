# The new config inherits a base config to highlight the necessary modification
_base_ = ['pisa_faster_rcnn_x101_32x4d_fpn_1x_coco.py']

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=13)),
    train_cfg=dict(
        rpn_proposal=dict(
            nms_pre=200,
            max_per_img=200)),
    test_cfg=dict(
        rpn=dict(
            nms_pre=200,
            max_per_img=200))
)
# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('bishop',
'black-bishop',
 'black-king',
 'black-knight',
 'black-pawn',
 'black-queen',
 'black-rook',
 'white-bishop',
 'white-king',
 'white-knight',
 'white-pawn',
 'white-queen',
 'white-rook')
data_root = 'data/coco/'

data = dict(
    train=dict(
        img_prefix='data/coco/train/',
        classes=classes,
        ann_file='data/coco/train/_annotations.coco.json'),
    val=dict(
        img_prefix='data/coco/valid/',
        classes=classes,
        ann_file='data/coco/valid/_annotations.coco.json'),
    test=dict(
        img_prefix='test/',
        classes=classes,
        ann_file='data/coco/test/_annotations.coco.json',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(
                type='MultiScaleFlipAug',
                img_scale=(1333, 800),
                flip=False,
                transforms=[
                    dict(type='Resize', keep_ratio=True),
                    dict(type='RandomFlip'),
                    dict(
                        type='Normalize',
                        mean=[123.675, 116.28, 103.53],
                        std=[58.395, 57.12, 57.375],
                        to_rgb=True),
                    dict(type='Pad', size_divisor=32),
                    dict(type='ImageToTensor', keys=['img']),
                    dict(type='Collect', keys=['img'])
                ])
        ]))