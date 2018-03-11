#!/usr/bin/env python
"""Cloud Storage"""

__author__ = "Petar Stoyanov"

import math

def main():
    """Docstring"""

    monthly_budget = float(input())
    concurrent_users = int(input())
    data_gb = int(input())
    hosts_count = int(input())
    up_time = float(input())

    server_cost_hour = math.ceil(concurrent_users / 50) * 2
    storage_cost_hour = math.ceil(data_gb / 0.5) * 0.5
    server_storage_monthly = (server_cost_hour + storage_cost_hour) * 24 * 30
    hosts_cost_monthly = hosts_count * 10

    monthly_cost = (server_storage_monthly + hosts_cost_monthly) * (up_time / 100.0)

    budget_left = monthly_budget - monthly_cost

    if budget_left >= 0:
        print(f'Clouds Ahoy! Monthly cost: ${monthly_cost:.2f} (${budget_left:.2f} leftover)')
    else:
        print(f'Stay Grounded! Monthly cost: ${monthly_cost:.2f} (Need ${abs(budget_left):.2f} more)')


if __name__ == '__main__':
    main()
