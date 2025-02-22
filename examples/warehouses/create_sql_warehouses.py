import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created = w.warehouses.create(name=f'sdk-{time.time_ns()}',
                              cluster_size="2X-Small",
                              max_num_clusters=1,
                              auto_stop_mins=10).result()

# cleanup
w.warehouses.delete(delete=created.id)
