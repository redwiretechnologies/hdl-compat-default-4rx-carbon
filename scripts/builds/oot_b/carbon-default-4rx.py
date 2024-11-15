# SPDX-License-Identifier: Apache-2.0

from . import oot_builds

carbon_default_4rx_dict = {  "carbon"   : {
                                            "images"    : ["default-4rx"],
                                           },
                             "carbon-carp"   : {
                                                "images"    : ["default-4rx"],
                                               }
                          }

oot_builds.merge(oot_builds.supported_oot, carbon_default_4rx_dict)
