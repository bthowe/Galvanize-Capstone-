clear
cd "/Users/brenthowe/datascience/project"

insheet using "/Users/brenthowe/datascience/project/data/flea_df.csv", comma

gen dose_per_client = doses/transaction_client
gen l_dose_per_client = log(dose_per_client)
gen l_doses = log(doses)
gen num_skus_low = 0
replace num_skus_low = 1 if num_skus<=3
gen num_skus_mid = 0
replace num_skus_mid = 1 if num_skus>3 & num_skus<=5
gen num_skus_high = 0
replace num_skus_high = 1 if num_skus>5


//reg doses num_skus transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto
reg doses num_skus transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto, vce(robust)

//reg dose_per_client num_skus transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto
reg dose_per_client num_skus transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto, vce(robust)

//reg l_dose_per_client num_skus transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto
reg l_dose_per_client num_skus transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto, vce(robust)
//reg l_doses num_skus transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto

reg l_doses num_skus transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto, vce(robust)

//reg dose_per_client num_skus_low num_skus_high transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto
reg dose_per_client num_skus_low num_skus_high transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto, vce(robust)

//reg doses num_skus_low num_skus_high transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto
reg doses num_skus_low num_skus_high transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto, vce(robust)

//reg l_dose_per_client num_skus_low num_skus_high transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto
reg l_dose_per_client num_skus_low num_skus_high transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto, vce(robust)

//reg l_doses num_skus_low num_skus_high transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto
reg l_doses num_skus_low num_skus_high transaction_client weighted_income total_revenue nexgardnetguardnextgardnextguard bravecto sentinelsentinal trifexis comfortis parastar activilactivylactiveyl revolutionrevoluton vectra advantageadvantix advantagemultiadvantagemulti serestosarestoserasto, vce(robust)


//////////////////////
/////////////////////////
//////////////////////////
////////////////////////////
////////////////////////////
///////////////////////////
/////////////////////////
////////////////////////
///////////////////////
clear
insheet using "/Users/brenthowe/datascience/project/data/heartworm_df.csv", comma

gen dose_per_client = doses/transaction_client
gen l_dose_per_client = log(dose_per_client)
gen l_doses = log(doses)
gen num_skus_low = 0
replace num_skus_low = 1 if num_skus<=3
gen num_skus_mid = 0
replace num_skus_mid = 1 if num_skus>3 & num_skus<=5
gen num_skus_high = 0
replace num_skus_high = 1 if num_skus>5


//reg doses num_skus transaction_client weighted_income total_revenue heartgardheartguardhartgardhartg sentinelsentinal proheartprohart trifexis triharttriheart iverhartiverheart interceptorintercepter revolutionrevoluton advantagemultiadvantagemulti
reg doses num_skus transaction_client weighted_income total_revenue heartgardheartguardhartgardhartg sentinelsentinal proheartprohart trifexis triharttriheart iverhartiverheart interceptorintercepter revolutionrevoluton advantagemultiadvantagemulti, vce(robust)

//reg dose_per_client num_skus transaction_client weighted_income total_revenue heartgardheartguardhartgardhartg sentinelsentinal proheartprohart trifexis triharttriheart iverhartiverheart interceptorintercepter revolutionrevoluton advantagemultiadvantagemulti
reg dose_per_client num_skus transaction_client weighted_income total_revenue heartgardheartguardhartgardhartg sentinelsentinal proheartprohart trifexis triharttriheart iverhartiverheart interceptorintercepter revolutionrevoluton advantagemultiadvantagemulti, vce(robust)

//reg l_dose_per_client num_skus transaction_client weighted_income total_revenue heartgardheartguardhartgardhartg sentinelsentinal proheartprohart trifexis triharttriheart iverhartiverheart interceptorintercepter revolutionrevoluton advantagemultiadvantagemulti
reg l_dose_per_client num_skus transaction_client weighted_income total_revenue heartgardheartguardhartgardhartg sentinelsentinal proheartprohart trifexis triharttriheart iverhartiverheart interceptorintercepter revolutionrevoluton advantagemultiadvantagemulti, vce(robust)

//reg l_doses num_skus transaction_client weighted_income total_revenue heartgardheartguardhartgardhartg sentinelsentinal proheartprohart trifexis triharttriheart iverhartiverheart interceptorintercepter revolutionrevoluton advantagemultiadvantagemulti
reg l_doses num_skus transaction_client weighted_income total_revenue heartgardheartguardhartgardhartg sentinelsentinal proheartprohart trifexis triharttriheart iverhartiverheart interceptorintercepter revolutionrevoluton advantagemultiadvantagemulti, vce(robust)

//reg dose_per_client num_skus_low num_skus_high transaction_client weighted_income total_revenue heartgardheartguardhartgardhartg sentinelsentinal proheartprohart trifexis triharttriheart iverhartiverheart interceptorintercepter revolutionrevoluton advantagemultiadvantagemulti
reg dose_per_client num_skus_low num_skus_high transaction_client weighted_income total_revenue heartgardheartguardhartgardhartg sentinelsentinal proheartprohart trifexis triharttriheart iverhartiverheart interceptorintercepter revolutionrevoluton advantagemultiadvantagemulti, vce(robust)

//reg doses num_skus_low num_skus_high transaction_client weighted_income total_revenue heartgardheartguardhartgardhartg sentinelsentinal proheartprohart trifexis triharttriheart iverhartiverheart interceptorintercepter revolutionrevoluton advantagemultiadvantagemulti
reg doses num_skus_low num_skus_high transaction_client weighted_income total_revenue heartgardheartguardhartgardhartg sentinelsentinal proheartprohart trifexis triharttriheart iverhartiverheart interceptorintercepter revolutionrevoluton advantagemultiadvantagemulti, vce(robust)

//reg l_dose_per_client num_skus_low num_skus_high transaction_client weighted_income total_revenue heartgardheartguardhartgardhartg sentinelsentinal proheartprohart trifexis triharttriheart iverhartiverheart interceptorintercepter revolutionrevoluton advantagemultiadvantagemulti
reg l_dose_per_client num_skus_low num_skus_high transaction_client weighted_income total_revenue heartgardheartguardhartgardhartg sentinelsentinal proheartprohart trifexis triharttriheart iverhartiverheart interceptorintercepter revolutionrevoluton advantagemultiadvantagemulti, vce(robust)

//reg l_doses num_skus_low num_skus_high transaction_client weighted_income total_revenue heartgardheartguardhartgardhartg sentinelsentinal proheartprohart trifexis triharttriheart iverhartiverheart interceptorintercepter revolutionrevoluton advantagemultiadvantagemulti
reg l_doses num_skus_low num_skus_high transaction_client weighted_income total_revenue heartgardheartguardhartgardhartg sentinelsentinal proheartprohart trifexis triharttriheart iverhartiverheart interceptorintercepter revolutionrevoluton advantagemultiadvantagemulti, vce(robust)
