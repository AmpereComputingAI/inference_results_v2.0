# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class ANBOX_ALTRA_MAX_AX1_A10_X1(ServerGPUBaseConfig):
    system = KnownSystem.anbox_altra_max_ax1_a10_x1
    gpu_copy_streams = 4
    use_deque_limit = True
    deque_timeout_usec = 30000
    gpu_batch_size = 8
    gpu_inference_streams = 2
    server_target_qps = 770


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class ANBOX_ALTRA_MAX_AX1_A10_X1_Triton(ANBOX_ALTRA_MAX_AX1_A10_X1):
    use_triton = True

