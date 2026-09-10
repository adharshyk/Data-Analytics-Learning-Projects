Football Transfers Dashboard (2000-2019)


1. Project Overview

This project provides an interactive visualization dashboard for football (soccer) transfer data from 2000 to 2019. Built with Streamlit, Plotly, and Pandas, the app enables users to explore trends, patterns, and insights in global transfer markets. Users can filter by season, player position, and clubs to gain dynamic perspectives on transfer fees, player movements, and league interactions.


2. Motivation

Football transfers involve billions of euros annually and shape the dynamics of leagues and clubs worldwide. However, raw datasets are difficult to interpret without visual tools. This dashboard allows:

-Fans to analyze trends in their favorite clubs or leagues.

-Analysts to study spending patterns, position-based investments, and age-related market behavior.

-Researchers to understand global football economics.

By converting static data into interactive visuals, we help stakeholders engage more deeply with the data.




3. Target Audience & Typical User Workflow

3.1 Target Audience:

-Football enthusiasts looking to explore high-value transfers.

-Sports journalists needing quick insights for stories.

-Club analysts/scouts seeking data-driven context for transfer trends.

-Students/researchers studying sports economics.


3.2Typical User Workflow:

-Select a season to analyze specific years or explore all seasons.

-Filter by player positions (e.g., Centre-Forward, Winger).

-Drill down to a specific club to see its incoming/outgoing transfers.

-Explore:

	Top 10 transfers.

	Seasonal spending trends.

	Position-based transfer patterns.

	Transfer fee distributions and age breakdowns.

	League-level spending and revenue.

-Optionally download filtered data for offline analysis.



4. Key Design Decisions & Data Challenges

4.1 Design Decisions:

-Streamlit-based UI for simplicity and accessibility.

-Sidebar filters to allow dynamic exploration.

-Multiple tabs separating high-level and detailed insights.

-Sankey diagrams for intuitive visualization of inter-league flows.

4.2 Data Challenges:

-Inconsistent league names required cleaning for Sankey diagrams.

-Missing transfer fees were dropped to preserve analytical accuracy.

-High-value outliers (e.g., Neymar, Ronaldo) skewed averages; median values included for balance.



Insights (Overall)

1. Total Transfer Fees by Season
Between 2000 and 2018, total transfer fees in professional football grew dramatically. In 2000, clubs spent around  1.86 billion. Over the next decade, spending saw slow fluctuations, staying near the  2 billion mark. However, starting from 2013, there was a sharp increase. By 2015, spending crossed  3.4 billion, and peaked in 2017 at nearly  4.75 billion an increase of over 250% compared to 2000.
Interestingly, 2018 saw a decline to around  3.44 billion, suggesting either market correction or financial fair play regulations taking effect.


2. Transfers by Position
The most transferred position was centre-forward, accounting for 25.9% of all transfers. This highlights the demand for reliable goal-scorers, a premium asset for any club. Following this were defenders and midfielders:
* Centre-backs: 15.2%
* Central midfielders: 10.4%
* Attacking midfielders and defensive midfielders each accounted for about 9% and 8.7%, respectively.
This distribution reflects that while strikers are highly sought-after, a solid spine (centre-back to centre-forward) remains crucial in team-building strategies.

3. Average Transfer Fee by Position
When looking at how much clubs paid on average per position, an interesting pattern emerges. Although centre-forwards were the most transferred, they didn t command the highest fees. That honor went to:
* Left wingers: ~ 12.9 million average
* Right wingers: ~ 11.9 million average
This suggests that top wide players, likely involved in marquee deals (e.g., Neymar, Hazard), inflated the averages. Meanwhile:
* Central midfielders: ~ 10 million average
* Centre-backs and defensive midfielders: Around  8.5 9 million
The lowest average transfer fees were observed for fullbacks and goalkeepers, consistent with historical undervaluation of those roles although that has changed somewhat in recent years

4. Transfer Fee by Player Age
Player age played a significant role in determining transfer value. The most common transfer ages were between 23 and 27, which coincides with a player s physical peak. Specifically:
* Age 24 had the most transfers, with an average fee of around  10 million
* Age 27 saw a slightly higher average fee (~ 10.6 million), indicating peak-market value
Surprisingly, age 33 players commanded the highest average fee (~ 13 million), but this is misleading only 15 players at this age were transferred, possibly big names on short-term deals. Generally, after age 30, the number of transfers and their value both decline steeply.


5. Top 10 Leagues by Incoming Transfer Fees
The English Premier League led all others by a wide margin, spending over  14.7 billion, which is 35% of the entire market. The Italian Serie A followed with  7.5 billion, then La Liga with  6.68 billion.
This dominance reflects:
* Higher TV revenues in England
* Increased competitiveness and financial muscle of mid-table EPL clubs
* Desire to attract global talent
France s Ligue 1 and Germany s Bundesliga also featured prominently, though at nearly half the spending of the EPL.


6. Top 10 Leagues by Outgoing Transfer Fees
While the Premier League spent the most, it also sold heavily:  7.25 billion in outgoing fees. However, it sold less than it bought, creating a net spending deficit.
By contrast:
* Serie A and La Liga each had over  7 billion in sales.
* Ligue 1, with  4.4 billion in sales, reflects its role as a "feeder league," exporting top talent to richer leagues.
Portuguese Liga NOS, Dutch Eredivisie, and Brazil s S rie A also stood out as talent-exporting leagues especially known for developing young players and selling them to top European clubs.


7. Inter-League Transfer Flows
Most transfers happened within the same leagues:
* EPL clubs traded  4.5 billion among themselves.
* Serie A:  3.89 billion in internal deals
* La Liga:  1.68 billion in internal activity
The most common cross-league flow was from La Liga to the EPL ( 1.65 billion), followed by Ligue 1 to EPL ( 1.59 billion). This reinforces the Premier League s attraction to top talents from Spain and France.
These flows show how:
* Some leagues act as stepping stones (France, Netherlands, Portugal)
* Others (like EPL) are ultimate destinations for top-tier players


8. Transfer Fee Distribution
Transfer fees followed a right-skewed distribution, meaning:
* Most deals were under  10 million
* The median fee was just  6.5 million, significantly lower than the mean (~ 9.45 million)
* Only 5% of deals crossed  27 million
* The top 1% included mega deals like Neymar ( 222 million)
This indicates that while a few deals grab headlines, the bulk of the market consists of low-to-mid-range transfers.


9. Age Distribution of Transfers
The average age of transferred players was 24.3 years, with the median at 24, confirming that clubs prioritize young or peak-age players.
* 75% of transfers involved players under age 27
* Only 5% of transfers were for players aged 30+
* The youngest players were teenagers, and the oldest was 35



Final Observations:
* The Premier League dominates in both buying and selling, suggesting a dynamic and financially aggressive market.
* Centre-forwards are key to team investment, but wingers demand higher fees on average due to marquee names.
* Peak value comes around age 24 27, aligning with clubs  strategic acquisition windows.
* Distribution is highly skewed a few blockbuster deals dramatically influence averages, but most deals are modest.










How to Run:

1. Go to the location where the app.py and dataset is located and run command prompt from there.

2. Install dependencies:(if not installed)
	pip install streamlit pandas plotly

3. Run the app:
	streamlit run app.py
	Open the provided localhost URL in your browser

NB:In Inter-League Transfer Flows Chart, if you select all in the filtering, sometimes the chart is crashing/page is not responding