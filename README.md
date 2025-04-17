# sysinfolib
Library for obtaining system information and user information.

---

[![PyPI Downloads](https://static.pepy.tech/badge/sysinfolib)](https://pepy.tech/projects/sysinfolib)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/sysinfolib)](https://github.com/smartlegionlab/sysinfolib/)
[![PyPI](https://img.shields.io/pypi/v/sysinfolib)](https://pypi.org/project/sysinfolib)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/sysinfolib?label=pypi%20downloads)](https://pypi.org/project/sysinfolib/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/sysinfolib)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/sysinfolib)](https://github.com/smartlegionlab/sysinfolib/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/sysinfolib)](https://pypi.org/project/sysinfolib)

***

Author and developer: ___A.A. Suvorov.___

***

# Description:

> Library for obtaining system information:

- Internal ip
- External ip
- Memory information
- Disk information
- Network information
- Username
- Computer name
- Operating system version
- Platform information
- Information about architecture
- Processor information
- Python version information
- Information about the city
- Information about the region
- Information about the country
- Information about the provider
- Information about geolocation
- Postcode
- Timezone

***

## Help:

`pip install sysinfolib`

> Attention!!! For some methods to work correctly, an active Internet connection is required.

```python
from sysinfolib.informers import SystemInformer

informer = SystemInformer()
external_ip = informer.ip.get_external_ip()
internal_ip = informer.ip.get_internal_ip()
system_user_name = informer.system.get_system_user_name()
system_name = informer.system.get_system_name()
node_name = informer.system.get_node_name()
release_info = informer.system.get_release_info()
version_info = informer.system.get_version_info()
platform_info = informer.system.get_platform_info()
machine_info = informer.system.get_machine_info()
processor_info = informer.system.get_processor_info()
cpu_info = informer.system.get_cpu_info()
disk_info = informer.system.get_disk_info()
memory_info = informer.system.get_memory_info()
network_interfaces = informer.system.get_network_interfaces()
system_load = informer.system.get_system_load()
python_version = informer.system.get_python_version()
ip_address = informer.user.get_ip_address()
hostname = informer.user.get_hostname()
city = informer.user.get_city()
region = informer.user.get_region()
country = informer.user.get_country()
loc = informer.user.get_loc()
org = informer.user.get_org()
postal = informer.user.get_postal()
timezone = informer.user.get_timezone()

```

> There are other useful classes and methods.

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2024, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------
