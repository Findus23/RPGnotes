from django.contrib.postgres.indexes import GinIndex

NameSearchIndex = GinIndex(
    name='%(class)s_name_gin_idx',
    fields=['name'],
    opclasses=['gin_trgm_ops'],
)
