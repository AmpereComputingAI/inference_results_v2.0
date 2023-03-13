# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class ANBOX_ALTRA_MAX_AX1_A10_X1(SingleStreamGPUBaseConfig):
    system = KnownSystem.anbox_altra_max_ax1_a10_x1
    enable_interleaved = False
    gemm_plugin_fairshare_cache_size = 120
    single_stream_expected_latency_ns = 1700000


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class ANBOX_ALTRA_MAX_AX1_A10_X1_Triton(ANBOX_ALTRA_MAX_AX1_A10_X1):
    use_triton = True


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class ANBOX_ALTRA_MAX_AX1_A10_X1_HighAccuracy(ANBOX_ALTRA_MAX_AX1_A10_X1):
    precision = "fp16"
    single_stream_expected_latency_ns = 1700000


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class ANBOX_ALTRA_MAX_AX1_A10_X1_HighAccuracy_Triton(ANBOX_ALTRA_MAX_AX1_A10_X1_HighAccuracy):
    use_triton = True

