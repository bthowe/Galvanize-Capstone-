cd "/Users/brenthowe/datascience/project"

insheet using "/Users/brenthowe/datascience/project/data/flea_df.csv", comma

reg doses num_skus transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto
reg doses num_skus transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto, vce(robust)

gen dose_per_client = doses/transaction_client

reg dose_per_client num_skus transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto
reg dose_per_client num_skus transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto, vce(robust)

