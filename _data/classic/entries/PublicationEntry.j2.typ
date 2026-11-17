// An empty first row lets publications use the full width while retaining regular entry spacing.
#regular-entry([ ], [ ], main-column-second-row: [
{% for line in entry.main_column.splitlines() %}
  {{ line|indent(2) }}

{% endfor %}
])
