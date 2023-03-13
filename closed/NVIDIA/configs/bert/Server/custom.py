# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class ANBOX_ALTRA_MAX_AX1_A10_X1(ServerGPUBaseConfig):
    system = KnownSystem.anbox_altra_max_ax1_a10_x1
    active_sms = 60
    gpu_batch_size = 48
    graphs_max_seqlen = 200
    server_num_issue_query_threads = 1
    server_target_qps = 1875
    soft_drop = 0.99
    use_small_tile_gemm_plugin = True


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class ANBOX_ALTRA_MAX_AX1_A10_X1_HighAccuracy(ANBOX_ALTRA_MAX_AX1_A10_X1):
    precision = "fp16"
    gpu_batch_size = 24
    server_target_qps = 1625


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class ANBOX_ALTRA_MAX_AX1_A10_X1_Triton(ANBOX_ALTRA_MAX_AX1_A10_X1):
    server_target_qps = 1750
    use_triton = True


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class ANBOX_ALTRA_MAX_AX1_A10_X1_HighAccuracy_Triton(ANBOX_ALTRA_MAX_AX1_A10_X1_HighAccuracy):
    server_target_qps = 1500
    use_triton = True

