# import ray
# import time
#
# # Start Ray.
# ray.init(_temp_dir='temp', include_dashboard=False)
# assert ray.is_initialized()
#
# @ray.remote
# def f(x):
#     time.sleep(1)
#     return x
#
#
# # Start 4 tasks in parallel.
# result_ids = []
# for i in range(4):
#     result_ids.append(f.remote(i))
#
# # Wait for the tasks to complete and retrieve the results.
# # With at least 4 cores, this will take 1 second.
# results = ray.get(result_ids)  # [0, 1, 2, 3]
# print(results)

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import ray
import time

print('Successfully imported ray!')

ray.init(num_cpus=8, ignore_reinit_error=True)


@ray.remote
def slow_function(i):
    time.sleep(1)
    return i


start_time = time.time()

results = []
for i in range(4):
    results.append(ray.get(slow_function.remote(i)))

duration = time.time() - start_time
print('Executing the for loop took {:.3f} seconds.'.format(duration))
print('The results are:', results)
print('Run the next cell to check if the exercise was performed correctly.')
