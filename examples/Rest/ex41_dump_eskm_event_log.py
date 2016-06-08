# Copyright 2016 Hewlett Packard Enterprise Development, LP.
 #
 # Licensed under the Apache License, Version 2.0 (the "License"); you may
 # not use this file except in compliance with the License. You may obtain
 # a copy of the License at
 #
 #      http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 # License for the specific language governing permissions and limitations
 # under the License.

import sys
from restobject import RestObject

def ex41_dump_eskm_event_log(restobj):
    sys.stdout.write("\nEXAMPLE 41: Dump ESKM Event Log\n")
    instances = restobj.search_for_type("SecurityService.")

    for instance in instances:
        tmp = restobj.rest_get(instance["href"])
        response = restobj.rest_get(tmp.dict["links"]["ESKM"]["href"])
        for entry in response.dict["ESKMEvents"]:
            sys.stdout.write(entry["Timestamp"] + "\n" \
                             + entry["Event"] + "\n")

if __name__ == "__main__":
 
    iLO_host = "https://10.0.0.100"
    iLO_account =  "admin"
    iLO_password =  "password"
    
    # Create a REST object
    REST_OBJ = RestObject(iLO_host, iLO_account, iLO_password)
    ex41_dump_eskm_event_log(REST_OBJ)
    