# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class ANBOX_ALTRA_MAX_AX1_A10_X1(SingleStreamGPUBaseConfig):
    system = KnownSystem.anbox_altra_max_ax1_a10_x1
    audio_buffer_num_lines = 1
    single_stream_expected_latency_ns = 10000000
    nouse_copy_kernel = False

