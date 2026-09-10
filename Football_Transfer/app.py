import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load data
df = pd.read_csv('top250-00-19_cleaned.csv')
df['Transfer_fee'] = pd.to_numeric(df['Transfer_fee'], errors='coerce')
df = df.dropna(subset=['Transfer_fee'])
df['Season_Start'] = df['Season'].str[:4].astype(int)

# Clean up league names
df['League_from'] = df['League_from'].astype(str).str.strip()
df['League_to'] = df['League_to'].astype(str).str.strip()

# Sidebar filters
st.sidebar.title("Football Transfers Dashboard")
season_options = sorted(df['Season'].unique())
selected_season = st.sidebar.selectbox("Select Season", ["All"] + season_options)
position_options = sorted(df['Position'].unique())
selected_positions = st.sidebar.multiselect("Select Position(s)", position_options, default=position_options)

# Club dropdown
all_clubs = sorted(set(df['Team_from'].dropna().unique()).union(set(df['Team_to'].dropna().unique())))
selected_club = st.sidebar.selectbox("Select Club (From/To)", ["All"] + all_clubs)

# Filter data
filtered_df = df.copy()
if selected_season != "All":
    filtered_df = filtered_df[filtered_df['Season'] == selected_season]
if selected_positions:
    filtered_df = filtered_df[filtered_df['Position'].isin(selected_positions)]
if selected_club != "All":
    filtered_df = filtered_df[
        (filtered_df['Team_from'] == selected_club) | (filtered_df['Team_to'] == selected_club)
    ]

# Top 10 transfers
top_10 = filtered_df.nlargest(10, 'Transfer_fee').copy()
top_10['Fee (€M)'] = top_10['Transfer_fee'] / 1e6

# Transfer fees over time
season_trend = filtered_df.groupby('Season_Start')['Transfer_fee'].sum().reset_index()

# Position analysis
position_counts = filtered_df['Position'].value_counts().reset_index()
position_counts.columns = ['Position', 'Count']
position_avg = filtered_df.groupby('Position')['Transfer_fee'].mean().sort_values(ascending=False).reset_index()

# League analysis
league_incoming = filtered_df.groupby('League_to')['Transfer_fee'].sum().reset_index().sort_values('Transfer_fee', ascending=False).head(10)
league_outgoing = filtered_df.groupby('League_from')['Transfer_fee'].sum().reset_index().sort_values('Transfer_fee', ascending=False).head(10)

# Age distribution
age_distribution = filtered_df.groupby('Age')['Transfer_fee'].sum().reset_index()

# League flow analysis (top leagues only, with cleaning)
top_leagues_in = league_incoming['League_to'].tolist()
top_leagues_out = league_outgoing['League_from'].tolist()
top_leagues = list(set(top_leagues_in + top_leagues_out))
def map_league(league):
    return league if league in top_leagues else 'Other'
filtered_df['League_from_sankey'] = filtered_df['League_from'].apply(map_league)
filtered_df['League_to_sankey'] = filtered_df['League_to'].apply(map_league)
league_flow = filtered_df.groupby(['League_from_sankey', 'League_to_sankey'])['Transfer_fee'].sum().reset_index()
nodes = list(set(league_flow['League_from_sankey'].unique()).union(set(league_flow['League_to_sankey'].unique())))
node_indices = {name: i for i, name in enumerate(nodes)}
sources = league_flow['League_from_sankey'].map(node_indices)
targets = league_flow['League_to_sankey'].map(node_indices)
values = league_flow['Transfer_fee'] / 1e6  # in millions

# Main dashboard
st.title("Football Transfers Dashboard (2000-2019)")

tab = st.sidebar.radio("Select View", [
    "Top Transfers",
    "Seasonal Trend",
    "Position Analysis",
    "Age vs. Fee",
    "League Analysis",
    "Market Trends"
])

if tab == "Top Transfers":
    st.header("Top 10 Most Expensive Transfers")
    st.dataframe(top_10[['Name', 'Team_from', 'Team_to', 'Fee (€M)', 'Season']].reset_index(drop=True), use_container_width=True)

elif tab == "Seasonal Trend":
    st.header("Total Transfer Fees by Season")
    fig = px.line(
        season_trend,
        x='Season_Start',
        y='Transfer_fee',
        markers=True,
        labels={'Season_Start': 'Season Start Year', 'Transfer_fee': 'Total Fees (€)'},
        title='Total Transfer Fees by Season'
    )
    fig.update_traces(line=dict(width=3))
    st.plotly_chart(fig, use_container_width=True)

elif tab == "Position Analysis":
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Transfers by Position")
        fig1 = px.pie(
            position_counts,
            names='Position',
            values='Count',
            title='Transfers by Position'
        )
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.subheader("Average Transfer Fee by Position")
        fig2 = px.bar(
            position_avg,
            x='Transfer_fee',
            y='Position',
            orientation='h',
            labels={'Transfer_fee': 'Average Fee (€)', 'Position': 'Position'},
            title='Average Transfer Fee by Position'
        )
        st.plotly_chart(fig2, use_container_width=True)

elif tab == "Age vs. Fee":
    st.header("Transfer Fee by Player Age")
    fig = px.scatter(
        filtered_df,
        x='Age',
        y='Transfer_fee',
        color='Position',
        hover_data=['Name', 'Team_from', 'Team_to', 'Season'],
        labels={'Transfer_fee': 'Transfer Fee (€)'},
        title='Transfer Fee by Player Age',
        log_y=True
    )
    st.plotly_chart(fig, use_container_width=True)

elif tab == "League Analysis":
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top 10 Leagues by Incoming Fees")
        fig1 = px.bar(
            league_incoming,
            x='Transfer_fee',
            y='League_to',
            orientation='h',
            labels={'Transfer_fee': 'Total Fees (€)', 'League_to': 'Destination League'},
            title='Top Destination Leagues by Spending'
        )
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.subheader("Top 10 Leagues by Outgoing Fees")
        fig2 = px.bar(
            league_outgoing,
            x='Transfer_fee',
            y='League_from',
            orientation='h',
            labels={'Transfer_fee': 'Total Fees (€)', 'League_from': 'Origin League'},
            title='Top Origin Leagues by Revenue'
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Inter-League Transfer Flows (Top Leagues and Other)")
    sankey_fig = go.Figure(data=[
        go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=nodes,
                color="#5DA5DA"
            ),
            link=dict(
                source=sources,
                target=targets,
                value=values,
                hovertemplate='%{source.label} → %{target.label}<br>%{value:.1f}M€'
            )
        )
    ])
    sankey_fig.update_layout(
        title_text="Inter-League Transfer Flows (Top Leagues and Other)",
        font_size=16,
        height=700,
        width=1100
    )
    st.plotly_chart(sankey_fig, use_container_width=True)

elif tab == "Market Trends":
    st.header("Transfer Fee Distribution")
    fig = px.box(
        filtered_df,
        y='Transfer_fee',
        points='all',
        labels={'Transfer_fee': 'Transfer Fee (€)'},
        title='Distribution of Transfer Fees'
    )
    st.plotly_chart(fig, use_container_width=True)

    st.header("Age Distribution of Transfers")
    fig2 = px.bar(
        age_distribution,
        x='Age',
        y='Transfer_fee',
        labels={'Transfer_fee': 'Total Fees (€)'},
        title='Transfer Spending by Player Age'
    )
    st.plotly_chart(fig2, use_container_width=True)

# Optional: Download filtered data
st.sidebar.download_button("Download Filtered Data", filtered_df.to_csv(index=False), "filtered_transfers.csv")
