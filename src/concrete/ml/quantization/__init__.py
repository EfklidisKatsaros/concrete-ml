"""Modules for quantization."""
from .base_quantized_op import QuantizedOp
from .post_training import (
    PostTrainingAffineQuantization,
    PostTrainingQATImporter,
    get_n_bits_dict,
    _get_n_bits_dict_trees,
    _inspect_tree_n_bits,
)
from .quantized_module import QuantizedModule
from .quantized_ops import (
    QuantizedAbs,
    QuantizedAdd,
    QuantizedAvgPool,
    QuantizedBatchNormalization,
    QuantizedBrevitasQuant,
    QuantizedCelu,
    QuantizedClip,
    QuantizedConv,
    QuantizedDiv,
    QuantizedElu,
    QuantizedErf,
    QuantizedExp,
    QuantizedGemm,
    QuantizedGreater,
    QuantizedGreaterOrEqual,
    QuantizedHardSigmoid,
    QuantizedHardSwish,
    QuantizedIdentity,
    QuantizedLeakyRelu,
    QuantizedLess,
    QuantizedLessOrEqual,
    QuantizedLog,
    QuantizedMatMul,
    QuantizedMaxPool,
    QuantizedMul,
    QuantizedOr,
    QuantizedPad,
    QuantizedPow,
    QuantizedPRelu,
    QuantizedReduceSum,
    QuantizedRelu,
    QuantizedReshape,
    QuantizedRound,
    QuantizedSelu,
    QuantizedSigmoid,
    QuantizedSoftplus,
    QuantizedSub,
    QuantizedTanh,
    QuantizedWhere,
)
from .quantizers import QuantizedArray
