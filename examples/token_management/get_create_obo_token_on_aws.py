import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import iam

w = WorkspaceClient()

groups = w.groups.group_display_name_to_id_map(iam.ListGroupsRequest())

spn = w.service_principals.create(display_name=f'sdk-{time.time_ns()}',
                                  groups=[iam.ComplexValue(value=groups["admins"])])

obo = w.token_management.create_obo_token(application_id=spn.application_id, lifetime_seconds=60)

by_id = w.token_management.get(get=obo.token_info.token_id)

# cleanup
w.service_principals.delete(delete=spn.id)
w.token_management.delete(delete=obo.token_info.token_id)
