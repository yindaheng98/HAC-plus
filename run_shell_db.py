import os

for lmbda in [0.004]:  # Optionally, you can try: 0.003, 0.002, 0.001, 0.0005
    for cuda, scene in enumerate([
        'basketball/frame1',
        'boxes/frame1',
        'football/frame1',
        'flame_salmon_1/frame1',
        'flame_steak/frame1',
        'sear_steak/frame1',
    ]):
        mask_lr_final = 0.00008 * lmbda / 0.001
        one_cmd = f'python train.py -s data/{scene} --eval --lod 0 --voxel_size 0.005 --update_init_factor 16 --iterations 30_000 -m outputs/{scene}/{lmbda} --lmbda {lmbda} --mask_lr_final {mask_lr_final}'
        os.system(one_cmd)
