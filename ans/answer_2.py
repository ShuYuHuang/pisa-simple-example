# 前面先include base config
_base_ = ['pisa_chess.py']
# 要求改NMS
model = dict(
    train_cfg=dict(
        rpn_proposal=dict(
            nms_pre=2000,
            max_per_img=2000)),
    test_cfg=dict(
        rpn=dict(
            nms_pre=2000,
            max_per_img=2000))
)
optimizer = dict(lr=0.02)
runner = dict(max_epochs=20)