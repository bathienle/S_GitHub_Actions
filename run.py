# -*- coding: utf-8 -*-

# * Copyright (c) 2009-2022. Authors: see NOTICE file.
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *      http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# * See the License for the specific language governing permissions and
# * limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from cytomine import CytomineJob
from cytomine.models import UserCollection


def main(argv):
    with CytomineJob.from_cli(argv) as cj:
        cj.job.update(statusComment="Initialization...")

        users = UserCollection().fetch()
        print(users)

        cj.job.update(statusComment="Finished.")


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
