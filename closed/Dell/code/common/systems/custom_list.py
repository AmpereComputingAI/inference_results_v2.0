# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import annotations

import os

from code.common.constants import *
from code.common.systems.base import *
from code.common.systems.accelerator import AcceleratorConfiguration, GPU, MIG
from code.common.systems.cpu import CPUConfiguration, CPU
from code.common.systems.memory import MemoryConfiguration
from code.common.systems.systems import SystemConfiguration
from code.common.systems.known_hardware import *


custom_systems = dict()


# Do not manually edit any lines below this. All such lines are generated via scripts/add_custom_system.py

###############################
### START OF CUSTOM SYSTEMS ###
###############################

custom_systems['R750xa_A100_PCIE_80GBx4'] = SystemConfiguration(host_cpu_conf=CPUConfiguration(layout={CPU(name="Intel(R) Xeon(R) Gold 6338 CPU @ 2.00GHz", architecture=CPUArchitecture.x86_64, core_count=32, threads_per_core=2): 2}), host_mem_conf=MemoryConfiguration(host_memory_capacity=Memory(quantity=527.8026600000001, byte_suffix=ByteSuffix.GB), comparison_tolerance=0.05), accelerator_conf=AcceleratorConfiguration(layout={KnownGPU.A100_PCIe_80GB.value: 4}), numa_conf=None, system_id="R750xa_A100_PCIE_80GBx4")
custom_systems['XE2420_A30x1'] = SystemConfiguration(host_cpu_conf=CPUConfiguration(layout={CPU(name="Intel(R) Xeon(R) Silver 4216 CPU @ 2.10GHz", architecture=CPUArchitecture.x86_64, core_count=16, threads_per_core=1): 2}), host_mem_conf=MemoryConfiguration(host_memory_capacity=Memory(quantity=65.575144, byte_suffix=ByteSuffix.GB), comparison_tolerance=0.05), accelerator_conf=AcceleratorConfiguration(layout={KnownGPU.A30.value: 1}), numa_conf=None, system_id="XE2420_A30x1")
custom_systems['XE2420_T4x1'] = SystemConfiguration(host_cpu_conf=CPUConfiguration(layout={CPU(name="Intel(R) Xeon(R) Gold 6238 CPU @ 2.10GHz", architecture=CPUArchitecture.x86_64, core_count=22, threads_per_core=2): 2}), host_mem_conf=MemoryConfiguration(host_memory_capacity=Memory(quantity=262.70808, byte_suffix=ByteSuffix.GB), comparison_tolerance=0.05), accelerator_conf=AcceleratorConfiguration(layout={GPU(name="Tesla T4", accelerator_type=AcceleratorType.Discrete, vram=Memory(quantity=14.7548828125, byte_suffix=ByteSuffix.GiB), max_power_limit=70.0, pci_id="0x1EB810DE", compute_sm=75): 1}), numa_conf=None, system_id="XE2420_T4x1")
custom_systems['XE2420_1xT4_edge'] = SystemConfiguration(host_cpu_conf=CPUConfiguration(layout={CPU(name="Intel(R) Xeon(R) Gold 6238 CPU @ 2.10GHz", architecture=CPUArchitecture.x86_64, core_count=22, threads_per_core=2): 2}), host_mem_conf=MemoryConfiguration(host_memory_capacity=Memory(quantity=262.70808, byte_suffix=ByteSuffix.GB), comparison_tolerance=0.05), accelerator_conf=AcceleratorConfiguration(layout={GPU(name="Tesla T4", accelerator_type=AcceleratorType.Discrete, vram=Memory(quantity=14.7548828125, byte_suffix=ByteSuffix.GiB), max_power_limit=70.0, pci_id="0x1EB810DE", compute_sm=75): 1}), numa_conf=None, system_id="XE2420_1xT4_edge")
custom_systems['XE8545_A100_SXM_80GB_1xMIG'] = SystemConfiguration(host_cpu_conf=CPUConfiguration(layout={CPU(name="AMD EPYC 7763 64-Core Processor", architecture=CPUArchitecture.x86_64, core_count=64, threads_per_core=2): 2}), host_mem_conf=MemoryConfiguration(host_memory_capacity=Memory(quantity=1.056401536, byte_suffix=ByteSuffix.TB), comparison_tolerance=0.05), accelerator_conf=AcceleratorConfiguration(layout={MIG(name="NVIDIA A100-SXM4-80GB MIG-1g.10gb", accelerator_type=AcceleratorType.Discrete, vram=Memory(quantity=10, byte_suffix=ByteSuffix.GiB), max_power_limit=500.0, pci_id="0x20B210DE", compute_sm=80, num_gpcs=1): 1}), numa_conf=None, system_id="XE8545_A100_SXM_80GB_1xMIG")
custom_systems['XE8545_A100_SXM_80GBx1'] = SystemConfiguration(host_cpu_conf=CPUConfiguration(layout={CPU(name="AMD EPYC 7763 64-Core Processor", architecture=CPUArchitecture.x86_64, core_count=64, threads_per_core=2): 2}), host_mem_conf=MemoryConfiguration(host_memory_capacity=Memory(quantity=1.056401536, byte_suffix=ByteSuffix.TB), comparison_tolerance=0.05), accelerator_conf=AcceleratorConfiguration(layout={GPU(name="NVIDIA A100-SXM4-80GB", accelerator_type=AcceleratorType.Discrete, vram=Memory(quantity=80.0, byte_suffix=ByteSuffix.GiB), max_power_limit=500.0, pci_id="0x20B210DE", compute_sm=80): 1}), numa_conf=None, system_id="XE8545_A100_SXM_80GBx1")
custom_systems['XE8545_A100_SXM_80GBx4'] = SystemConfiguration(host_cpu_conf=CPUConfiguration(layout={CPU(name="AMD EPYC 7763 64-Core Processor", architecture=CPUArchitecture.x86_64, core_count=64, threads_per_core=2): 2}), host_mem_conf=MemoryConfiguration(host_memory_capacity=Memory(quantity=1.056401536, byte_suffix=ByteSuffix.TB), comparison_tolerance=0.05), accelerator_conf=AcceleratorConfiguration(layout={GPU(name="NVIDIA A100-SXM4-80GB", accelerator_type=AcceleratorType.Discrete, vram=Memory(quantity=80.0, byte_suffix=ByteSuffix.GiB), max_power_limit=500.0, pci_id="0x20B210DE", compute_sm=80): 4}), numa_conf=None, system_id="XE8545_A100_SXM_80GBx4")
custom_systems['XE8545_maxQ_A100_SXM_80GBx4'] = SystemConfiguration(host_cpu_conf=CPUConfiguration(layout={CPU(name="AMD EPYC 7763 64-Core Processor", architecture=CPUArchitecture.x86_64, core_count=64, threads_per_core=1): 2}), host_mem_conf=MemoryConfiguration(host_memory_capacity=Memory(quantity=1.056499164, byte_suffix=ByteSuffix.TB), comparison_tolerance=0.05), accelerator_conf=AcceleratorConfiguration(layout={GPU(name="NVIDIA A100-SXM4-80GB", accelerator_type=AcceleratorType.Discrete, vram=Memory(quantity=80.0, byte_suffix=ByteSuffix.GiB), max_power_limit=500.0, pci_id="0x20B210DE", compute_sm=80): 4}), numa_conf=None, system_id="XE8545_maxQ_A100_SXM_80GBx4")


###############################
#### END OF CUSTOM SYSTEMS ####
###############################
