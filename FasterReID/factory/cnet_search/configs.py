# -*- coding: utf-8 -*-
# @Author: solicucu

from yacs.config import CfgNode as CN 

_C = CN()

#------------------------------
# MODEL
# config for model paramter
#------------------------------

_C.MODEL = CN()
# use cpu or gpu to train
_C.MODEL.DEVICE = "cuda"
# specify the gpu device id if use gpu
_C.MODEL.DEVICE_IDS = "0"
# specify the num of cell in each stage
_C.MODEL.STAGES = [2, 2, 2]
# specify the channel in ecch stage
# _C.MODEL.PLANES = [32, 64, 128, 256]
_C.MODEL.PLANES = [64, 256, 384, 512]
# _C.MODEL.PLANES = [64, 128, 384, 512]
# float multiplier for scaling the model
_C.MODEL.MULTIPLIER = 1. 
# path to pretrained checkpoint
# _C.MODEL.PRETRAINED = "/home/share/solicucu/data/ReID/ReIDModels/csnet_search/market1501/checkpoints/csnet_softmax/"
_C.MODEL.PRETRAINED = ""
# whether use adaption fusion
_C.MODEL.ADAPTION_FUSION = True
# dim list for construct fc before classify
_C.MODEL.FC_DIMS = [512]

#--------------------------------
# DATA
# preprocess the data
#--------------------------------

_C.DATA = CN()
# which dataset to be use for training
_C.DATA.DATASET = "market1501"
# path to dataset
# _C.DATA.DATASET_DIR = "D:/project/data/"
_C.DATA.DATASET_DIR = "/home/share/solicucu/data/"


#--------------------------------
# DATALOADER
#--------------------------------

_C.DATALOADER = CN()
# number of threads to load data
_C.DATALOADER.NUM_WORKERS = 4
# how to sample the training data
_C.DATALOADER.SAMPLER = "triplet"
# number samples of each identity in one batch
_C.DATALOADER.NUM_INSTANCE = 4


#--------------------------------
# SOLVER
#--------------------------------

_C.SOLVER = CN()
# the max epoch to train the network
_C.SOLVER.MAX_EPOCHS = 120
# number of image in each batch
_C.SOLVER.BATCH_SIZE = 64

# lr
# the initial learning rate
# _C.SOLVER.BASE_LR = 0.065
_C.SOLVER.BASE_LR = 0.025
# the name of lr scheduler
_C.SOLVER.LR_SCHEDULER_NAME = "CosineAnnealingLR"
# minimum learning rate for CosineAnnealingLR
_C.SOLVER.LR_MIN = 0.0001
# _C.SOLVER.LR_MIN = 0.00065
# learning rate for train the architecture param alpha
_C.SOLVER.ARCH_LR = 3e-4
# the period for lerning decay
_C.SOLVER.LR_DECAY_PERIOD = 10
# learning rate decay fator
_C.SOLVER.LR_DECAY_FACTOR = 0.1

# optimizer
# the name of the optimizer
_C.SOLVER.OPTIMIZER_NAME = "SGD"
# momentum for optimizer
_C.SOLVER.MOMENTUM = 0.9
# weight decay for optimizer
_C.SOLVER.WEIGHT_DECAY = 3e-4
# weight decay factor for architecture
_C.SOLVER.ARCH_WEIGHT_DECAY = 1e-3

# loss 
# choices: softmax, triplet, softmax_triplet
_C.SOLVER.LOSS_NAME = "softmax_triplet"
# margin for triplet loss if use triplet loss
_C.SOLVER.TRI_MARGIN = 0.3 

# other
# use one-step unrolled validation loss
_C.SOLVER.UNROLLED = True
# gradient clipping if grad_clip is not a zero
_C.SOLVER.GRAD_CLIP = 0.
# rand seed
_C.SOLVER.SEED = 6

#--------------------------------
# OUTPUT
#--------------------------------

_C.OUTPUT = CN()
# path to output
# _C.OUTPUT.DIRS = "D:/project/data/ReID/FasterReID/market1501/cnet_search/"
_C.OUTPUT.DIRS = "/home/share/solicucu/data/ReID/FasterReID/market1501/cnet_search/"
# path to save the checkpoint
_C.OUTPUT.CKPT_DIRS = "checkpoints/cnet_blneck/"
# specify a name for log
_C.OUTPUT.LOG_NAME = "log_search_cnet_blneck.txt"
# the period for log
_C.OUTPUT.LOG_PERIOD = 10
# the period for saving the checkpoint
_C.OUTPUT.CKPT_PERIOD = 10
# the period for validatio
_C.OUTPUT.EVAL_PERIOD = 20
