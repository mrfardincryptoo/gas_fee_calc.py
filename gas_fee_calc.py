def calculate_total_gas_cost(gas_used, gas_price_gwei):
    # 1 Gwei = 10^-9 ETH
    total_cost = gas_used * (gas_price_gwei * 10**-9)
    return total_cost

# Example: 21000 gas units at 50 Gwei
print(f"Total Gas Cost: {calculate_total_gas_calc(21000, 50):.6f} ETH")
