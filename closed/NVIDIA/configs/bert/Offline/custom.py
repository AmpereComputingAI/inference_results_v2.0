# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class ANBOX_ALTRA_MAX_AX1_A10_X1(OfflineGPUBaseConfig):
    system = KnownSystem.anbox_altra_max_ax1_a10_x1
    use_small_tile_gemm_plugin = True
    gemm_plugin_fairshare_cache_size = 120
    gpu_batch_size = 1024
    offline_expected_qps = 3400
    workspace_size = 7516192768


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class ANBOX_ALTRA_MAX_AX1_A10_X1_Triton(ANBOX_ALTRA_MAX_AX1_A10_X1):
    use_triton = True


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class ANBOX_ALTRA_MAX_AX1_A10_X1_HighAccuracy(ANBOX_ALTRA_MAX_AX1_A10_X1):
    precision = "fp16"
    offline_expected_qps = 1950


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class ANBOX_ALTRA_MAX_AX1_A10_X1_HighAccuracy_Triton(ANBOX_ALTRA_MAX_AX1_A10_X1_HighAccuracy):
    use_triton = True

